from sqlalchemy import func, select, delete
from sqlalchemy.orm import sessionmaker
from src.database.models import CharIdea, Character, RewrittenPrompts, KeyDescription, DescriptionToIdea, Classes, BestChar
from typing import List, Dict
from src.debug.debug_log import DebugLog

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
	
	@DebugLog.debug_log
	def save_user_prompt(self, prompt: str, analysed_dict: dict[str, list[str]]):
		"""
		speichert alle daten aus der Analyse des user_prompts
		"""
		# extrahiert die daten aus der LLM_antwort
		possible_classes, key_descriptions, rewritten_prompts = self.extract_analysed_data(analysed_dict)

		session = self.Session()
		# user_prompt abspeichern
		self._save_char_idea(prompt, session)

		# gibt die nueste / höchste idea_id heraus
		stmt_new_idea = select(func.max(CharIdea.idea_id))
		new_idea_id = session.scalars(stmt_new_idea).first()

		# possible_classes abspeichern
		self._save_classes(new_idea_id, session)

		# key_descriptions abspeichern
		self._save_key_descriptions(key_descriptions, new_idea_id, session)

		# umgeschriebene user_prompts abspeichern
		self._save_rewritten_prompts(new_idea_id, rewritten_prompts, session)
		session.commit()
		session.close()
	
	@DebugLog.debug_log
	def _save_char_idea(self, prompt, session):
		"""Saves user_prompt in db"""
		char_idea = CharIdea(user_prompt=prompt)
		session.add(char_idea)
		session.flush()
	
	@DebugLog.debug_log
	def _save_rewritten_prompts(self, new_idea_id, rewritten_prompts, session):
		"""saves the three rewritten user_prompts in db"""
		for i, r_prompt in enumerate(rewritten_prompts):
			rewritten_prompt = RewrittenPrompts(idea_id=new_idea_id, rewritten_prompt=r_prompt)
			session.add(rewritten_prompt)
	
	@DebugLog.debug_log
	def _save_key_descriptions(self, key_descriptions, new_idea_id, session):
		"""saves the key_descriptions from user_prompt in db"""
		for i, key_description in enumerate(key_descriptions):
			stmt_all = select(KeyDescription.description)
			all_key_descriptions = session.scalars(stmt_all).all()
			if not key_description in all_key_descriptions:
				description = KeyDescription(description=key_description)
				session.add(description)
				stmt_max = select(func.max(KeyDescription.description_id))
				description_id = session.scalars(stmt_max).first()
			else:
				description_id = session.scalars(
					select(KeyDescription.description_id).where(KeyDescription.description == key_description)).first()

			description_to_idea = DescriptionToIdea(idea_id=new_idea_id, description_id=description_id)
			session.add(description_to_idea)
	
	@DebugLog.debug_log
	def _save_classes(self, new_idea_id, session):
		"""saves the three best fitting dnd-classes for user_prompt in db"""
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
	
	@DebugLog.debug_log
	def extract_analysed_data(self, analysed_dict: dict[str, list[str]]) -> tuple:
		"""
		extrahiert alle daten aus dem dictionary und gibt sie als tuple zurück
		"""
		classes: list[str] = analysed_dict["matched_classes"]
		key_words: list[str] = analysed_dict["keywords"]
		rewritten_prompts: list[str] = analysed_dict["rewritten_prompt_template"]
		return classes, key_words, rewritten_prompts
	
	@DebugLog.debug_log
	def load_all_char_ideas(self):
		"""lädt alle char_ideen und gibt sie als dict mit key=id und value=idea zurück"""
		session = self.Session()

		stmt = select(CharIdea)
		result = session.execute(stmt).all()

		if not result:
			return {}

		return result
	
	@DebugLog.debug_log
	def load_character_data(self, idea_id):
		"""loads all data form the analysed user_prompt for creating a system prompt for character creation"""
		session = self.Session()
		classes_for_idea =  self._load_classes_for_idea(idea_id, session)

		descriptions_for_idea = self._load_key_description_for_idea(idea_id, session)

		rewritten_prompts = self._load_rewritten_prompts(idea_id, session)

		return {
			'classes': classes_for_idea,
			'key_descriptions': descriptions_for_idea,
			'rewritten_prompts': rewritten_prompts
		}
	
	@DebugLog.debug_log
	def _load_rewritten_prompts(self, idea_id, session):
		"""loads all rewritten prompts with the idea_id i"""
		stmt = select(RewrittenPrompts.rewritten_prompt).where(RewrittenPrompts.idea_id == idea_id)
		result = session.execute(stmt).all()

		if result:
			return result

		return []
	
	@DebugLog.debug_log
	def _load_key_description_for_idea(self, idea_id, session):
		"""
		gibt alle descriptions zurück, die eine key-key paarung mit der idea_id haben
		"""
		descriptions: list[str] = []
		stmt = select(DescriptionToIdea.description_id).where(DescriptionToIdea.idea_id == idea_id)
		result = session.execute(stmt).all()
		if result:
			for i, description_id in enumerate(result):
				description: str = select(KeyDescription.description).where(KeyDescription.description_id == description_id).first()
				if description:
					descriptions.append(description)
		return descriptions
	
	@DebugLog.debug_log
	def _load_classes_for_idea(self, idea_id, session):
		"""gives back all class_names from Table Classes, wich are True"""
		stmt = select(Classes).where(Classes.idea_id == idea_id)
		result = session.execute(stmt).first()
		if result:
			class_names = [column.name for column in Classes.__table__.columns if getattr(result[0], column.name) is True and column.name != "class_table_id" and column.name != "idea_id"]
			return class_names
		return []
	
	@DebugLog.debug_log
	def save_generated_characters(self, characters: List[Dict]):
		"speichert die erstellen charactere in der db ab"
		session = self.Session()
		for character in characters:
			character_entry = Character(**character)
			session.add(character_entry)

		session.commit()
	
	@DebugLog.debug_log
	def delete_character_by_idea_id(self, idea_id: int):
		"""Löscht eine char_idea mit allen colums, die damit verbunden sind"""
		session = self.Session()
		# list of all models, which containing the idea_id as foregin_key
		models = [CharIdea, DescriptionToIdea, RewrittenPrompts, Classes, Character, BestChar]

		# looping thrue all models
		for i, model in enumerate(models):

			# deleting all colums with the idea_id == idea_id
			stmt = delete(model).where(model.idea_id == idea_id)
			session.execute(stmt)

		session.commit()
