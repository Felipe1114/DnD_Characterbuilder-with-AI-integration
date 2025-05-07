"""
Welche daten kommen in die Datenbank:
- analysed promt sieht so aus:
{
"matched_classes": ["paladin", "fighter", "cleric"],
"keywords": ["Bote des Lichts", "großes Schwert", "Elemente beherrschen", "strahlende Rüstung"],
"rewritten_prompt_template": [
    "Ein paladin des Lichts. Er hat ein großes Schwert und beherrscht die Elemente. Er ist in eine strahlende Rüstung getaucht.",
    "Ein fighter des Lichts. Er hat ein großes Schwert und beherrscht die Elemente. Er ist in eine strahlende Rüstung getaucht.",
    "Ein cleric des Lichts. Er hat ein großes Schwert und beherrscht die Elemente. Er ist in eine strahlende Rüstung getaucht."
  ]
}

was muss gemacht werden:
-   user_prompt muss gespeichert werden
-   matched_classes muss in Table classes eingefügt werden -> paladin, fighter und cleric auf 'true'
-   keywords müssen in Table key_descriptions eingefügt werden und eine colum mit idea_id und description_id angelegt werden.
    Wichtig: abchecken, ob Keyword schon im Table vorhanden ist. Wenn ja, dann nur eine neue colum im Table description_to_idea anlegen.
-   rewritten_user_prompts müssen in Table rewritten_user_prompts eingefügt werden.

genauer ablauf:
1. user gibt prompt ein -> input()
2. llm analysiert prompt -> LLm
	prompt_key = "prompt_alpha_3"
    user_promt = "Ein bote des lichts. Er hat ein großes schwert und beherrscht die elemente. Er ist in eine strahlende Rüstung getaucht."

    rewrite = RewriteUserPromt(user_promt, prompt_key=prompt_key)

    rewritten_promt = rewrite.rewrite() <-- gibt das dict zurück mit den analysierten user-prompt daten
3. user prompt und analysierten prompt speichern

"""
from fastapi import APIRouter
from pydantic import BaseModel # BaseModel is a Class, which defines the input type
from src.database.db_manager import DatabaseManager
from src.LLM.rewrite_user_promt import RewriteUserprompt
from sqlalchemy import create_engine
from src.debug.debug_log import DebugLog


router = APIRouter()

# verkünpfung mit db
db_path = "sqlite:///../../data/db/dnd_db.sqlite"
engine = create_engine(db_path)
db_mngr = DatabaseManager(engine)

class Prompt(BaseModel):
	"""Defines the Input type and validates it"""
	text: str
 
class AnalysedPrompt(BaseModel):
	matched_classes: list
	keywords: list
	rewritten_prompt_template: list

@DebugLog.debug_log
@router.post("/")
async def analyze_prompt(user_prompt: Prompt):
# def analyse_prompt(Prompt(user_prompt).model_dump())
	"""
	nimmt user_prompt entgegen
	gibt user_prompt an LLM.RewriteUserPrompt weiter
	prompt wird analysiert
	anaylsierter user_prompt und user_prompt werden in db gespeichert
	"""
	# instanziert RewriteUserPrompt und erhält bereits user_prompt
	
	rewrite = RewriteUserprompt(user_prompt.text)
	# analysiert user_prompt und gibt analysed_prompt zurück
	analysed_prompt: AnalysedPrompt = rewrite.rewrite()
	
	# speichern der daten in db
	db_mngr.save_user_prompt(user_prompt, analysed_prompt)
	
	return (f"prompt: {user_prompt} wurde in Datenbank gespeichert\n"
	        f"analysed_user_prompt:\n"
	        f"{analysed_prompt}"
	        f"wurde in Datenbank gespeichert")
	
	
	











