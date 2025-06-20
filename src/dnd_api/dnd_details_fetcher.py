import requests
import time
from requests import RequestException
from src.dnd_api.base_classes.dnd_api_base import DnDAPIBase
from fastapi import HTTPException
from src.helper.logger import Logger

logger = Logger("dnd_api")

class DnDDetailsFetcher(DnDAPIBase):
	"""
	Loads details for the dnd_base data of the dnd_classes from the DnD5e-api
	"""

	def __init__(self, base_url=None):
		"""
		Initialice the fetcher; optional the base_url can be changed
		"""
		logger.info(f"initialize class DnDDetailsFetcher as {__name__}")

		super().__init__(base_url)
		self.class_detail_url = None  # This Urls will be set later, to load class datas
		self.data = {}  # the loaded data will be saved here
		
	def load_data(self, delay=0.1):
		"""
		Loads the class_data from the actual setted URL (class_detail_url)
	    """
		try:
			if not self.class_detail_url:
				logger.error(f"Error with DnD5e-API; No url was set. Url must be set, before api request")
				raise HTTPException(status_code=502, detail="no url for DnD5e-api; url must set, before loading class_detail_data")
			
			response = requests.get(self.class_detail_url)
			
			if response.status_code == 200:
				logger.info(f"loading detail data from DnD5e-api from url: {self.class_detail_url}")
				self.data = response.json() # the data from the Api-response will be saved here
				
				time.sleep(delay)
			
			else:
				logger.error(f"Loading data from DnD5e-api failed; HTTP-status: {response.status_code}")
				
				raise RequestException(
				    f"Error: Loading of data failed; HTTP-status: {response.status_code}"
				)
			
			# returns data from api-response as Json
			return self.data

		except RequestException as e:
			raise HTTPException(status_code=502, detail=f"Error with DnD5e-api: {e}")
		
		except HTTPException as e:
			if e.status_code == 502:
				raise HTTPException(status_code=502, detail=e)
			
			else:
				raise HTTPException(status_code=500, detail=e)
			

	@property
	def detail_url(self):
		"""gives back the class_detail_url"""
		logger.debug(f"detail_url from class: DnDDetailsFetcher is requested")
		
		return self.class_detail_url

	@detail_url.setter
	def detail_url(self, new_detail_url):
		"""sets a new class_detail_url"""
		
		self.class_detail_url = new_detail_url
		
		logger.info(f"url for class_DnDDetailsFetcher was set")
		logger.debug(f"url for class_DnDDetailsFetcher was set to: {new_detail_url}")
