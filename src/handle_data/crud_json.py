from src.handle_data.base_classes.crud_base import CrudBase
import json
from json import JSONDecodeError
from fastapi import HTTPException
from src.helper.logger import Logger

logger = Logger("data_handler")

class CrudJsonFiles(CrudBase):
	"""handels JSON crud operations"""
	def _save(self, data):
		"""saves data in storage; if file not exists, a new file is created"""
		try:
			logger.debug(f"data: {data} will savend in file: {self.data_path}")
			with open(self.data_path, 'w') as json_obj:
				json.dump(data, json_obj, indent=4)
			logger.debug(f"saved json-file: {self.data_path} with data: {data} ")
			
		except JSONDecodeError as e:
			logger.critical(f"Error: JSONDecodeError with: {self.data_path}; Error: {e}")
			raise HTTPException(status_code=500, detail=f"Error with Json decoding: {e}")
		
		except FileNotFoundError as e:
			logger.warning(f"FileNotFoundError: {e} -> cause not existing dir?; new dir will be created")
			# checks if dir exists; if not create new dir.
			self.check_dir()
			
			# save dta in new created dir
			self._save(data)
			
			# counts tries of self.check_dir()
			self._tries_of_i += 1
			
			# checks, if
			self.check_tries_of_i(error_message=f"to many tries of checking path: {self.data_path}; error in creating {self.data_path}")
			
		except Exception as e:
			logger.error(f"Error occured: {e}")
			
	@property
	def data(self):
		"""returns the data from storage"""
		try:
			logger.debug(f"load_data from file: {self.data_path}")
			
			with open(self.data_path, 'r') as json_obj:
				existing_data = json.load(json_obj)
				logger.info(f"loading data: {existing_data}")
				
				return existing_data
			
		except (FileNotFoundError, JSONDecodeError):
			logger.warning(f"Error with loading data from file: {self.data_path}; will return empty list")
			
			# set existing_data to empty list
			existing_data = []
			
			return existing_data

	@data.setter
	def data(self, new_data):
		"""saves new data to storage"""
		existing_data = self.data
		
		logger.debug(f"load data: {existing_data} from file: {self.data_path}")
		
		existing_data.append(new_data)
		
		logger.debug(f"append new_data: {new_data} to exiting_data: {existing_data}")
		self._save(existing_data)
		
		logger.debug(f"save updated data")
		logger.info(f"Data:{new_data} was added and saved to file: {self.data_path}")


	def new_file(self, new_data):
		"""saves data in a new file"""
		logger.debug(f"save data: {new_data} to new file: {self.data_path}")
		
		self._save(new_data)
		
		logger.info(f"new_data: {new_data} was savend to file: {self.data_path}")
		
	def reset(self, empty_data=[]):
		"""resets a JSON-file; empty_data can be [] or {}."""
		# checks if correct empty data type is given for 'empty_data'
		if not empty_data in [{}, []]:
			logger.warning(f"Error with reset JSON-file: {self.data_path}; got wrong Value: {empty_data} instead of [] or {"{}"}")
			raise ValueError("empty_data has to be '[]' or '{}'")
		
		super().reset(empty_data)

		
