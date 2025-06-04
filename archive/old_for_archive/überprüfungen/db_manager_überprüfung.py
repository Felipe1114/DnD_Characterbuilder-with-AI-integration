"""getestet werden soll:
- können daten in die db gespeichert werden?
- kömnnen daten aus der db gelesen werden?
- können objekte aus der db gelöscht werden?
"""
from src.database.models import Base, CharIdea, Character, RewrittenPrompts, KeyDescription, DescriptionToIdea, Classes, \
	BestChar, AnalysedPrompt
from src.database.db_manager import DatabaseManager
from sqlalchemy import create_engine, select





def ue_save_user_prompt(db):
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
	
	stmt = select(RewrittenPrompts)
	result = session.execute(stmt).all()
	
	print(result)
	# Korrigierte Ausgabe der idea_id's
	for prompt in result:
		print(prompt[0].rewritten_prompt)
	
	
if __name__ == "__main__":
	engine = create_engine("sqlite:///:memory:")
	Base.metadata.create_all(engine)
	
	db = DatabaseManager(test_case=True, temp_engine=engine)
	
	# test funtion wird ausgeführt
	ue_save_user_prompt(db)
	
	# schließt lokale db wieder
	Base.metadata.drop_all(engine)






