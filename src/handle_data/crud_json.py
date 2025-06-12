from src.handle_data.crud_base import CrudBase
import json
import os

class CrudJsonFiles(CrudBase):
	"""handels JSON crud operations"""
	def _save(self, data):
		"""saves data in storage; if file not exists, a new file is created"""
		with open(self.data_path, 'w') as json_obj:
			json.dump(data, json_obj, indent=4)

	@property
	def data(self):
		"""returns the data from storage"""
		try:
			with open(self.data_path, 'r') as json_obj:
				existing_data = json.load(json_obj)
			
				return existing_data

		except (FileNotFoundError, json.JSONDecodeError):
			print(f"Error: {self.data_path} could not be found")
			existing_data = []
			
			return existing_data

	@data.setter
	def data(self, new_data):
		"""saves new data to storage"""
		existing_data = self.data
		
		existing_data.append(new_data)
		
		self._save(existing_data)
		

	def new_file(self, new_data):
		"""saves data in a new file"""
		self._save(new_data)
  
  
	def reset(self, new_data=[]):
		"""resets a file to None; depending on witch data-type the Crud-Class is working,
		'empty_data' has to be None or '[]'"""
		self._save(new_data)
		
	def check_path(self):
		"""checks, if a dir exists. If not, the dir will be created"""
		if not os.path.exists(self._parent_path):
			os.makedirs(self._parent_path)

	

