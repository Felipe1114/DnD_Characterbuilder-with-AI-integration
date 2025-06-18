"""
GET and POST API endpoints

POST:
	Generates a DnD Character on base of a rewritten-user-Prompt and saves it (POST) to the Database

GET:
	Gets a DnD Character from the Database, by its user_prompt_id --> user_prompt_id of the user_prompt
"""
from fastapi import APIRouter, HTTPException
from src.llm.character_builder_app import CharacterBuilderApp
from src.database.db_manager import DatabaseManager
from src.helper.logger import Logger


router = APIRouter()
db_mngr = DatabaseManager()
logger = Logger("api")

@router.get("/get")
async def get_characters(user_input: int):
	"""gets all characters by user_prompt_id"""
	try:
		logger.info(f"Execute endpoit: /characters/get?user_input={user_input}")
		# validates user_input
		# if not, raise HTTPException with 400 status_code
		user_prompt_id = validate_input(user_input)
		
		# does user_prompt_id exist in db?
		# if not, raise HTTPException with 404 status_code
		user_prompt_id = validate_user_prompt_id(user_prompt_id)
		
		character_list = db_mngr.load_characters(user_prompt_id)
		
		return character_list
	
	except Exception:
		raise HTTPException(status_code=500, detail="Internal server Error")

		# 400 bad request (if input is not an integer -> validate_input einbauen)
		# 404 not found (if user_prompt_id is not in db)
		# 429 to many requests (mit slowapi arbeiten)
		# 500 error for all other cases

	
@router.post("/generate")
async def generate_characters(user_input: int):
	"""Generates for characters and saves them into the db
	
	user_prompt_id is the primary key for the user_prompt
	the user_prompt is rewritten and the llm had given back a prompt für the generation of a character.
	
	this pormpt is saved in the db.
	
	with the diea_id, we can get the rewritten_prompts from the db
	"""
	try:
		# validates user_input
		# if not, raise HTTPException with 400 status_code
		user_prompt_id = validate_input(user_input)
		
		# does user_prompt_id exist in db?
		# if not, raise HTTPException with 404 status_code
		user_prompt_id = validate_user_prompt_id(user_prompt_id)
		
		char_builder = CharacterBuilderApp(user_prompt_id)
		char_builder.run()
	
	except Exception:
		raise HTTPException(status_code=500, detail="Internal server Error")
	



# 400 bad request (if input is not an integer -> validate_input einbauen)
		# 404 not found (if user_prompt_id is not in db)
		# 429 to many requests (mit slowapi arbeiten)
		# 500 error for all other cases

def validate_input(user_input):
	"""validates user_input; if user_input can not be transformed into an int, an error is raised"""
	try:
		logger.debug(f"user_input:{user_input}, is in valdiation process; checked if it is an int, or str.isdecimal(). If str.isdecimal() -> change type str to int")
		logger.info(f"Data type of user_input:{user_input}, is in valdiation process...")
		
		# user_input is int
		if isinstance(user_input, int):
			logger.debug(f"user_input: {user_input} is type 'int'")
			logger.info(f"user_input: {user_input} has valid type")
			
			return user_input
		
		# user_input is str
		elif isinstance(user_input, str):
			logger.debug(f"user_input: {user_input} is type 'str'")

			# user_input is str and decimal; like '4', '2' or '1'
			if user_input.isdecimal():
				# casts str to int
				logger.debug(f"user_input: {user_input} is 'decimal'")
				logger.info(f"user_input: {user_input} has valid type")
				
				return int(user_input)
		
			else:
				logger.warning(f"user_input: {user_input} is type 'str' but not decimal")
				
				raise ValueError("User_input has to be type 'str' and decimal")
		
		# user_input is float
		elif isinstance(user_input, float):
			# casts float to int
			logger.debug(f"user_input: {user_input} is type 'float'")
			logger.info(f"user_input: {user_input} has valid type")

			return int(user_input)
		
		# if user_input is not int, str or float
		else:
			logger.warning(f"user_input: {user_input} is not valid data_type!")
			
			raise TypeError("Wrong Value for User_input")
			
	except (ValueError, TypeError) as e:
		logger.error(f"HTTPException; status_code:400, detail={e}")
		
		raise HTTPException(status_code=400, detail=e)


def validate_user_prompt_id(user_prompt_id):
	"""does user_prompt_id exist in database?"""
	try:
		logger.debug(f"check if given user_prompt_id: {user_prompt_id}, is in database")
		logger.info(f"validate user_prompt_id: {user_prompt_id}")
		
		logger.debug(f"load all user_prompt_ids form database and check, if given user_prompt_id: {user_prompt_id}, is in all id´s")
		all_prompt_ids = db_mngr.load_user_prompt_ids()
		
		# if user_prmopt_id is in id´s from database
		if user_prompt_id in all_prompt_ids:
			logger.info(f"user_prompt_id: {user_prompt_id}, is valid")
			
			return user_prompt_id
		
		else:
			logger.warning(f"user_prompt_id: {user_prompt_id}, is not in database")
			
			raise ValueError("given user_prompt_id does not exist in database")
	
	except ValueError as e:
		logger.error(f"HTTPEsception, status_code?404, detail={e}")
		
		raise HTTPException(status_code=404, detail=e)