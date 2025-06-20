"""
GET API-Endpoints

Gets no Input
Loads all necesary DnD data, like all datas for the 12 DnD classes, from the DnD5e-api
"""
from fastapi import APIRouter, HTTPException
from src.dnd_api.dnd_api_manager import DnDApiManager
from src.helper.logger import Logger

router = APIRouter()
logger = Logger("api")

@router.get("/")
async def get_dnd_data_from_DnDapi():
	"""loads all dnd class_data form the DnD5e-API"""
	try:
		logger.debug(f"Execute endpoit: /get_dnd_data_from_DnDapi/")
		logger.info(f"Data from dnd5e-api starts to load")
		
		manager = DnDApiManager()
		manager.run()
	
	# if a HTTPException is raised, it is diferenced here
	except HTTPException as e:
		if e.status_code == 502:
			logger.error(f"Error: status_code 502: {e}")
			
			raise HTTPException(status_code=502, detail=e)
		
		if e.status_code == 404:
			logger.error(f"Error: status_code 404: {e}")

			raise HTTPException(status_code=404, detail=e)

		# for all other HTTPExceptions
		else:
			logger.error(f"Error: status_code 500: {e}")
			
			raise HTTPException(status_code=500, detail="Internal server error!")
	
	# for all other Excpetions
	except Exception as e:
		logger.error(f"Error: status_code 500: {e}")
		
		raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
		
		# 429 to many requests (mit slowapi arbeiten)
