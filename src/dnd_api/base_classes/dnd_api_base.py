import requests
from requests import RequestException
import time
from fastapi import HTTPException


class DnDAPIBase:
	"""Baseclass for DnDAPI 'loader'. Contains the base logic for the 'loader' module"""
	def __init__(self, url):
		self.url = url
		self.data = {}

	def load_data(self):
		"""loads data from DnD5e-API, depending on given url"""
		try:
			response = requests.get(self.url)

			if response.status_code == 200:
				self.data = response.json()
				time.sleep(0.1)  # delay for API

			else:
				raise RequestException(f"Error at loading: {response.status_code}; dnd_api_base.py 20")
		
		except RequestException as e:
			raise HTTPException(status_code=502, detail=f"Error with DnD5e-api: {e}")
		
