from abc import ABC, abstractmethod
from pathlib import PurePath
import os
from src.helper.logger import Logger
from fastapi import HTTPException

logger = Logger("data_handler")

class CrudBase(ABC):
	"""handles crud operations for local data"""
	def __init__(self, data_path):
		self.data_path = data_path
		self._pure_path = PurePath(self.data_path)
		self._parent_path = self._pure_path.parent
		
		# secruity number to get shure no recursion loop occures
		self._tries_of_i = 0
		
		logger.debug(f"initialize Crudclass: {__name__}")
		
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
		logger.debug(f"load existing data: {existing_data}")
		
		existing_data.append(new_data)
		logger.debug(f"append new_data: {new_data} to existing_data")
		
		self._save(existing_data)
		logger.debug(f"saved updated data")
		
		logger.info(f"append data: {new_data} to {self.data_path} and saved")
		
	@abstractmethod
	def new_file(self, new_data):
		"""saves data in a new file"""
		self._save(new_data)
		
		logger.info(f"new file: {self.data_path} with data: {new_data} was created and saved")
		
	@abstractmethod
	def reset(self, empty_data=None):
		"""resets a file to None; depending on witch data-type the Crud-Class is working,
		'empty_data' has to be None or '[]'"""
		self._save(empty_data)
		
		logger.debug(f"file: {self.data_path} was resetet by saving empty data to file")
		logger.info(f"file: {self.data_path} was resetet")
		
	
	def check_dir(self):
		"""checks, if a dir exists. If not, the dir is created"""
		logger.debug(f"check, if file_path: {self.data_path} does exist")
		if not os.path.exists(self._parent_path):
			logger.debug(f"file_path: {self.data_path} does not exist")
			
			os.makedirs(self._parent_path)
			logger.info(f"check file_path: {self.data_path} -> file path dosn´t exist; file path was created")
		
		logger.info(f"check file_path: {self.data_path} -> file path exist")


	def check_tries_of_i(self, error_message: str="tries_of_i is to high!!!", max_tries: int=3):
		"""checks wath the number of tries_of_i is. If number is over 3 Error is raised"""
		try:
			if self._tries_of_i >= max_tries:
				raise OSError(f"{error_message}")
		
		except OSError as e:
			raise HTTPException(status_code=500, detail=f"Internal Server Error with file path: {self.data_path}; path couldn´t be created")