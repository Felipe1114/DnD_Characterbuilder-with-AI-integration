"""
POST API endpoint

gets a user_prompt, wich contains a idea or a description for a DnD-Character.

rewrites the user_promt and saves the rewritten_user_prompt into the database
"""
from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError
import json
import re

from yaql.cli.cli_functions import load_data

from src.database.db_manager import DatabaseManager
from src.llm.rewrite_user_prompt import RewriteUserPrompt
from src.helper.logger import Logger

logger = Logger("api")

router = APIRouter()

db_mngr = DatabaseManager()

@router.post("/")
async def rewrite_user_prompt(user_prompt: str):
	"""
	takes the user_prompt as input
	gives user_prompt to AnalyseUserPrompt class, wich rewrites user_prompt
	saves rewritten_user_prompt and user_prompt to database
	"""
	try:
		logger.debug(f"execute api endpoint 'rewrite user prompt")
		logger.info(f"start rewriting user prompt...")
		# instanziates RewriteUserPrompt class
		rewrite = RewriteUserPrompt(user_prompt)
		# analyses user_prompt and gives back rewritten_user_prompt
		
		rewritten_user_prompt = rewrite.rewrite()
		logger.debug(f"rewritten_user_prompt(type:{type(rewritten_user_prompt)} is: {rewritten_user_prompt}")
		
		rewritten_user_prompt = check_json_struk(txt=rewritten_user_prompt)
		
		logger.debug(f"start changing 'rewritten_user_prompt' to json.loads()...")
		rewritten_user_prompt_json = json.loads(str(rewritten_user_prompt))
		logger.debug(f"changed 'rewritten_user_prompt' to json.loads()...")

	
	# saves data in db
		logger.info(f"save rewritten data into database...")
		db_mngr.save_rewritten_data(user_prompt, rewritten_user_prompt_json)
		logger.info(f"saving rewritten data was sucessfull...")
	
	except HTTPException as e:
		if e.status_code == 400:
			logger.error(f"Error with statuscode: 400: {e}")
			raise HTTPException(status_code=400, detail=e)
		
		if e.status_code == 403:
			logger.error(f"Error with statuscode: 403: {e}")
			raise HTTPException(status_code=403, detail=e)
		
		else:
			logger.error(f"Error with statuscode: 500: {e}")
			raise HTTPException(status_code=500, detail=f"Internal Server error: {e}")
	
	except (SQLAlchemyError, IntegrityError, OperationalError) as e:
		# rollback is handled in 'save_rewritten_data' method.
		logger.error(f"Error with database; statuscode: 500: {e}")
		raise HTTPException(status_code=500, detail=f"Error with the database: {e}")
	
	except Exception as e:
		logger.error(f"Error with statuscode: 500: {e}")
		raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
	
	
def check_json_struk(txt:str):
	"""checks, if txt is a json like string; if ```json is in front of txt, or ``` is at the end of txt, it will be removed"""
	# Check if the text starts with ```json and ends with ```
	logger.info(f"check, if rewritten_user_prompt has markdown format in it...")
	
	if re.match(r'^\s*```json\s*', txt, flags=re.IGNORECASE | re.DOTALL) and txt.rstrip().endswith('```'):
		logger.info(f"rewritten_user_prompt has markdown formats, removing them...")
		
		logger.debug(f"remove ```json from rewritten_user_prompt")
		# Remove ```json from the beginning
		txt = re.sub(r'^\s*```json\s*', '', txt, flags=re.IGNORECASE | re.DOTALL)
		
		logger.debug(f"remove ``` from rewritten_user_prompt")
		# Remove ``` from the end
		txt = re.sub(r'\s*```\s*$', '', txt)
		
		logger.info(f"return clean rewritten_user_prompt")
		return txt.strip()
	
	logger.info(f"rewritten_user_prompt is clean")
	return txt











