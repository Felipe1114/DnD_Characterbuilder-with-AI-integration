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
- `delete_character_by_user_prompt_id()`: Deletes a character idea and all related data
- `load_all_char_ideas()`: Retrieves all character ideas from the database
- `load_characters()`: Loads generated characters for a specific idea

#### Helper Methods:
- `_save_user_prompt()`: Internal method for saving user prompts
- `_save_rewritten_prompts()`: Internal method for saving rewritten prompts
- `_save_key_descriptions()`: Internal method for saving key descriptions
- `_save_classes()`: Internal method for saving class information
- `_load_rewritten_prompts()`: Internal method for loading rewritten prompts
- `_load_key_description_for_user_prompt()`: Internal method for loading descriptions
- `_load_classes_for_user_prompt()`: Internal method for loading class information
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
import logging

from mpmath.libmp import str_to_man_exp
from sqlalchemy import func, select, delete, create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError, PendingRollbackError
from src.database.models import UserPrompt, Character, RewrittenPrompts, KeyDescription, DescriptionToPrompt, Classes, BestChar
from src.handle_data.env_loader import EnvLoader
from src.helper.logger import Logger
from fastapi import HTTPException
from typing import List

logger = Logger("db")

SQL_ALCHEMY_ERROR =(PendingRollbackError, SQLAlchemyError, IntegrityError, OperationalError)

