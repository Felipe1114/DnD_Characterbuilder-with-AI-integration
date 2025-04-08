"""
Welche daten kommen in die Datenbank:
- analysed promt sieht so aus:
{
"matched_classes": ["paladin", "fighter", "cleric"],
"keywords": ["Bote des Lichts", "großes Schwert", "Elemente beherrschen", "strahlende Rüstung"],
"rewritten_prompt_template": [
    "Ein paladin des Lichts. Er hat ein großes Schwert und beherrscht die Elemente. Er ist in eine strahlende Rüstung getaucht.",
    "Ein fighter des Lichts. Er hat ein großes Schwert und beherrscht die Elemente. Er ist in eine strahlende Rüstung getaucht.",
    "Ein cleric des Lichts. Er hat ein großes Schwert und beherrscht die Elemente. Er ist in eine strahlende Rüstung getaucht."
  ]
}

was muss gemacht werden:
-   matched_classes muss in Table classes eingefügt werden -> paladin, fighter und cleric auf 'true'
-   keywords müssen in Table key_descriptions eingefügt werden und eine colum mit idea_id und description_id angelegt werden.
    Wichtig: abchecken, ob Keyword schon im Table vorhanden ist. Wenn ja, dann nur eine neue colum im Table description_to_idea anlegen.
-   rewritten_user_prompts müssen in Table rewritten_user_prompts eingefügt werden.

"""
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