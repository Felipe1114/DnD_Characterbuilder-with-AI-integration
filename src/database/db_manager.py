"""
# DatabaseManager Class Overview

This module provides the `DatabaseManager` class, which manages interactions with a SQL database
for a character creation system. The class handles saving, loading, and deleting data related to
user prompts, character ideas, classes, descriptions, and generated characters.

## Key Features

- **Database Connection Management**: Handles both production and test database connections
- **Data Persistence**: Saves and retrieves character ideas, rewritten prompts, key descriptions, and classes
- **Character Management**: Stores and retrieves generated character data
- **Data Deletion**: Provides functionality to delete character ideas and related data
- **Error Handling**: Comprehensive error handling for database operations

## Main Components

### Class: DatabaseManager

#### Core Methods:
- `save_rewritten_data()`: Saves analyzed prompt data including classes, descriptions, and rewritten prompts
- `load_character_prompts()`: Retrieves all data needed for character creation based on an idea ID
- `save_generated_characters()`: Stores generated character data in the database
- `delete_character_by_idea_id()`: Deletes a character idea and all related data
- `load_all_char_ideas()`: Retrieves all character ideas from the database
- `load_characters()`: Loads generated characters for a specific idea

#### Helper Methods:
- `_save_user_prompt()`: Internal method for saving user prompts
- `_save_rewritten_prompts()`: Internal method for saving rewritten prompts
- `_save_key_descriptions()`: Internal method for saving key descriptions
- `_save_classes()`: Internal method for saving class information
- `_load_rewritten_prompts()`: Internal method for loading rewritten prompts
- `_load_key_description_for_idea()`: Internal method for loading descriptions
- `_load_classes_for_idea()`: Internal method for loading class information
- `extract_rewriten_data()`: Extracts data from analysis dictionary

## Database Models Used

The class interacts with several database models:
- CharIdea: Stores user prompts
- Character: Stores generated characters
- RewrittenPrompts: Stores rewritten versions of user prompts
- KeyDescription: Stores key descriptions extracted from prompts
- DescriptionToIdea: Maps descriptions to character ideas
- Classes: Stores class information for character ideas
- BestChar: Stores information about best characters

## Error Handling

The class implements comprehensive error handling for database operations,
including rollback mechanisms for failed transactions and proper session management.
"""

from sqlalchemy import func, select, delete, create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError, PendingRollbackError
from src.database.models import UserPrompt, Character, RewrittenPrompts, KeyDescription, DescriptionToPrompt, Classes, BestChar
from typing import List
from src.handle_data.env_loader import EnvLoader
from src.helper.debug_helper import DebugHelper

SQL_ALCHEMY_ERROR =(PendingRollbackError, SQLAlchemyError, IntegrityError, OperationalError)

# sets the DebugHelper on or off
DebugHelper.activ(activ=True)

class DatabaseManager:
	"""
	manages the interactions with the database
	"""
	def __init__(self, test_case=False, temp_engine=None):
		# if I want to test the Databasemanager class with a temporary database
		if test_case:
			self.session = sessionmaker(bind=temp_engine)
		
		else:
			self.db_path = EnvLoader.db_path()
			engine = create_engine(self.db_path)
			self.Session = sessionmaker(bind=engine)
			
	def save_rewritten_data(self, prompt: str, analysed_dict):
		"""
		Saves all generated data from the analysing prozess of the user_prompt
		"""
		# extracts the data from the rewrite prozess of the LLM
		possible_classes, key_descriptions, rewritten_prompts = self.extract_rewriten_data(analysed_dict)

		session = self.Session()
		try:
			# saves user_prompt
			self._save_user_prompt(prompt, session)

			# generates a new 'idea_id'
			stmt_new_idea = select(func.max(UserPrompt.idea_id))
			new_idea_id = session.scalars(stmt_new_idea).first()

			# saves possible_classes
			self._save_classes(possible_classes, new_idea_id, session)

			# saves key_descriptions
			self._save_key_descriptions(key_descriptions, new_idea_id, session)

			# saves rewritten_user_prompts
			self._save_rewritten_prompts(new_idea_id, rewritten_prompts, session)
			session.commit()
			
		except SQL_ALCHEMY_ERROR as e:
			session.rollback()
			raise e
		finally:
			session.close()
	
	def _save_user_prompt(self, prompt: str, session):
		"""Saves user_prompt in db"""
		try:
			char_idea = UserPrompt(user_prompt=prompt)
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

				description_to_idea = DescriptionToPrompt(idea_id=new_idea_id, description_id=description_id)
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
	
	def extract_rewriten_data(self, analysed_dict) -> tuple:
		"""
		extracts data from the dictionary and returns them as tuples
		"""
		classes: list[str] = analysed_dict["matched_classes"]
		key_words: list[str] = analysed_dict["keywords"]
		rewritten_prompts: list[str] = analysed_dict["rewritten_prompt_template"]
		return classes, key_words, rewritten_prompts
	
	def load_all_char_ideas(self):
		"""loads all char_ideas (user_prompts) and gives them back as key=id and value=idea"""
		session = self.Session()
		try:
			stmt = select(UserPrompt)
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
		returns descriptions wich have a key-key connection with the given idea_id
		
		from the Table DescriptionToIdea we get the description_id-row,
		wich contains all key-key pairs for descriptions and idea_ids
		"""
		descriptions: list[str] = []
		try:
			stmt = select(DescriptionToPrompt.description_id).where(DescriptionToPrompt.idea_id == idea_id)
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
	
	def save_generated_characters(self, characters: List[str], idea_id):
		"saves generated characters in db"
		session = self.Session()
		try:
			for character in characters:
				# Debugging output
				DebugHelper.debug_print(data_description="character is a generated character json-string",
				                        data_type=True,
				                        data=character,
				                        store_data=True,
				                        active=True)
				
				character_entry = Character(idea_id=idea_id, character=character)
				session.add(character_entry)

			session.commit()
		except SQL_ALCHEMY_ERROR as e:
			session.rollback()
			raise e
		finally:
			session.close()
	
	def delete_character_by_idea_id(self, idea_id: int):
		"""delets a idea_id (user_prompt) with all connected colums"""
		session = self.Session()
		try:
			# list of all models, which containing the idea_id as foregin_key
			models = [UserPrompt, DescriptionToPrompt, RewrittenPrompts, Classes, Character, BestChar]

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
		"""Loads all four character with the foreign_key: idea_id"""
		session = self.Session()
		try:
			stmt = select(Character).where(Character.idea_id == idea_id)
			results = session.execute(stmt).all()
			
			DebugHelper.debug_print(active=False, data_description="List of characters, loaded from Database:", data=results, data_type=True, store_data=False)
			
			if results:
				# results is type: Row. Row is not JSON serializable, so it is transformed in a Tuple
				results = [tuple(row) for row in results]
		
				return results
		except SQL_ALCHEMY_ERROR as e:
			session.rollback()
			raise e
		finally:
			session.close()
			
	def load_user_prompt_ids(self):
		"""loads all user_prompt_id´s form the database"""
		session = self.Session()
		
		try:
			stmt = select(UserPrompt.user_prompt_id)
			result = session.execute(stmt).all()
			
			if result:
				# returns a list of user_prompt_id´s
				return [i for i in result]
		
		except SQL_ALCHEMY_ERROR as e:
			session.rollback()
			raise e
		finally:
			session.close()
			
if __name__ == "__main__":
	
	db = DatabaseManager()
	prompts = db.load_character_prompts(1)
	print(prompts)
	