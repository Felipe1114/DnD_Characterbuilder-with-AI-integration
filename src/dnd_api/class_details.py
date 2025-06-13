from src.dnd_api.dnd_details_fetcher import DnDDetailsFetcher
from src.helper.progress_tracker import ProgressTracker

BASE_URL = "https://www.dnd5eapi.co"

class ClassDetails:
	"""Class loads all detailed information witch are not in the 'base' dictionary of a dnd-claass
	
	The loades details are not enough. They need more descriptions.
	So the progranmm prozess is:
		1. load detail data form base-data
		2. load descriptions for each detail-data
	"""
	def __init__(self, data: dict, class_name: str):
		self.data = data # the 'base-data' dict of a dnd class
		self.class_name = self.data.get('name', '').lower()
		self.d_fetcher = DnDDetailsFetcher()
		
		
		if self.class_name != class_name.lower():
			raise ValueError(f"Wrong data input. Expected '{class_name}', got '{self.class_name}'.")
		
		# detail data without desccirptions
		self.spells = None
		self.levels = None
		self.subclasses = None
		
		# detail data with descriptions
		self.enriched_spells = None
		self.enriched_levels = None
		self.enriched_subclasses = [] # cause in a further version their will be more than one sublcass, here is an empty list, insted None

	def initialize_all_data(self):
		"""loads all detail data from the base data dict"""
		# if spells are in base data dict, load spells
		self.spells = self.load_spells() if 'spells' in self.data else []
		# loads detail data for levels
		self.levels = self.load_levels()
		# loads detail data for sublcasses
		self.subclasses = self.load_subclasses()

	def load_spells(self):
		"""load details for spells"""
		url = f"{BASE_URL}{self.data['spells']}"
		
		self.d_fetcher.detail_url = url
		
		return self.d_fetcher.load_data()

	def load_levels(self):
		"""loads detail data for level"""
		url = f"{BASE_URL}{self.data['class_levels']}"
		
		self.d_fetcher.detail_url = url
		
		return self.d_fetcher.load_data()

	def load_subclasses(self):
		"""loads detils for subclass data
		
		cause in the future their will be more subclasses, this method contains the logic for the loading porcess of more than one subclass
		"""
		urls = [f"{BASE_URL}{entry['url']}" for entry in self.data.get('subclasses', [])]
		all_data = []
		
		for i, url in enumerate(urls):
			self.d_fetcher.detail_url = url

			data = self.d_fetcher.load_data()
			if data:
				all_data.append(data)
		
	
		return all_data

	def spell_details(self):
		"""loads descriptions for spell_data"""
		if not self.spells:
			return []
		
		# progress tracker for user interface
		tracker = ProgressTracker(self.spells.get("count", 0), task_name=f"{self.class_name}-spell_details")
		detailed_spells = []

		for i, spell in enumerate(self.spells.get("results", [])):

			url = f"{BASE_URL}{spell['url']}"
			
			self.d_fetcher.detail_url = url
			details = self.d_fetcher.load_data()
			
			# creates a new dict, with the spell data and its descriptions
			detailed_spells.append({
			    "searched_index": spell["searched_index"],
			    "name": spell["name"],
			    "level": spell.get("level"),
			    "details": details
			})
			
			tracker.update(message=f'loading spell details{url}')

		tracker.done()
		
		# save spell data with descriptions
		self.enriched_spells = detailed_spells

	def level_details(self):
		"""loads descriptions for level data"""
		# progress tracker for user interface
		tracker = ProgressTracker(len(self.levels), task_name=f"{self.class_name}-level/feature details")

		# does self.levels hase data?
		if not self.levels:
			raise ValueError("self.data enthält keine daten!!!")
			
		enriched_levels = []
		
		# iterates over each level and each feature in each level. 1 level of nested loops
		# level iteration
		for i, level in enumerate(self.levels):
			features = []

			# feature iteration
			for feature in level.get('features', []):

				url = f"{BASE_URL}{feature['url']}"
				
				self.d_fetcher.detail_url = url
				details = self.d_fetcher.load_data()
				
				# creates a new dict with level features and its descriptions
				if details:
					features.append({
					    "searched_index": feature["searched_index"],
					    "name": feature["name"],
					    "details": details
					})
				else:
					raise ValueError(f"Error: Error of loading: {self.class_name}-feature: {url}")
				
				tracker.update(message=f'loading level/feature details{url}')
			
			# create new dict with the current level and its new feature dict with their descriptions
			enriched_levels.append({
									"level": level["level"],
			                        "ability_score_bonuses": level["ability_score_bonuses"],
			                        "prof_bonus": level["prof_bonus"],
			                        "features": features,
			                        "spellcasting": level.get("spellcasting", None),
			                        "class_specific": level["class_specific"],
			                        "searched_index": level["searched_index"],
			                        })

		self.enriched_levels = enriched_levels
		
		tracker.done()
		
	def subclass_details(self):
		"""loads descripitions for subclass data"""
		# progress tracker für user interface
		tracker = ProgressTracker(len(self.subclasses), task_name=f"{self.class_name}-subclasses")
		
		for i, subclass in enumerate(self.subclasses):
			tracker.update(message='loading subclasses')
			self._enrich_subclass(subclass)
		
		tracker.done()

	def _enrich_subclass(self, subclass):
		"""loads the spells for the subclass"""
		self._load_subclass_spells(subclass)
		self._load_subclass_levels(subclass)
		
		self.enriched_subclasses.append(subclass)
	
	def _load_subclass_levels(self, subclass):
		if 'subclass_levels' in subclass:

			url = f"{BASE_URL}{subclass['subclass_levels']}"
			self.d_fetcher.detail_url = url
			levels = self.d_fetcher.load_data()
			
			# progress tracker for uster interface
			tracker = ProgressTracker(len(levels),
			                                  task_name=f"{self.class_name}-subclass:{subclass['name']} levels/features")
			
			for level in levels:
				features = []
				for feature in level.get('features', []):
					# API-Call zur Feature-URL
					f_url = f"{BASE_URL}{feature['url']}"
					self.d_fetcher.detail_url = f_url
					details = self.d_fetcher.load_data()
					features.append({
						"searched_index": feature["searched_index"],
						"name": feature["name"],
						"details": details
					})
					
					tracker.update(message=f'loading {subclass['name']} levels/features: {f_url}')
				
				level["features"] = features
			
			subclass['subclass_levels'] = levels
			
	
	def _load_subclass_spells(self, subclass):
		if 'spells' in subclass:
			subclass_spells = []
			spell_list = subclass.get('spells', [])
			# progress tracker for user interface
			tracker = ProgressTracker(len(spell_list),
			                          task_name=f"{self.class_name}-subclass:{subclass['name']} spells")
			
			for s, spell_entry in enumerate(spell_list):
				spell = spell_entry.get('spell', {})
				url = f"{BASE_URL}{spell.get('url')}"
				self.d_fetcher.detail_url = url
				details = self.d_fetcher.load_data()
				
				subclass_spells.append({
					"searched_index": spell.get("searched_index"),
					"name": spell.get("name"),
					"prerequisites": spell_entry.get("prerequisites"),
					"details": details
				})
				
				tracker.update(message=f'loading {subclass['name']} spells:{url}')
			
			tracker.done()
			
			subclass['spells'] = subclass_spells
	
	def initialize_all_details(self) -> tuple:
		"""puts all loading funktions togeter. Loads all detail data for class_data"""
		if self.spells:
			self.spell_details()
		self.level_details()
		self.subclass_details()
		return self.enriched_spells, self.enriched_levels, self.enriched_subclasses