"""
POST API endpoint

gets a user_prompt, wich contains a idea or a description for a DnD-Character.

rewrites the user_promt and saves the rewritten_user_prompt into the database
"""
from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError
import json
from src.database.db_manager import DatabaseManager
from src.llm.rewrite_user_prompt import RewriteUserPrompt


router = APIRouter()

db_mngr = DatabaseManager()


@DebugLog.debug_log
@router.post("/")
async def rewrite_user_prompt(user_prompt: str):
	"""
	takes the user_prompt as input
	gives user_prompt to AnalyseUserPrompt class, wich rewrites user_prompt
	saves rewritten_user_prompt and user_prompt to database
	"""
	try:
		# instanziates RewriteUserPrompt class
		rewrite = RewriteUserPrompt(user_prompt)
		# analyses user_prompt and gives back rewritten_user_prompt
		rewritten_user_prompt = rewrite.rewrite()
		
		rewritten_user_prompt_json = json.loads(rewritten_user_prompt)#
		
	except HTTPException as e:
		if e.status_code == 400:
			raise HTTPException(status_code=400, detail=e)
		
		if e.status_code == 403:
			raise HTTPException(status_code=403, detail=e)
		
		else:
			raise HTTPException(status_code=500, detail=f"Internal Server error: {e}")
	
	except Exception as e:
		raise HTTPException(status_code=500, detail=f"Internal Server error: {e}")
		
	
	# saves data in db
	try:
		db_mngr.save_rewritten_data(user_prompt, rewritten_user_prompt_json)
		
		return f"prompt: {user_prompt} and {rewritten_user_prompt} saved in database"
	
	except (SQLAlchemyError, IntegrityError, OperationalError) as e:
		# rollback is handled in 'save_rewritten_data' method.
		raise HTTPException(status_code=500, detail=f"Error with the database: {e}")
	
	except Exception as e:
		raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
	
	
	
	











