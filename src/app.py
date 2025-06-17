"""

"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api_endpoints.laod_dnd_class_data_enpoint import router as get_router
from src.api_endpoints.rewrite_user_prompt_endpoint import router as post_router
from src.api_endpoints.character_generation_endpoints import router as get_and_post_router
from src.helper.debug_log import DebugLog

app = FastAPI()

app.add_middleware(
    CORSMiddleware,  # ignore IDE error
    allow_origins=["*"],  # allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # allows all HTTP mehtods
    allow_headers=["*"],
)

# registers all endpoints
app.include_router(get_router, prefix="/get_dnd_data_from_DnDapi", tags=["Get Data"])
app.include_router(post_router, prefix="/rewrite_user_prompt", tags=["Analyze Prompt"])
app.include_router(get_and_post_router, prefix="/characters", tags=["Generate Characters"])
