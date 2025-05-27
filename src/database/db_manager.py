from sqlalchemy import func, select, delete, create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError, PendingRollbackError
from src.database.models import CharIdea, Character, RewrittenPrompts, KeyDescription, DescriptionToIdea, Classes, BestChar
from typing import List
from pydantic import BaseModel
from src.handle_data.env_loader import EnvLoader
from src.debug.debug_helper import DebugHelper
import json


SQL_ALCHEMY_ERROR =(PendingRollbackError, SQLAlchemyError, IntegrityError, OperationalError)

class Prompt(BaseModel):
	"""Defines the Input type and validates it"""
	text: str
	
class AnalysedPrompt(BaseModel):
	matched_classes: list
	keywords: list
	rewritten_prompt_template: list

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
	def __init__(self, test_case=False, temp_engine=None):
		# if I want to test the Databasemanager class with a temporary database
		if test_case:
			self.session = sessionmaker(bind=temp_engine)
		
		else:
			self.db_path = EnvLoader.db_path()
			engine = create_engine(self.db_path, pool_pre_ping=True, echo=True)
			self.Session = sessionmaker(bind=engine)
			
			# sets the DebugHelber on or off
			DebugHelper.activ(activ=True)
	
	def save_user_prompt(self, prompt: Prompt, analysed_dict: AnalysedPrompt):
		"""
		speichert alle daten aus der Analyse des user_prompts
		"""
		# extrahiert die daten aus der LLM_antwort
		possible_classes, key_descriptions, rewritten_prompts = self.extract_analysed_data(analysed_dict)

		session = self.Session()
		try:
			# user_prompt abspeichern
			self._save_char_idea(prompt, session)

			# gibt die nueste / höchste idea_id heraus
			stmt_new_idea = select(func.max(CharIdea.idea_id))
			new_idea_id = session.scalars(stmt_new_idea).first()

			# possible_classes abspeichern
			self._save_classes(possible_classes, new_idea_id, session)

			# key_descriptions abspeichern
			self._save_key_descriptions(key_descriptions, new_idea_id, session)

			# umgeschriebene user_prompts abspeichern
			self._save_rewritten_prompts(new_idea_id, rewritten_prompts, session)
			session.commit()
			
		except SQL_ALCHEMY_ERROR as e:
			session.rollback()
			raise e
		finally:
			session.close()
	
	def _save_char_idea(self, prompt, session):
		"""Saves user_prompt in db"""
		try:
			char_idea = CharIdea(user_prompt=prompt.text)
			session.add(char_idea)
			session.flush()
		except SQL_ALCHEMY_ERROR as e:
			session.rollback()
			raise e
	
	def _save_rewritten_prompts(self, new_idea_id, rewritten_prompts, session):
		"""saves the three rewritten user_prompts in db"""
		try:
			for i, r_prompt in enumerate(rewritten_prompts):
				rewritten_prompt = RewrittenPrompts(idea_id=new_idea_id, rewritten_prompt=r_prompt)
				session.add(rewritten_prompt)
		except SQL_ALCHEMY_ERROR as e:
			session.rollback()
			raise e
	
	def _save_key_descriptions(self, key_descriptions, new_idea_id, session:Session):
		"""saves the key_descriptions from user_prompt in db"""
		try:
			for i, key_description in enumerate(key_descriptions):
				stmt_all = select(KeyDescription.description)
				all_key_descriptions = session.scalars(stmt_all).all()
				if not key_description in all_key_descriptions:
					description = KeyDescription(description=key_description)
					session.add(description)
					session.flush()
					description_id = description.description_id
				else:
					description_id = session.scalars(
						select(KeyDescription.description_id).where(KeyDescription.description == key_description)).first()

				description_to_idea = DescriptionToIdea(idea_id=new_idea_id, description_id=description_id)
				session.add(description_to_idea)
		except SQL_ALCHEMY_ERROR as e:
			session.rollback()
			raise e
	
	def _save_classes(self, possible_classes, new_idea_id, session):
		"""saves the three best fitting dnd-classes for user_prompt in db"""
		try:
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
		except SQL_ALCHEMY_ERROR as e:
			session.rollback()
			raise e
	
	def extract_analysed_data(self, analysed_dict: AnalysedPrompt) -> tuple:
		"""
		extrahiert alle daten aus dem dictionary und gibt sie als tuple zurück
		"""
		classes: list[str] = analysed_dict["matched_classes"]
		key_words: list[str] = analysed_dict["keywords"]
		rewritten_prompts: list[str] = analysed_dict["rewritten_prompt_template"]
		return classes, key_words, rewritten_prompts
	
	def load_all_char_ideas(self):
		"""lädt alle char_ideen und gibt sie als dict mit key=id und value=idea zurück"""
		session = self.Session()
		try:
			stmt = select(CharIdea)
			result = session.execute(stmt).all()

			if not result:
				return {}

			return result
		except SQL_ALCHEMY_ERROR as e:
			session.rollback()
			raise e
		finally:
			session.close()
	
	def load_character_prompts(self, idea_id):
		"""loads all data form the analysed user_prompt for creating a system prompt for character creation"""
		session = self.Session()
		try:
			# checks if idea_id is an interger
			if not isinstance(idea_id, int):
				raise ValueError("idea_id hase to be an integer")
			
			classes_for_idea =  self._load_classes_for_idea(idea_id, session)

			descriptions_for_idea = self._load_key_description_for_idea(idea_id, session)

			rewritten_prompts = self._load_rewritten_prompts(idea_id, session)
			
			result = {
				'classes': classes_for_idea, # -> three classes [class_1, class_2, class_3]
				'key_descriptions': descriptions_for_idea, # -> ["great", "big", "strong", "fire", ...]
				'rewritten_prompts': rewritten_prompts # -> ["a Paladin wich...", "a warlock wich...", "a wizard wich..."]
			}
			return result
		except SQL_ALCHEMY_ERROR as e:
			session.rollback()
			raise e
		finally:
			session.close()
	
	def _load_rewritten_prompts(self, idea_id, session):
		"""loads all rewritten prompts with the idea_id i"""
		try:
			stmt = select(RewrittenPrompts.rewritten_prompt).where(RewrittenPrompts.idea_id == idea_id)
			result = session.execute(stmt).all()

			if result:
				return result

			return []
		except SQL_ALCHEMY_ERROR as e:
			session.rollback()
			raise e
	
	def _load_key_description_for_idea(self, idea_id, session):
		"""
		gibt alle descriptions zurück, die eine key-key paarung mit der idea_id haben
		
		from the Table DescriptionToIdea we get the description_id-row
		"""
		descriptions: list[str] = []
		try:
			stmt = select(DescriptionToIdea.description_id).where(DescriptionToIdea.idea_id == idea_id)
			# all description_id´s from the row in DescriptiontoIdea, where idea_id is 'idea_id'
			result = session.execute(stmt).all()
			
			if result:
				for i, description_id in enumerate(result):
					stmt_2 = select(KeyDescription.description).where(KeyDescription.description_id == description_id[0])
					description: str = session.execute(stmt_2).first()
					if description:
						descriptions.append(description)
			return descriptions
		except SQL_ALCHEMY_ERROR as e:
			session.rollback()
			raise e
	
	def _load_classes_for_idea(self, idea_id, session):
		"""gives back all class_names from Table Classes, wich are True"""
		try:
			stmt = select(Classes).where(Classes.idea_id == idea_id)
			result = session.scalars(stmt).first()
			if result:
				class_names = [
					column.name
					for column in Classes.__table__.columns
					if getattr(result, column.name) is True and column.name not in ("class_table_id", "idea_id")
				]
				return class_names
			
			return []
		except SQL_ALCHEMY_ERROR as e:
			session.rollback()
			raise e
	
	# TODO idea_id muss noch gesetzt werden
	def save_generated_characters(self, characters: List[dict], idea_id):
		"speichert die erstellen charactere in der db ab"
		session = self.Session()
		try:
			for character in characters:
				
				# changes the character in a json-
				character = json.dumps(character)
				
				# Debugging output
				DebugHelper.debug_print(data_description="character is a generated character json-string",
				                        data_type=True,
				                        data=character,
				                        store_data=True,
				                        active=True)
				
				# TODO: hier in Character ist irgendwo ein fehler
				character_entry = Character(idea_id, character)
				session.add(character_entry)

			session.commit()
		except SQL_ALCHEMY_ERROR as e:
			session.rollback()
			raise e
		finally:
			session.close()
	
	def delete_character_by_idea_id(self, idea_id: int):
		"""Löscht eine char_idea mit allen colums, die damit verbunden sind"""
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
		except SQL_ALCHEMY_ERROR as e:
			session.rollback()
			raise e
		finally:
			session.close()
		
	def load_characters(self, idea_id: int):
		"""Loads all foru character with the foreign_key: idea_id"""
		session = self.Session()
		try:
			stmt = select(Character).where(Character.idea_id == idea_id)
			result = session.execute(stmt).first()

			if result:
				return result
		except SQL_ALCHEMY_ERROR as e:
			session.rollback()
			raise e
		finally:
			session.close()
			
			
if __name__ == "__main__":
	
	db = DatabaseManager()
	prompts = db.load_character_prompts(1)
	print(prompts)
	