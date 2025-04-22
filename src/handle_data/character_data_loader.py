from src.handle_data.crud_json import CrudJsonFiles
# TODO: pydantic kann hier noch für die input validierung eingefügt werden
CLASS_INDICIES = {
  "barbarian": 0,
  "bard": 1,
  "cleric": 2,
  "druid": 3,
  "fighter": 4,
  "monk": 5,
  "paladin": 6,
  "ranger": 7,
  "rogue": 8,
  "sorcerer": 9,
  "warlock": 10,
  "wizard": 11
                }

class CharacterDataLoader:
	"""läd einen character aus dem lokalen speicher. 'class_name' ist eine von den 12 möglichen Klassen"""
	def __init__(self, class_name):
		
		self.class_name = class_name.lower()
		self.data_base_path = "../../static_dnd_data/"
		self.base_data_path = "all_classes.json"
		self.class_data_path = f"/detailed_class_data/{class_name}/{class_name}"
		
		self.detail_base_path = self.data_base_path + self.class_data_path
		
		self.class_base_data = self.data_base_path +  self.base_data_path
		self.spell_file_path = self.detail_base_path + "_spells.json"
		self.level_file_path = self.detail_base_path + "_levels_features.json"
		self.subclass_file_path = self.detail_base_path + "_subclass(es).json"

			# erstellt eine liste mit spell-, level- und subclass-datapath


	def class_data(self) -> list:
		"""gibt alle klassen daten, in einer liste zurück"""
		base_crud = CrudJsonFiles(self.class_base_data)
		spell_crud = CrudJsonFiles(self.spell_file_path)
		level_crud = CrudJsonFiles(self.level_file_path)
		subclass_crud = CrudJsonFiles(self.subclass_file_path)
		
		base_data: dict = base_crud.data[CLASS_INDICIES[self.class_name]]
		
		spells: list = spell_crud.data
		level_features: list = level_crud.data
		subclasses: list = subclass_crud.data
		
		return [base_data, spells, level_features, subclasses]
 
	def run(self):
		return self.class_data()


if __name__ == "__main__":
	loader = CharacterDataLoader("barbarian")
	data = loader.run()
	print(data)





