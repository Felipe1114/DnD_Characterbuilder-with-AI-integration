from src.handle_data.character_data_loader import CharacterDataLoader

loader = CharacterDataLoader("wizard")

data = loader.class_data()

print(data)