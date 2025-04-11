"""getestet werden soll:
- können daten in die db gespeichert werden?
- kömnnen daten aus der db gelesen werden?
- können objekte aus der db gelöscht werden?
"""

import pytest
from src.database.models import Base, CharIdea, Character, RewrittenPrompts, KeyDescription, DescriptionToIdea, Classes, BestChar
from src.database.db_manager import DatabaseManager
from sqlalchemy import create_engine, select


@pytest.fixture(scope="function")
def db():
	"""Erstellt eine frishe db im lokalen speicher.
	bei jeder neuen test_funktion wird eine neue db erstellt die frisch und sauber ist.
	"""
	engine = create_engine("sqlite:///:memory:")
	Base.metadata.create_all(engine)
	# gibt Database_manager(engine) zurück, ohne die funktion zu beenden
	yield DatabaseManager(engine)
	Base.metadata.drop_all(engine)


def test_save_user_prompt(db):
	prompt = "Ein bote des lichts. Er hat ein großes schwert und beherrscht die elemente. Er ist in eine strahlende Rüstung getaucht."
	analysed_result = {
    "matched_classes": ["paladin", "fighter", "cleric"],
    "keywords": ["Bote des Lichts", "großes Schwert", "Elemente beherrschen", "strahlende Rüstung"],
    "rewritten_prompt_template": [
        "Ein paladin des Lichts. Er hat ein großes Schwert und beherrscht die Elemente. Er ist in eine strahlende Rüstung getaucht.",
        "Ein fighter des Lichts. Er hat ein großes Schwert und beherrscht die Elemente. Er ist in eine strahlende Rüstung getaucht.",
        "Ein cleric des Lichts. Er hat ein großes Schwert und beherrscht die Elemente. Er ist in eine strahlende Rüstung getaucht."
    ]
	}
	
	session = db.Session()
	# daten in db gespeichert
	db.save_user_prompt(prompt, analysed_result)
	
	stmt = select(CharIdea)
	result = session.execute(stmt).all()
	
	assert len(result) == 1

	



