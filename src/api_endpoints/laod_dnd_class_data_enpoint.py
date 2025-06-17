"""
GET API-Endpoints

Gets no Input
Loads all necesary DnD data, like all datas for the 12 DnD classes, from the DnD5e-api
"""
from fastapi import APIRouter, HTTPException
from src.dnd_api.dnd_api_manager import DnDApiManager

router = APIRouter()

@router.get("/")
async def get_dnd_data_from_DnDapi():
	"""loads all dnd class_data form the DnD5e-API"""
	try:
		
		manager = DnDApiManager()
		manager.run()
	
	# if a HTTPException is raised, it is diferenced here
	except HTTPException as e:
		if e.status_code == 502:
			raise HTTPException(status_code=502, detail=e)
		
		if e.status_code == 404:
			raise HTTPException(status_code=404, detail=e)

		# for all other HTTPExceptions
		else:
			raise HTTPException(status_code=500, detail="Internal server error!")
	
	# for all other Excpetions
	except Exception as e:
		raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
		
		# 429 to many requests (mit slowapi arbeiten)
