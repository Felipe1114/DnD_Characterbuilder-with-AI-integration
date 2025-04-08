"""
was muss hier gemacht werden:
-   alle dnd-class daten werden für alle 12 dnd-classes von der DnD5e-api gezogen.
-   diese daten werden - jeweils - in Json files gespeichert und lokal abgelegt.
"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_data():
    # Placeholder-Funktion, die später durch die Logik zum Abrufen von DnD5e-Daten ersetzt wird
    return {"message": "Daten von DnD5e API werden hier abgerufen."}