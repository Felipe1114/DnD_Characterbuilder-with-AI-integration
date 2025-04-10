from sqlalchemy import func, select, delete
from sqlalchemy.orm import sessionmaker
from models import CharIdea, Character, RewrittenPrompts, KeyDescription, DescriptionToIdea, Classes, BestChar
from typing import List, Dict

class DatabaseManager:
	"""
	managet die interaktionene mit der datenbank

	erhaltene daten:
	{
		"matched_classes": ["paladin", "fighter", "cleric"],
		"keywords": ["Bote des Lichts", "großes Schwert", "Elemente beherrschen", "strahlende Rüstung"],
		"rewritten_prompt_template": [
		"Ein paladin des Lichts. Er hat ein großes Schwert und beherrscht die Elemente. Er ist in eine strahlende Rüstung getaucht.",
		"Ein fighter des Lichts. Er hat ein großes Schwert und beherrscht die Elemente. Er ist in eine strahlende Rüstung getaucht.",
		"Ein cleric des Lichts. Er hat ein großes Schwert und beherrscht die Elemente. Er ist in eine strahlende Rüstung getaucht."
		]
	}
	"""
	def __init__(self, engine):
		self.Session = sessionmaker(bind=engine)

	def save_user_prompt(self, prompt: str, analysed_dict: dict[list[str]]):
		"""
		speichert alle daten aus der Analyse des user_prompts
		"""
		# extrahiert die daten aus der LLM_antwort
		possible_classes, key_descriptions, rewritten_prompts = self.extract_analysed_data(analysed_dict)

		session = self.Session()
		try:
			# user_prompt abspeichern
			self.save_char_idea(prompt, session)

			# gibt die nueste / höchste idea_id heraus
			stmt_new_idea = select(func.max(CharIdea.idea_id))
			new_idea_id = session.scalars(stmt_new_idea).first()

			# possible_classes abspeichern
			self.save_classes(new_idea_id, session)

			# key_descriptions abspeichern
			self.save_key_descriptions(key_descriptions, new_idea_id, session)

			# umgeschriebene user_prompts abspeichern
			self.save_rewritten_prompts(new_idea_id, rewritten_prompts, session)

			session.flush()
		except Exception as e:
			session.rollback()
			raise e
		finally:
			session.close()

	def save_char_idea(self, prompt, session):
		"""Saves user_prompt in db"""
		#TODO: Error handling einbauen
		char_idea = CharIdea(user_prompt=prompt)
		session.add(char_idea)
		session.flush()

	def save_rewritten_prompts(self, new_idea_id, rewritten_prompts, session):
		"""saves the three rewritten user_prompts in db"""
		#TODO: Error handling einbauen

		for i, r_prompt in enumerate(rewritten_prompts):
			rewritten_promp = RewrittenPrompts(idea_id=new_idea_id, rewritten_promp=r_prompt)

			session.add(rewritten_promp)

	def save_key_descriptions(self, key_descriptions, new_idea_id, session):
		"""saves the key_descriptions from user_prompt in db"""
		#TODO: Error handling einbauen

		for i, key_description in enumerate(key_descriptions):

			stmt_all = select(KeyDescription.description)
			all_key_descriptions = session.scalars(stmt_all).all()
			if not key_description in all_key_descriptions:

				# description in Table einfügen
				description = KeyDescription(description=key_description)
				session.add(description)

				# der aktuelle höchste description_id wert für den Verbindungstable
				stmt_max = select(func.max(KeyDescription.description_id))
				description_id = session.scalars(stmt_max).first()

			else:
				# wenn description bereits in db, description_id von existierender descripton finden
				description_id = session.scalars(
					select(KeyDescription.description_id).where(KeyDescription.description == key_description)).first()

			description_to_idea = DescriptionToIdea(idea_id=new_idea_id, description_id=description_id)

			session.add(description_to_idea)

	def save_classes(self, new_idea_id, session):
		"""saves the three best fitting dnd-classes for user_prompt in db"""
		#TODO: Error handling einbauen

		# classes abpseichern
		# classes abgleichen und entsprechende classes auf True setzten
		possible_classes = ['barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk', 'paladin', 'ranger', 'rogue',
							'sorcerer', 'warlock', 'wizard']
		dnd_classes = Classes(idea_id=new_idea_id,
							  barbarian='barbarian' in possible_classes,
							  bard='bard' in possible_classes,
							  cleric='cleric' in possible_classes,
							  druid='druid' in possible_classes,
							  fighter='fighter' in possible_classes,
							  monk='monk' in possible_classes,
							  paladin='paladin' in possible_classes,
							  ranger='ranger' in possible_classes,
							  rogue='rogue' in possible_classes,
							  sorcerer='sorcerer' in possible_classes,
							  warlock='warlock' in possible_classes,
							  wizard='wizard' in possible_classes)
		session.add(dnd_classes)

	def extract_analysed_data(self, analysed_dict: dict[list[str]]) -> tuple:
		"""
		extrahiert alle daten aus dem dictionary und gibt sie als tuple zurück
		"""
		#TODO: Error handling einbauen -> richtiges datenformat

		classes: list[str] = analysed_dict["matched_classes"]
		key_words: list[str] = analysed_dict["keywords"]
		rewritten_prompts: list[str] = analysed_dict["rewritten_prompt_template"]

		return classes, key_words, rewritten_prompts


	# TODO write method to get all char_ideas
	def load_all_char_ideas(self):
		"""lädt alle char_ideen und gibt sie als dict mit key=id und value=idea zurück"""
		session = self.Session()

		try:
			stmt = select(CharIdea)
			result = session.execute(stmt).all()

			if not result:
				return {}

			return result

		except Exception as e:
			session.rollback()
			raise e
		finally:
			session.close()

	def load_character_data(self, idea_id):
		"""loads all data form the analysed user_prompt for creating a system prompt for character creation"""
		#TODO: Error handling einbauen

		session = self.Session()
		try:
			classes_for_idea =  self.load_classes_for_idea(idea_id, session)

			descriptions_for_idea = self.load_key_description_for_idea(idea_id, session)

			rewritten_prompts = self.load_rewritten_prompts(idea_id, session)

			return {
				'classes': classes_for_idea,
				'key_descriptions': descriptions_for_idea,
				'rewritten_prompts': rewritten_prompts
			}
		finally:
			session.close()

	def load_rewritten_prompts(self, idea_id, session):
		"""loads all rewritten prompts with the idea_id i"""
		stmt = select(RewrittenPrompts.rewritten_prompt).where(RewrittenPrompts.idea_id == idea_id)
		result = session.execute(stmt).all()

		if result:
			return result

		return []

	def load_key_description_for_idea(self, idea_id, session):
		"""
		gibt alle descriptions zurück, die eine key-key paarung mit der idea_id haben

		"""
		#TODO: Error handling einbauen

		descriptions: list[str] = []

		stmt = select(DescriptionToIdea.description_id).where(DescriptionToIdea.idea_id == idea_id)
		result = session.execute(stmt).all()

		if result:
			for i, description_id in enumerate(result):
				description: str = select(KeyDescription.description).where(KeyDescription.description_id == description_id).first()

				if description:
					descriptions.append(description)

		return descriptions

	def load_classes_for_idea(self, idea_id, session):
		"""gives back all class_names from Table Classes, wich are True"""
		#TODO: Error handling einbauen

		stmt = select(Classes).where(Classes.idea_id == idea_id)
		result = session.execute(stmt).all()

		if result:
			class_names = [column for column in Classes.__table__.columns if getattr(result, column.name) is True]
			return class_names
		return []

	def save_generated_characters(self, characters: List[Dict]):
		#TODO: Error handling einbauen

		session = self.Session()
		try:
			for character in characters:
				character_entry = Character(**character)
				session.add(character_entry)

			session.commit()

		except Exception as e:
			session.rollback()
			raise e
		finally:
			session.close()

	def delete_character_by_idea_id(self, idea_id: int):
		#TODO: Error handling einbauen

		session = self.Session()
		try:
			# list of all models, which containing the idea_id as foregin_key
			models = [CharIdea, DescriptionToIdea, RewrittenPrompts, Classes, Character, BestChar]

			# looping thrue all models
			for i, model in enumerate(models):

				# deleting all colums with the idea_id == idea_id
				stmt = delete(model).where(model.idea_id == idea_id)
				session.execute(stmt)

			session.commit()

		except Exception as e:
			session.rollback()
			raise e
		finally:
			session.close()