class DatabaseManager:
	"""
	manages the interactions with the database
	"""
	def __init__(self, test_case=False, temp_engine=None):
		# if I want to test the Databasemanager class with a temporary database
		if test_case:
			logger.info(f"initialize DataBaseManager in test_mode")
			
			self.session = sessionmaker(bind=temp_engine)
		
		else:
			logger.info(f"initialize DataBaseManager in normal_mode")

			self.db_path = EnvLoader.db_path()
			logger.debug(f"initialized self.db_path as: {self.db_path}")

			engine = create_engine(self.db_path)
			logger.debug(f"initialized engine as: {engine}")

			self.Session = sessionmaker(bind=engine)
			
			logger.debug(f"initialized DataBaseMangaer as: {__name__}")
		
	def save_rewritten_data(self, prompt: str, analysed_dict):
		"""
		Saves all generated data from the analysing prozess of the user_prompt
		"""
		# extracts the data from the rewrite prozess of the LLM
		logger.info(f"save data from rewrite process of rewriting the user_prompt...")
		
		possible_classes, key_descriptions, rewritten_prompts = self.extract_rewriten_data(analysed_dict)
		logger.debug(f"extracted the rewritten data:\npossible_classes: {possible_classes}\nkey_descriptions: {key_descriptions}\nrewritten_prompts: {rewritten_prompts}")
		
		session = self.Session()
		try:
			# saves user_prompt
			self._save_user_prompt(prompt, session)

			# generates a new 'user_prompt_id'
			stmt_new_idea = select(func.max(UserPrompt.user_prompt_id))
			new_user_prompt_id = session.scalars(stmt_new_idea).first()
			logger.debug(f"created 'new_user_prompt_id' as: {new_user_prompt_id}")

			# saves possible_classes
			self._save_classes(possible_classes, new_user_prompt_id, session)

			# saves key_descriptions
			self._save_key_descriptions(key_descriptions, new_user_prompt_id, session)

			# saves rewritten_user_prompts
			self._save_rewritten_prompts(new_user_prompt_id, rewritten_prompts, session)
			session.commit()
			
		except SQL_ALCHEMY_ERROR as e:
			session.rollback()
			
			logger.critical(f"Error with database; status_code: 500; {e}")
			raise HTTPException(status_code=500, detail=e)
		finally:
			session.close()
	
	def _save_user_prompt(self, prompt: str, session):
		"""Saves user_prompt in db"""
		try:
			logger.info(f"save user_prompt")
			logger.debug(f"save user_prompt as: {prompt}")
			
			user_prompt = UserPrompt(user_prompt=prompt)
			logger.debug(f"add user_prompt: {prompt} to Table 'UserPrompt'")
			
			session.add(user_prompt)
			session.flush()
			
		except SQL_ALCHEMY_ERROR as e:
			session.rollback()
			
			logger.critical(f"Error with _save_user_prompt; status_code: 500; {e}")
			raise HTTPException(status_code=500, detail=e)
	
	def _save_rewritten_prompts(self, new_user_prompt_id, rewritten_prompts, session):
		"""saves the three rewritten user_prompts in db"""
		try:
			logger.info(f"save rewritten prompts")
		
			for i, r_prompt in enumerate(rewritten_prompts):
				logger.debug(f"save rewritten prompt: {r_prompt} from rewritten_prompts: {rewritten_prompts}; prompt nmbr: {i +1 }. of {len(rewritten_prompts)}.")
				
				rewritten_prompt = RewrittenPrompts(user_prompt_id=new_user_prompt_id, rewritten_prompt=r_prompt)
				logger.debug(f"add rewritten_prompt: {rewritten_prompt} to table RewrittenPrompts")
				
				session.add(rewritten_prompt)
				
		except SQL_ALCHEMY_ERROR as e:
			session.rollback()
			
			logger.critical(f"Error with _save_rewritten_prompts; status_code: 500; {e}")
			raise HTTPException(status_code=500, detail=e)
	
	def _save_key_descriptions(self, key_descriptions, user_prompt_id, session:Session):
		"""saves the key_descriptions from user_prompt in db"""
		try:
			logger.info(f"save key descriptions...")
			
			for i, key_description in enumerate(key_descriptions):
				logger.debug(f"save key_description: {key_description} from key_descriptions: {key_descriptions}; key_description nmbr: {i + 1}. of {len(key_descriptions)}.")
				
				logger.info(f"load existing_keydescrpitions")

				stmt_all = select(KeyDescription.description)
				existing_keydescriptions = session.scalars(stmt_all).all()
				logger.debug(f"loades existing_key_descrpitions: {existing_keydescriptions}")
				
				logger.debug(f"check, if key_description: {key_description} is not in existing keydescriptions")
				if not key_description in existing_keydescriptions:
					
					logger.debug(f"key_description: {key_description} is not in existing keydescriptions")
					description = KeyDescription(description=key_description)
					session.add(description)
					logger.debug(f"add key_description to table KeyDescriptions")
					
					session.flush()
					description_id = description.description_id
				
				else:
					logger.debug(f"key_description: {key_description} is in existing keydescriptions")
					
					description_id = (session.scalars(
						select(KeyDescription.description_id)
						.where(KeyDescription.description == key_description))
	                    .first())

				
				description_to_idea = DescriptionToPrompt(user_prompt_id=user_prompt_id, description_id=description_id)
				logger.debug(f"connect description: {description} with user_prompt_id in 'DescriptionToPrompt' table")
				session.add(description_to_idea)
	
		except SQL_ALCHEMY_ERROR as e:
			session.rollback()
			
			logger.critical(f"Error with _save_rewritten_prompts; status_code: 500; {e}")
			raise HTTPException(status_code=500, detail=e)
	
	def _save_classes(self, possible_classes, new_user_prompt_id, session):
		"""saves the three best fitting dnd-classes for user_prompt in db"""
		try:
			logger.info(f"save possible classes; extracted from user_prompt")
			logger.debug(f"save possible classes: {possible_classes};  extracted from user_prompt")
			
			dnd_classes = Classes(user_prompt_id=new_user_prompt_id,
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
			
			logger.critical(f"Error with _save_classes; status_code: 500; {e}")
			raise HTTPException(status_code=500, detail=e)
	
	def extract_rewriten_data(self, analysed_dict) -> tuple:
		"""
		extracts data from the dictionary and returns them as tuples
		"""
		try:
			classes: list[str] = analysed_dict.get("matched_classes", [])
			key_words: list[str] = analysed_dict.get("keywords", [])
			rewritten_prompts: list[str] = analysed_dict.get("rewritten_prompt_template", [])
			
			return classes, key_words, rewritten_prompts
	
		except Exception as e:
			logger.critical(f"Error with extract_rewritten_data; status_code: 500; {e}")
			raise HTTPException(status_code=500, detail=e)
	
	def load_all_char_ideas(self):
		"""loads all char_ideas (user_prompts) and gives them back as key=id and value=idea"""
		logger.info(f"load all user_prompts / char_ideas for character generration from database...")
		
		session = self.Session()
		
		try:
			stmt = select(UserPrompt)
			logger.debug(f"stmt for loading all user_prompts / char_ideas from database: {stmt}")

			result = session.execute(stmt).all()
			
			if not result:
				logger.warning(f"stmt for loading all user_prompts / char_ideas had no effeckt; result is empty!!!")
				return {}

			logger.debug(f"stmt for loading all user_prompts / char_ideas was succesfull; result: {result}")

			return result
		
		except SQL_ALCHEMY_ERROR as e:
			session.rollback()
			
			logger.critical(f"Error with load_all_char_ideas; status_code: 500; {e}")
			raise HTTPException(status_code=500, detail=e)
		
		finally:
			session.close()
	
	def load_character_prompts(self, user_prompt_id):
		"""loads all data form the analysed user_prompt for creating a system prompt for character creation"""
		logger.info(f"loading character prompts...")
		
		session = self.Session()
		try:
			# checks if user_prompt_id is an interger
			if not isinstance(user_prompt_id, int):
				raise ValueError("user_prompt_id hase to be an integer")
			
			classes_for_idea =  self._load_classes_for_user_prompt(user_prompt_id, session)
			
			descriptions_for_idea = self._load_key_description_for_user_prompt(user_prompt_id, session)

			rewritten_prompts = self._load_rewritten_prompts(user_prompt_id, session)
			
			result = {
				'classes': classes_for_idea, # -> three classes [class_1, class_2, class_3]
				'key_descriptions': descriptions_for_idea, # -> ["great", "big", "strong", "fire", ...]
				'rewritten_prompts': rewritten_prompts # -> ["a Paladin wich...", "a warlock wich...", "a wizard wich..."]
			}
			
			logger.debug(f"loading character prompt from user_prompt_id was succesfull; result: {result}")
			return result
		
		except SQL_ALCHEMY_ERROR as e:
			session.rollback()
			
			logger.critical(f"Error with load_character_prompts; status_code: 500; {e}")
			raise HTTPException(status_code=500, detail=e)
		
		except ValueError as e:
			session.rollback()
		
			logger.critical(f"Error with load_character_prompts: user_prompt_id has to be an integer!; status_code: 500; {e}")
			raise HTTPException(status_code=500, detail=e)

		finally:
			session.close()
	
	def _load_rewritten_prompts(self, user_prompt_id, session):
		"""loads all rewritten prompts with the user_prompt_id i"""
		try:
			logger.info(f"load rewritten prompts from database...")
			stmt = select(RewrittenPrompts.rewritten_prompt).where(RewrittenPrompts.user_prompt_id == user_prompt_id)
			logger.debug(f"stmt for loading rewritten prompts from database: {stmt}")
			
			result = session.execute(stmt).all()
			
			if not result:
				logger.warning(f"database request was not succesfull")
				raise HTTPException(status_code=500, detail=f"rewritten prompts could not loaded from database")
				
				
			logger.info(f"database request was successfull")
			logger.debug(f"result from database request: {result}")
			
			return result
		
		except SQL_ALCHEMY_ERROR as e:
			session.rollback()
			logger.warning(f"Error with database: {e}")
		
			raise HTTPException(status_code=500, detail=e)
		
		except  HTTPException as e:
			session.rollback()
			raise HTTPException(status_code=500, detail=e)
	
	def _load_key_description_for_user_prompt(self, user_prompt_id, session):
		"""
		returns descriptions wich have a key-key connection with the given user_prompt_id
		
		from the Table DescriptionToIdea we get the description_id-row,
		wich contains all key-key pairs for descriptions and user_prompt_ids
		"""
		logger.info(f"lod key descriptions for user_prompt")
		
		descriptions: list[str] = []
		try:
			stmt = select(DescriptionToPrompt.description_id).where(DescriptionToPrompt.user_prompt_id == user_prompt_id)
			logger.debug(f"stmt for loading key descriptions for user prompt from database: {stmt}")
			
			# all description_id´s from the row in DescriptiontoIdea, where user_prompt:id is 'user_prompt_id'
			result = session.execute(stmt).all()
			
			if not result:
				logger.warning("databease request to Table: DescriptionToPrompt failed")
				
				raise HTTPException(status_code=500, detail=f"databease request to Table: DescriptionToPrompt failed")
	
			elif result:
				logger.info(f"database request for load key descriptions for user prompt was succesfull")
			
				for i, description_id in enumerate(result):
					logger.info(f"extracting descriptions from result from database")
					
					stmt_2 = select(KeyDescription.description).where(KeyDescription.description_id == description_id[0])
					description: str = session.execute(stmt_2).first()
					logger.debug(f"extracting description: {description} from result; description nmbr: {i +1}. of {len(result)}.")

					if description:
						descriptions.append(description)
				
			logger.info(f"loading of key descriptions for user prompt, was succesfull")
		
		except SQL_ALCHEMY_ERROR as e:
			session.rollback()
			raise HTTPException(status_code=500, detail=e)
	
		except HTTPException as e:
			session.rollback()
			raise HTTPException(status_code=500, detail=e)
			
	def _load_classes_for_user_prompt(self, user_prompt_id, session):
		"""gives back all class_names from Table Classes, wich are True"""
		try:
			logger.info(f"load classes for user_prompt")
			
			stmt = select(Classes).where(Classes.user_prompt_id == user_prompt_id)
			logger.debug(f"stmt for loading prozess: {stmt}")
			
			result = session.scalars(stmt).first()
			
			if not result:
				logger.warning(f"could not load classes for user_prompt from database")
			
				raise HTTPException(status_code=500, detail=f"could not load classes for user_prompt from database")
				
			elif result:
				logger.info(f"Loding prozess form classes for user_prompt was succesfull")
				
				classes = [
					column.name
					for column in Classes.__table__.columns
					if getattr(result, column.name) is True and column.name not in ("class_table_id", "user_prompt_id")
				]
				logger.debug(f"loades classes are: {classes}")
				
				return classes
			
		except SQL_ALCHEMY_ERROR as e:
			session.rollback()
			raise HTTPException(status_code=500, detail=e)
		
		except HTTPException as e:
			session.rollback()
			raise HTTPException(status_code=500, detail=e)

	
	def save_generated_characters(self, characters: List[str], user_prompt_id):
		"saves generated characters in db"
		logger.info(f"save generated characters")
		logger.debug(f"user_prompt_id: {user_prompt_id}; characters for saving: {characters}")
		
		session = self.Session()
		try:
			for i, character in enumerate(characters):
				character_entry = Character(user_prompt_id=user_prompt_id, character=character)
				session.add(character_entry)
				
				logger.debug(f"saving character: {character}; character nmbr: {i + 1}. of {len(characters)}.")

			session.commit()
			
		except SQL_ALCHEMY_ERROR as e:
			logger.error(f"could not save cahracters in database: {e}")
			
			session.rollback()
			raise HTTPException(status_code=500, detail=f"could not save cahracters in database: {e}")
		
		finally:
			session.close()
	
	def delete_character_by_user_prompt_id(self, user_prompt_id: int):
		"""delets a user_prompt_id (user_prompt) with all connected colums"""
		logger.info(f"deleting character by user_prompt_id")
		logger.debug(f"deleting character with user_prompt_id: {user_prompt_id}")

		session = self.Session()
		try:
			# list of all models, which containing the user_prompt_id as foregin_key
			models = [UserPrompt, DescriptionToPrompt, RewrittenPrompts, Classes, Character, BestChar]

			# looping thrue all models
			for i, model in enumerate(models):
				logger.debug(f"deleting character connection in table: {model}; table nmbr: {i +1}. of {len(models)}.")
				
				# deleting all colums with the user_prompt_id == user_prompt_id
				stmt = delete(model).where(model.user_prompt_id == user_prompt_id)
				logger.debug(f"stm for deleting {model}: {stmt}")

				session.execute(stmt)

			session.commit()
			
		except SQL_ALCHEMY_ERROR as e:
			logger.error(f"failed deleting character with user_prompt_id: {user_prompt_id}: {e}")
			
			session.rollback()
			raise HTTPException(status_code=500, detail=f"failed deleting character with user_prompt_id: {user_prompt_id}: {e}")
		
		finally:
			session.close()
		
	def load_characters(self, user_prompt_id: int):
		"""Loads all four character with the foreign_key: user_prompt_id"""
		logger.info(f"loading character...")
		logger.debug(f"loading character with user_prompt_id: {user_prompt_id}")
		
		session = self.Session()
		
		try:
			stmt = select(Character).where(Character.user_prompt_id == user_prompt_id)
			logger.debug(f"stmt for loading character: {stmt}")
			results = session.execute(stmt).all()
			
			if results:
				logger.info(f"loading prozess was succesfull")
				# results is type: Row. Row is not JSON serializable, so it is transformed in a Tuple
				results = [tuple(row) for row in results]
				logger.debug(f"loading prozess was succesfull; results: {results}")
				
				return results
			
			if not results:
				raise HTTPException(status_code=500, detail=f"failed loading character from database, with user_prompt_id: {user_prompt_id}")
	
		except SQL_ALCHEMY_ERROR as e:
			logger.error(f"failed loading character from database, with user_prompt_id: {user_prompt_id}: {e}")
			
			session.rollback()
			raise HTTPException(status_code=500, detail=f"failed loading character from database, with user_prompt_id: {user_prompt_id}: {e}")
		
		except HTTPException as e:
			logger.error(f"failed loading character from database, with user_prompt_id: {user_prompt_id}: {e}")

			session.rollback()
			raise HTTPException(status_code=500, detail=e)
	
		finally:
			session.close()
			
	def load_user_prompt_ids(self):
		"""loads all user_prompt_id´s form the database"""
		logger.info(f"loading all user prompt id´s")
		
		session = self.Session()
		
		try:
			stmt = select(UserPrompt.user_prompt_id)
			result = session.execute(stmt).all()
			
			if result:
				# returns a list of user_prompt_id´s
				return [i for i in result]
		
			if not result:
				raise HTTPException(status_code=500, detail=f"failed loading user_prompt_id´s")
				
		except SQL_ALCHEMY_ERROR as e:
			logger.error(f"failed loading user_prompt_id´s: {e}")

			session.rollback()
			raise HTTPException(status_code=500, detail=f"failed loading user_prompt_id´s: {e}")
	
		except HTTPException as e:
			logger.error(f"failed loading user_prompt_id´s: {e}")
			
			session.rollback()
			raise HTTPException(status_code=500, detail=e)
	
		finally:
			session.close()
