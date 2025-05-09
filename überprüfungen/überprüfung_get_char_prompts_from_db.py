from src.database.db_manager import DatabaseManager

# instatiate db
path = "../data/db/dnd_db.sqlite"
db_path = f"sqlite:///{path}"

db = DatabaseManager(db_path)

# get char_prompts
char_prompts = db.load_character_prompts(1)

print(char_prompts)
