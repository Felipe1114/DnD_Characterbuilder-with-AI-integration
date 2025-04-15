from src.DnD_API.dnd_api_base import DnDAPIBase
from src.handle_data.CRUD import CRUD

class DnDClassFetcher(DnDAPIBase):
	def __init__(self, url):
		super().__init__(url)
		self.crud = CRUD("../../static_dnd_data/all_classes.json")

	def load_and_save(self):
		self.load_data()
		indicies = [key for key in self.data.keys() if key != 'updated_at']
		class_data_dict = {i: self.data.get(i) for i in indicies}

		self.save_data(class_data_dict)
	 
	# temporary method
	def save_data(self, new_data):
		self.crud.data = new_data



