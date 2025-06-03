"""
main datei, die die API endpunkte aufruf, die die jeweiligen Programm funktionen ausführen.
hat folgende Endpunkte:
    Daten von DnD5e API laden(GET)
         alle Klassen daten werden von der DnD5e API gezogen

    analyse user promt(POST)
        promt wird analysiert

        analysierte daten werden in datenbank abgespeichert

        pro user promt gibt drei request-promts zurück.

        bsp: request promt:'dunkler {Klassen_name} der tote beschwören kann und feuer Magie nutzt'
        Klassen_namen : ['wizard', ‘sorcerer’, ‘celric’]

    generate Charcters(GET, POST)
        analysierte request-promts werden geladen und mit lokalen daten (Klassen daten von DnD5e API) an LLM gegeben.

        Aus den daten werden dann vier Charactere erstellt und als Json zurück gegeben.

        erstelle Charactere werden in Datenbank gespeichert
"""
from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware import _MiddlewareFactory
from src.api_endpoints.get_endpoints import router as get_router
from src.api_endpoints.post_endpoints import router as post_router
from src.api_endpoints.get_and_post_endpoints import router as get_and_post_router
from src.debug.debug_log import DebugLog

app = FastAPI()

app.add_middleware(     # type: ignore
    CORSMiddleware,
    allow_origins=["*"],  # Erlaubt alle Ursprünge
    allow_credentials=True,
    allow_methods=["*"],  # Erlaubt alle HTTP-Methoden
    allow_headers=["*"],
)

# Hier registrieren wir die Endpunkte
app.include_router(get_router, prefix="/get_dnd_data_from_DnDapi", tags=["Get Data"])
app.include_router(post_router, prefix="/write_character_idea_for_analysing", tags=["Analyze Prompt"])
app.include_router(get_and_post_router, prefix="/characters", tags=["Generate Characters"])
