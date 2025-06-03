from abc import ABC, abstractmethod
from pathlib import PurePath
import os

class CrudBase(ABC):
	"""handles crud operations for local data"""
	def __init__(self, data_path):
		self.data_path = data_path
		self._pure_path = PurePath(self.data_path)
		self._parent_path = self._pure_path.parent
	
	@abstractmethod
	def _save(self, data):
		"""saves data in storage; if file not exists, a new file is created"""
		pass
	
	@property

	@abstractmethod
	def data(self):
		"""returns the data from storage"""
		pass
	
	@data.setter

	@abstractmethod
	def data(self, new_data):
		"""saves new data to storage"""
		existing_data = self.data()
		existing_data.append(new_data)
		self._save(existing_data)
		pass
	
	@abstractmethod
	def new_file(self, new_data):
		"""saves data in a new file"""
		self._save(new_data)
		
	@abstractmethod
	def reset(self, empty_data=None):
		"""resets a file to None; depending on witch data-type the Crud-Class is working,
		'empty_data' has to be None or '[]'"""
		self._save(empty_data)
	
	def check_path(self):
		"""checks, if a dir exists. If not, the dir is created"""
		if not os.path.exists(self._parent_path):
			os.makedirs(self._parent_path)

