from src.dnd_api.base_classes.dnd_api_base import DnDAPIBase
from src.handle_data.crud_json import CrudJsonFiles
from src.handle_data.env_loader import EnvLoader

class DnDClassFetcher(DnDAPIBase):
	def __init__(self, url):
		super().__init__(url)
		self.all_dnd_classes_path = EnvLoader.all_dnd_classes()
		self.crud = CrudJsonFiles(self.all_dnd_classes_path)

	def load_and_save(self):
		self.load_data()
		indicies = [key for key in self.data.keys() if key != 'updated_at']
		class_data_dict = {i: self.data.get(i) for i in indicies}

		self.save_data(class_data_dict)
	 
	def save_data(self, new_data):
		self.crud.data = new_data



