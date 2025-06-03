import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from src.database.db_manager import DatabaseManager
from src.database.models import Base, CharIdea, Classes, RewrittenPrompts, KeyDescription, DescriptionToIdea, Character

TEST_ANALYSED_DICT = {
    "matched_classes": ["paladin", "fighter", "cleric"],
    "keywords": ["Bote des Lichts", "großes Schwert", "Elemente beherrschen", "strahlende Rüstung"],
    "rewritten_prompt_template": [
        "Ein paladin des Lichts. Er hat ein großes Schwert und beherrscht die Elemente. Er ist in eine strahlende Rüstung getaucht.",
        "Ein fighter des Lichts. Er hat ein großes Schwert und beherrscht die Elemente. Er ist in eine strahlende Rüstung getaucht.",
        "Ein cleric des Lichts. Er hat ein großes Schwert und beherrscht die Elemente. Er ist in eine strahlende Rüstung getaucht."
    ]
}

@pytest.fixture(scope="function")
def db():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    yield DatabaseManager(test_case=True, temp_engine=engine)
    Base.metadata.drop_all(engine)

def test_save_char_idea(db):
    prompt = "Ein Testcharakter"
    session = db.Session()
    
    db._save_char_idea(prompt, session)
    
    result = session.query(CharIdea).all()
    session.close()
    assert len(result) == 1 # überprüft, ob auch ein objekt vorhanden ist
    assert result[0].user_prompt == prompt # überpüft, ob die erhaltene antwort auch die eingegebene ist

def test_save_full_analysis(db):
    prompt = "Ein Testcharakter mit Analyse"
    session = db.Session()
    
    db.save_user_prompt(prompt, TEST_ANALYSED_DICT)

    idea_id = session.query(CharIdea.idea_id).first()[0]

    # Check classes
    classes_entry = session.query(Classes).filter_by(idea_id=idea_id).first()
    # was passier thier? müsste s nicht eine for loop geben
    assert classes_entry.paladin
    assert classes_entry.fighter
    assert classes_entry.cleric

    # Check rewritten prompts
    prompts = session.query(RewrittenPrompts).filter_by(idea_id=idea_id).all()
    assert len(prompts) == 3
    assert TEST_ANALYSED_DICT["rewritten_prompt_template"][0] in [p.rewritten_prompt for p in prompts]

    # Check key_descriptions
    key_desc_ids = session.query(DescriptionToIdea.description_id).filter_by(idea_id=idea_id).all()
    assert len(key_desc_ids) == 4
    session.close()

def test_load_all_char_ideas(db):
    prompt = "Char Idee"
    session = db.Session()
    db._save_char_idea(prompt, session)
    session.flush()
    session.close()

    all_ideas = db.load_all_char_ideas()
    assert len(all_ideas) > 0
    assert all_ideas[0][0].user_prompt == prompt

def test_load_character_data(db):
    prompt = "Analyse für Charakterdaten"
    db.save_user_prompt(prompt, TEST_ANALYSED_DICT)
    session = db.Session()
    idea_id = session.query(CharIdea.idea_id).first()[0]
    session.close()

    data = db.load_character_prompts(idea_id)
    assert "classes" in data and "key_descriptions" in data and "rewritten_prompts" in data
    assert "paladin" in data["classes"]
    assert len(data["rewritten_prompts"]) == 3

def test_delete_character_by_idea_id(db):
    prompt = "Charakter zum Löschen"
    db.save_user_prompt(prompt, TEST_ANALYSED_DICT)
    session = db.Session()
    idea_id = session.query(CharIdea.idea_id).first()[0]
    session.close()

    db.delete_character_by_idea_id(idea_id)

    session = db.Session()
    assert session.query(CharIdea).filter_by(idea_id=idea_id).first() is None
    assert session.query(Classes).filter_by(idea_id=idea_id).first() is None
    assert session.query(RewrittenPrompts).filter_by(idea_id=idea_id).first() is None
    session.close()
