from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_data():
    # Placeholder-Funktion, die später durch die Logik zum Abrufen von DnD5e-Daten ersetzt wird
    return {"message": "Daten von DnD5e API werden hier abgerufen."}