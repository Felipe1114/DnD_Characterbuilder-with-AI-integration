"""
Was muss gemacht werden:
GET:
-   von der datenbank werden alle daten einer char_idea gezogen.
-   dann werden vier charactere erstellt
for 2x class 1 , 1x class 2, 1x class 3:
    character mit keywords: 'keywords' und dem rewritten_prompt: rewritten_prompt[i]


beispiel_daten: {
"matched_classes": ["paladin", "fighter", "cleric"],
"keywords": ["Bote des Lichts", "großes Schwert", "Elemente beherrschen", "strahlende Rüstung"],
"rewritten_prompt_template": [
    "Ein paladin des Lichts. Er hat ein großes Schwert und beherrscht die Elemente. Er ist in eine strahlende Rüstung getaucht.",
    "Ein fighter des Lichts. Er hat ein großes Schwert und beherrscht die Elemente. Er ist in eine strahlende Rüstung getaucht.",
    "Ein cleric des Lichts. Er hat ein großes Schwert und beherrscht die Elemente. Er ist in eine strahlende Rüstung getaucht."
    ]
}


danach:
POST:
-   alle vier erstellen charactere als JSON in die colum 'character' des Tables 'Character' speichern

"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from src.LLM.character_builder_app import CharacterBuilderApp
from src.database.db_manager import DatabaseManager
from src.debug.debug_log import DebugLog

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
	
	db_mngr.load_characters(id)

@DebugLog.debug_log
@router.post("/generate")
async def generate_characters(idea_id: int):
	"""Generates for characters and saves them into the db
	
	idea_id is the primary key for the user_prompt
	the user_prompt is analysed and the LLM had given back a prompt für the generation of a character.
	
	this pormpt is saved in the db.
	
	with the diea_id, we can get the analysed_prompt from the db
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