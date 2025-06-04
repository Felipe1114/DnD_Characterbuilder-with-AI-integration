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
		return os.getenv("DB_PATH")
	
	@staticmethod
	def mistral_key():
		return os.getenv("MISTARL_API_KEY")
	
	@staticmethod
	def system_message():
		return os.getenv("SYSTEM_MESSAGE")
	
	@staticmethod
	def all_class_data_template():
		return os.getenv("ALL_CLASS_TEMPLATE")
	
	@staticmethod
	def all_dnd_classes():
		return os.getenv("ALL_DND_CLASSES")
	
	@staticmethod
	def detailed_class_data_dir():
		return os.getenv("DETAILED_CLASS_DATA_DIR")