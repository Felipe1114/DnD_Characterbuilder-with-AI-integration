from src.DnD_API.class_url_fetcher import DnDClassUrlFetcher
from src.DnD_API.dnd_class_fetcher import DnDClassFetcher


class DnDApiManager:
	"""holt alle 'base'-Klassen daten von der DnD5e-API und erstellt ein großes Josn mit allen 12 Klassen und base-daten"""
	def __init__(self):
		self.classes = []
	
	def run(self):
		# instanziert DnDClassListFetcher
		fetcher = DnDClassUrlFetcher()
		# gets all urls for all classes, in a list
		# hier kommt raus:
		# ['https://www.dnd5eapi.co/api/2014/classes/barbarian', 'https://www.dnd5eapi.co/api/2014/classes/bard', ...
		class_urls = fetcher.get_class_urls()
		
		# TODO: wenn file: 'all_classes.json' schon existiert, soll die for-schleife nicht ausgeführt werden
		# lädt alle daten von der DnD5e-API und speichert sie in file
		for url in class_urls:
			print(f"→ load class: {url}")
			char_class = DnDClassFetcher(url)
			char_class.load_and_save()
			print(char_class.data)
			self.classes.append(char_class)
			
		# TODO: hier auch ClassDetails einbauen, damit alles über den DnDClassManager läuft
			
#
# if __name__ == "__maxin__":
# 	manager = DnDClassManager()
# 	manager.run()
	