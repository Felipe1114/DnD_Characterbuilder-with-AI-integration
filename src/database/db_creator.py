"""
Only for use, if a new database should be created.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database.models import Base
from src.handle_data.env_loader import EnvLoader

# !!! If you have a existing database, be shure, in your .env file, you´ve created a new database_file_path;
# !!! If not, your new database may overwrite your existing database

# gets the database_file_path for the new database
DATABASE_URL = EnvLoader.db_path()

if __name__ == "__main__":
	
	engine = create_engine(DATABASE_URL)
	
	Base.metadata.create_all(engine)
	
	Session = sessionmaker(bind=engine)
	session = Session()
	
	print("Database was sucesfully created.")
