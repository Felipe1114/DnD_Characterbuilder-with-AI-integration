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