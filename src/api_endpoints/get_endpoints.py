"""
was muss hier gemacht werden:
-   alle dnd-class daten werden für alle 12 dnd-classes von der DnD5e-api gezogen.
-   diese daten werden - jeweils - in Json files gespeichert und lokal abgelegt.
"""
from fastapi import APIRouter
from src.dnd_api.dnd_api_manager import DnDApiManager

router = APIRouter()

@router.get("/")
async def get_dnd_data_from_DnDapi():
	manager = DnDApiManager()
	manager.run()
	