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
from sqlalchemy import create_engine


router = APIRouter()

class CharacterRequest(BaseModel):
    prompt: str
    class_names: List[str]

@DebugLog.debug_log
@router.get("/")
async def get_characters(idea_id: int):
    """gets all characters by idea_id"""
    db_path = "sqlite:///../../data/db/dnd_db.sqlite"
    engine = create_engine(db_path)
    db_mngr = DatabaseManager(engine)
    
    db_mngr.load_characters(idea_id)

@DebugLog.debug_log
@router.post("/generate")
async def generate_characters(idea_id: int):
   """Generates for characters and saves them into the db"""
   char_builder = CharacterBuilderApp(idea_id)
   char_builder.run()