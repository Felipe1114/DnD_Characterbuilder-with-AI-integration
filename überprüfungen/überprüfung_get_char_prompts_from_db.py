from src.database.db_manager import DatabaseManager
from src.LLM.system_request_builder import SystemRequestBuilder

# instatiate db
path = "../data/db/dnd_db.sqlite"
db_path = f"sqlite:///{path}"

db = DatabaseManager(db_path)
system_request_builder = SystemRequestBuilder(1)
# get char_prompts
char_prompts = db.load_character_prompts(1)
print(char_prompts)

char_prompt_list = system_request_builder.run()
print(char_prompt_list)
