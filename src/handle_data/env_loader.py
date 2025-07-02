from dotenv import load_dotenv
import os

# loads .env file
load_dotenv()


class EnvLoader:
	"""
	lods data with keys from .env file
	"""
	@staticmethod
	def db_path():
		"""database dir path"""
		return os.getenv("DB_PATH")
	
	@staticmethod
	def mistral_key():
		"""api-key for mistral LLM"""
		return os.getenv("MISTARL_API_KEY")
	
	@staticmethod
	def all_class_data_template():
		"""path for .txt file with the 'all class data' template, where all data for one class is stored and put into the sytem message"""
		return os.getenv("ALL_CLASS_TEMPLATE")
	
	@staticmethod
	def all_dnd_classes():
		"""path to all dnd classes JSON"""
		return os.getenv("ALL_DND_CLASSES")
	
	@staticmethod
	def detailed_class_data_dir():
		"""path to details class data dir"""
		return os.getenv("DETAILED_CLASS_DATA_DIR")
	
	@staticmethod
	def static_dnd_data_dir():
		"""path to static dnd data dir; main dir for all dnd data in local storage"""
		return os.getenv("STATIC_DND_DATA_DIR")
	
	@staticmethod
	def log_dir():
		"""path to log_dir"""
		return os.getenv("LOG_DIR")
	
	@staticmethod
	def character_dir():
		"""path to generated local characters"""
		return os.getenv("CHARACTER_DIR")