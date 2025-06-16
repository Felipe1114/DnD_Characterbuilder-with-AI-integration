"""
GET and POST API endpoints

POST:
	Generates a DnD Character on base of a rewritten-user-Prompt and saves it (POST) to the Database

GET:
	Gets a DnD Character from the Database, by its idea_id --> id of the user_prompt
												   ^^^^^^^
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from src.llm.character_builder_app import CharacterBuilderApp
from src.database.db_manager import DatabaseManager
from src.helper.debug_log import DebugLog

router = APIRouter()

class CharacterRequest(BaseModel):
	prompt: str
	class_names: List[str]

@DebugLog.debug_log
@router.get("/get")
async def get_characters(idea_id: int):
	"""gets all characters by idea_id"""
	# checks, if idea_id is an int
	id = str_to_int(idea_id)
	
	db_mngr = DatabaseManager()
	
	character_list = db_mngr.load_characters(id)
	
	return character_list

@DebugLog.debug_log
@router.post("/generate")
async def generate_characters(idea_id: int):
	"""Generates for characters and saves them into the db
	
	idea_id is the primary key for the user_prompt
	the user_prompt is rewritten and the llm had given back a prompt für the generation of a character.
	
	this pormpt is saved in the db.
	
	with the diea_id, we can get the rewritten_prompts from the db
	"""
	# checks, if idea_id is an int
	id = str_to_int(idea_id)
	
	char_builder = CharacterBuilderApp(id)
	char_builder.run()


def str_to_int(id):
	"""converts idea_id in an int, if idea_id is not an int"""
	try:
		if not isinstance(id, int):
			id_as_int = int(id)
			return id_as_int
		
		return id
	
	except ValueError as e:
		print(f"Error: Idea_id has to be an Integer: {e}")