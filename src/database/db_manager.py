from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from models import CharIdea, Character, RewrittenPrompts, AnalysedPrompt, KeyDescription, DescriptionToIdea, Classes, BestChar
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
		classes, key_descriptions, rewritten_prompts = self.extract_analysed_data(analysed_dict)

		session = self.Session()
		try:
			# user_prompt abspeichern+
			char_idea = CharIdea(user_prompt=prompt)
			session.add(char_idea)

			session.commit()

			# gibt die nueste / höchste idea_id heraus
			new_idea_id = session.query(func.max(CharIdea.idea_id)).scalar()

			# classes abpseichern
			# classes abgleichen und entsprechende classes auf True setzten
			possible_classes = ['barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk', 'paladin', 'ranger', 'rogue', 'sorcerer', 'warlock', 'wizard']
			dnd_classes = Classes(idea_id=new_idea_id,
								  barbarian='barbarian' in classes,
								  bard='bard' in classes,
								  cleric='cleric' in classes,
								  druid='druid' in classes,
								  fighter='fighter' in classes,
								  monk='monk' in classes,
								  paladin='paladin' in classes,
								  ranger='ranger' in classes,
								  rogue='rogue' in classes,
								  sorcerer='sorcerer' in classes,
								  warlock='warlock' in classes,
								  wizard='wizard' in classes)


			# keywords abspeichern
			# TODO: keywords einbauen mit verbindungstable
			# rewritten_prompts abspeichern


			session.commit()
		except Exception as e:
			session.rollback()
			raise e
		finally:
			session.close()

	def extract_analysed_data(self, analysed_dict: dict[list[str]]) -> tuple:
		"""
		extrahiert alle daten aus dem dictionary und gibt sie als tuple zurück
		"""
		classes = analysed_dict["matched_classes"]
		key_words = analysed_dict["keywords"]
		rewritten_prompts = analysed_dict["rewritten_prompt_template"]

		return classes, key_words, rewritten_prompts


	def load_character_data(self):
		session = self.Session()
		try:
			classes = session.query(ClassModel).all()
			key_descriptions = session.query(KeyDescriptionModel).all()
			rewritten_prompts = session.query(RewrittenPromptModel).all()
			return {
				'classes': classes,
				'key_descriptions': key_descriptions,
				'rewritten_prompts': rewritten_prompts
			}
		finally:
			session.close()

	def save_generated_characters(self, characters: List[Dict]):
		session = self.Session()
		try:
			for character in characters:
				character_entry = CharacterModel(**character)
				session.add(character_entry)
			session.commit()
		except Exception as e:
			session.rollback()
			raise e
		finally:
			session.close()

	def delete_character_by_idea_id(self, idea_id: int):
		session = self.Session()
		try:
			session.query(CharIdeaModel).filter_by(idea_id=idea_id).delete()
			session.query(DescriptionToIdeaModel).filter_by(idea_id=idea_id).delete()
			session.query(RewrittenPromptModel).filter_by(idea_id=idea_id).delete()
			session.query(ClassModel).filter_by(idea_id=idea_id).delete()
			session.query(CharacterModel).filter_by(idea_id=idea_id).delete()
			session.query(BestCharModel).filter_by(idea_id=idea_id).delete()
			session.commit()
		except Exception as e:
			session.rollback()
			raise e
		finally:
			session.close()
