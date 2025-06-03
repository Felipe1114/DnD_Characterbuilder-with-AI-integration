from src.handle_data.crud_base import CrudBase
import json
import os

class CrudJsonFiles(CrudBase):
	def _save(self, data):
		with open(self.data_path, 'w') as json_obj:
			json.dump(data, json_obj, indent=4)


	@property
	def data(self):
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
		existing_data = self.data
		
		existing_data.append(new_data)
		
		self._save(existing_data)
		

	def new_file(self, new_data):
		self._save(new_data)
  
  
	def reset(self, new_data=[]):
		self._save(new_data)
		
	def check_path(self):
		"""überprüft, ob die directories, in denen das file liegen soll, existieren.
		Falls nein, wird das directory erstellt"""
		if not os.path.exists(self._parent_path):
			os.makedirs(self._parent_path)

	

