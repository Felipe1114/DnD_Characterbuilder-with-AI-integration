"""
POST API endpoint

gets a user_prompt, wich contains a idea or a description for a DnD-Character.

rewrites the user_promt and saves the rewritten_user_prompt into the database
"""
from fastapi import APIRouter
from src.database.db_manager import DatabaseManager
from src.llm.rewrite_user_prompt import RewriteUserPrompt
from src.helper.debug_log import DebugLog
import json
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError


router = APIRouter()

db_mngr = DatabaseManager()


@DebugLog.debug_log
@router.post("/")
async def write_character_idea_for_analysing(user_prompt: str):
	"""
	takes the user_prompt as input
	gives user_prompt to AnalyseUserPrompt class, wich rewrites user_prompt
	saves rewritten_user_prompt and user_prompt to database
	"""
	
	# instanziates RewriteUserPrompt class
	rewrite = RewriteUserPrompt(user_prompt)
	# analyses user_prompt and gives back rewritten_user_prompt
	rewritten_user_prompt = rewrite.rewrite()
	
	rewritten_user_prompt_json = json.loads(rewritten_user_prompt)
	
	# saves data in db
	try:
		db_mngr.save_rewritten_data(user_prompt, rewritten_user_prompt_json)
	except (SQLAlchemyError, IntegrityError, OperationalError) as e:
		# rollback is handled in 'save_rewritten_data' method.
		print(f"DB Error: {str(e)}")
		raise e
	
	return f"prompt: {user_prompt} and {rewritten_user_prompt} saved in database"
	
	











