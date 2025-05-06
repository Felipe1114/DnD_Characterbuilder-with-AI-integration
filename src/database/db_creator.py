from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database.models import Base

# Erstelle eine SQLite-Datenbank im angegebenen Pfad
DATABASE_URL = "sqlite:///../../data/db/dnd_db.sqlite"

if __name__ == "__main__":
	
	engine = create_engine(DATABASE_URL)
	
	# Erstelle alle Tabellen in der Datenbank
	Base.metadata.create_all(engine)
	
	# Optional: Erstelle eine Sitzung, um mit der Datenbank zu interagieren
	Session = sessionmaker(bind=engine)
	session = Session()
	
	# Beispiel: Füge einen Eintrag hinzu (optional)
	# new_idea = CharIdea(user_prompt="Create a powerful sorcerer")
	# session.add(new_idea)
	# session.commit()
	
	print("Datenbank und Tabellen wurden erfolgreich erstellt.")
