"""überprüft, ob CharacterBuilderApp funktioniert
testet die applikation mit der idea_id '1'

idea_id 1 soll einen character bauen, der an Conan den bararen erinnert"""
from src.llm.character_builder_app import CharacterBuilderApp

idea_id = 1

char_builder = CharacterBuilderApp(idea_id)
char_builder.run()