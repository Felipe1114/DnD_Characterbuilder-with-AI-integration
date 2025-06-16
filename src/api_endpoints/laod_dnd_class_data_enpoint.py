"""
GET API-Endpoints

Gets no Input
Loads all necesary DnD data, like all datas for the 12 DnD classes, from the DnD5e-api
"""
from fastapi import APIRouter
from src.dnd_api.dnd_api_manager import DnDApiManager

router = APIRouter()

@router.get("/")
async def get_dnd_data_from_DnDapi():
	"""loads all dnd class_data form the DnD5e-API"""
	manager = DnDApiManager()
	manager.run()
	