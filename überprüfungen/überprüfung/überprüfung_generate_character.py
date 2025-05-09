"""
prüft den characterbuilder prozess in prozeduralem code
"""
from src.LLM.system_request_builder import SystemRequestBuilder
from src.LLM.talk_to_mistral import TalkToMistral
from src.database.db_manager import DatabaseManager
from json import loads

path = "../../data/db/dnd_db.sqlite"
db_path = f"sqlite:///{path}"

db = DatabaseManager(db_path)
prompts = db.load_character_prompts(1)

print(prompts)

