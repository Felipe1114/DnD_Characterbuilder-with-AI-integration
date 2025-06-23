import requests
from requests import RequestException
import time
from fastapi import HTTPException
from src.helper.logger import Logger

logger= Logger("dnd_api")

class DnDAPIBase:
	"""Baseclass for DnDAPI 'loader'. Contains the base logic for the 'loader' module"""
	def __init__(self, url):
		logger.info(f"class DnDAPIBase is initialiced")
		
		self.url = url
		self.data = {}
		
		logger.debug(f"class DnDAPIBAse as: {__name__} was initialized")

	def load_data(self):
		"""loads data from DnD5e-API, depending on given url"""
		try:
			logger.info(f"load data from DnD5e-api; url for request: {self.url}")
			
			response = requests.get(self.url)

			if response.status_code == 200:
				self.data = response.json()
				time.sleep(0.1)  # delay for API

			else:
				raise RequestException(f"Error at loading: {response.status_code}; dnd_api_base.py 20")
		
		except RequestException as e:
			logger.error(f"Error with DnD5e-api: {e}")
			
			raise HTTPException(status_code=502, detail=f"Error with DnD5e-api: {e}")
		
