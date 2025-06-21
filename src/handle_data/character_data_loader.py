from src.handle_data.crud_json import CrudJsonFiles
from src.handle_data.env_loader import EnvLoader
from src.helper.logger import Logger

logger = Logger("data_handler")

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
	"""Loads all class data for a specific class from local storage; 'class_name' is one of the 12 possible classes"""
	def __init__(self, class_name):
		logger.info(f"initialize CharacterDataLoader")
		self.class_name = class_name.lower()
		logger.debug(f"initialize self.class_name as: {self.class_name}")
		
		self.data_base_path = EnvLoader.static_dnd_data_dir() # base_dir path from .env
		logger.debug(f"initialize self.data_base_paht as: {self.data_base_path}")
		self.base_data_path = "all_classes.json"
		logger.debug(f"initialize self.base_data_paht as: {self.base_data_path}")
		self.class_data_path = f"/detailed_class_data/{class_name}/{class_name}" # constructor for class_dir ending
		logger.debug(f"initialize self.class_data_path as: {self.class_data_path}")
		
		self.detail_base_path = self.data_base_path + self.class_data_path # path constructor for individual class dir
		logger.debug(f"initialize self.detail_base_path as: {self.detail_base_path}")
		
		self.class_base_data = self.data_base_path + "/" + self.base_data_path
		logger.debug(f"initialize self.class_base_data as: {self.class_base_data}")
		
		self.spell_file_path = self.detail_base_path + "_spells.json"
		logger.debug(f"initialize self.spell_file_path as: {self.spell_file_path}")
		self.level_file_path = self.detail_base_path + "_levels_features.json"
		logger.debug(f"initialize self.level_file_path as: {self.level_file_path}")
		self.subclass_file_path = self.detail_base_path + "_subclass(es).json"
		logger.debug(f"initialize self.subclass_file_path as: {self.subclass_file_path}")

	def class_data(self) -> list:
		"""returns all data from a class in a list"""
		logger.info(f"load class data for class: {self.class_name}")
		
		base_crud = CrudJsonFiles(self.class_base_data)
		spell_crud = CrudJsonFiles(self.spell_file_path)
		level_crud = CrudJsonFiles(self.level_file_path)
		subclass_crud = CrudJsonFiles(self.subclass_file_path)
				
		base_data: dict = base_crud.data[CLASS_INDICIES[self.class_name]]
		
		spells: list = spell_crud.data
		level_features: list = level_crud.data
		subclasses: list = subclass_crud.data
		
		logger.info(f"loading of class data for {self.class_name} was succesfull")
		return [base_data, spells, level_features, subclasses]
 
	def run(self):
		logger.info(f"run CharacterDataLoader...")
		return self.class_data()






