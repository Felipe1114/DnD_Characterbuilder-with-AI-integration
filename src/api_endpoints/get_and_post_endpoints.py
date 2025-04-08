"""
Was muss gemacht werden:
GET:
-   von der datenbank werden alle daten einer char_idea gezogen.
-   dann werden vier charactere erstellt
for 2x class 1 , 1x class 2, 1x class 3:
    character mit keywords: 'keywords' und dem rewritten_prompt: rewritten_prompt[i]


beispiel_daten: {
"matched_classes": ["paladin", "fighter", "cleric"],
"keywords": ["Bote des Lichts", "großes Schwert", "Elemente beherrschen", "strahlende Rüstung"],
"rewritten_prompt_template": [
    "Ein paladin des Lichts. Er hat ein großes Schwert und beherrscht die Elemente. Er ist in eine strahlende Rüstung getaucht.",
    "Ein fighter des Lichts. Er hat ein großes Schwert und beherrscht die Elemente. Er ist in eine strahlende Rüstung getaucht.",
    "Ein cleric des Lichts. Er hat ein großes Schwert und beherrscht die Elemente. Er ist in eine strahlende Rüstung getaucht."
    ]
}


danach:
POST:
-   alle vier erstellen charactere als JSON in die colum 'character' des Tables 'Character' speichern

"""
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