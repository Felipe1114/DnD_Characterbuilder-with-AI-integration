from src.dnd_api.base_classes.dnd_api_base import DnDAPIBase


class DnDClassUrlFetcher(DnDAPIBase):
	"""returns all the API-urls for all 12 DnD classes"""
	def __init__(self):
		super().__init__('https://www.dnd5eapi.co/api/classes')

	def get_class_urls(self):
		self.load_data() # load data from : 'https://www.dnd5eapi.co/api/classes'
		# returns a list of all class urls
		return [f"https://www.dnd5eapi.co{entry['url']}" for entry in self.data.get('results', [])]
