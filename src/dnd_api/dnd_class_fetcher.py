from src.dnd_api.base_classes.dnd_api_base import DnDAPIBase
from src.handle_data.crud_json import CrudJsonFiles
from src.handle_data.env_loader import EnvLoader
from src.helper.logger import Logger

logger = Logger("dnd_api")

class DnDClassFetcher(DnDAPIBase):
	def __init__(self, url):
		super().__init__(url)
		logger.info(f"class DnDClassFetcher was intitialized")

		self.all_dnd_classes_path = EnvLoader.all_dnd_classes()
		logger.debug(f"initialize self.all_dnd_class_paths as: {self.all_dnd_classes_path}")
		
		self.crud_json = CrudJsonFiles(self.all_dnd_classes_path)
		
		logger.debug(f"class DnDClassFechter was initialized as: {__name__}")
	
	def load_and_save(self):
		"""Loads data from the dnd5e-api and savev them in Json"""
		logger.info(f"load base_class data for all calsses")
		
		self.load_data()
		
		indicies = [key for key in self.data.keys() if key != 'updated_at']
		
		class_data_dict = {i: self.data.get(i) for i in indicies}
		logger.debug(f"loaded class_data in a dict: {class_data_dict}")
		
		self.save_data(class_data_dict)
	 
	def save_data(self, new_data):
		"""saves loaded data in JSON file"""
		logger.info(f"saved class data in JSON file")
		
		self.crud_json.data = new_data



