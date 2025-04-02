# endpoints/analyze_prompt.py
from fastapi import APIRouter
from pydantic import BaseModel # BaseModel is a Class, which defines the input type

router = APIRouter()


class Prompt(BaseModel):
    """Defines the Input type and validates it"""
    text: str

@router.post("/")
async def analyze_prompt(prompt: Prompt):
    # Placeholder-Funktion, die später durch die Analyse-Logik ersetzt wird
    return {"message": f"Analysiere den Text: {prompt.text}"}