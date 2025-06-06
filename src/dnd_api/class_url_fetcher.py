from src.dnd_api.base_classes.dnd_api_base import DnDAPIBase


class DnDClassUrlFetcher(DnDAPIBase):
	"""Erbt von DnDAPIBase
	gibt die URLs für die requests für alle DnD Klassen von der DnD5e-API zurück"""
	def __init__(self):
		super().__init__('https://www.dnd5eapi.co/api/classes')

	def get_class_urls(self):
		self.load_data() # lädt die daten von : 'https://www.dnd5eapi.co/api/classes'
		# returns a list of all class urls
		return [f"https://www.dnd5eapi.co{entry['url']}" for entry in self.data.get('results', [])]
