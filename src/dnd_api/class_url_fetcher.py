from src.dnd_api.base_classes.dnd_api_base import DnDAPIBase
from src.helper.logger import Logger

logger = Logger("dnd_api")

class DnDClassUrlFetcher(DnDAPIBase):
	"""returns all the API-urls for all 12 DnD classes"""
	def __init__(self):
		super().__init__('https://www.dnd5eapi.co/api/classes')
		logger.info(f"class DnDClassUrlFetcher was initialised")
		logger.debug(f"class DnDClassUrlFetcher was initialised as {__name__}")

	def get_class_urls(self):
		self.load_data() # load data from : 'https://www.dnd5eapi.co/api/classes'
		# returns a list of all class urls
		return [f"https://www.dnd5eapi.co{entry['url']}" for entry in self.data.get('results', [])]
