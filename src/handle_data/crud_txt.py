from src.handle_data.crud_base import CrudBase

class CrudTxtFiles(CrudBase):
	"""
	handels crud operations on .txt files
	
	Class Variables form __init__:
		self.data_path -> data_path
		self._pure_path -> PurePathClass
		self._parent_path = -> the path before the 'file_name' like: ../crud_txt.py
	"""
	def _save(self, data):
		"""saves data in storage"""
		with open(self.data_path, "w") as txt_obj:
			txt_obj.write(data)
			
			
	@property
	def data(self) -> str:
		"""returns the data from storage, if file not exists, an empty string es returned"""
		try:
			with open(self.data_path, "r") as txt_obj:
				data = txt_obj.read()
				
			return data
		except FileNotFoundError:
			print(f"file: {self.data_path} does not exists, return empty string")
			data = ""
			return data
	
	@data.setter
	def data(self, new_data):
		"""saves new data to storage, if file not exists, a new file is created with self.data_paht"""
		existing_data = self.data
		
		# if existing_data is empty
		if len(existing_data) < 1:
			existing_data = new_data
		
		# if data exists in existing_data, new data is 'appended' with \n as seperator
		else:
			existing_data = existing_data + '\n' + new_data
		
		self._save(existing_data)
		
	
	def new_file(self, new_data):
		"""saves data in a new file"""
		self._save(new_data)
	
	def reset(self, empty_data=""):
		"""resets a .txt file - per default - with an empty string'"""
		self._save(empty_data)
	
