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

router = APIRouter()
db_mngr = DatabaseManager()


@router.get("/get")
async def get_characters(user_input: int):
	"""gets all characters by user_prompt_id"""
	try:
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
		# user_input is int
		if isinstance(user_input, int):
			return user_input
		
		# user_input is str
		elif isinstance(user_input, str):
			
			# user_input is str and decimal; like '4', '2' or '1'
			if user_input.isdecimal():
				# casts str to int
				return int(user_input)
			else:
				raise ValueError("User_input has to be decimal")
		
		# user_input is float
		elif isinstance(user_input, float):
			# casts float to int
			return int(user_input)
		
		# if user_input is not int, str or float
		else:
			raise TypeError("Wrong Value for User_input")
	
	except (ValueError, TypeError) as e:
		raise HTTPException(status_code=400, detail=e)


def validate_user_prompt_id(user_prompt_id):
	"""does user_prompt_id exist in database?"""
	try:
		all_prompt_ids = db_mngr.load_user_prompt_ids()
		
		# if user_prmopt_id is in id´s from database
		if user_prompt_id in all_prompt_ids:
			return user_prompt_id
		else:
			raise ValueError("given user_prompt_id does not exist in database")
	
	except ValueError as e:
		raise HTTPException(status_code=404, detail=e)