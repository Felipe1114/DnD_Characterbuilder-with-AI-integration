from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class CharacterRequest(BaseModel):
    prompt: str
    class_names: List[str]

@router.get("/")
async def get_characters():
    # Placeholder-Funktion für GET-Anfragen (Zugriff auf generierte Charaktere)
    return {"message": "Hier werden die generierten Charaktere abgerufen."}

@router.post("/")
async def generate_characters(request: CharacterRequest):
    # Placeholder-Funktion für POST-Anfragen (Generierung von Charakteren)
    return {"message": f"Charaktere basierend auf dem Prompt: {request.prompt}"}