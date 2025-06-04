"""
Basis-Klasse für alle 12 DnD-Klassen.
Stellt die Grundstruktur für Subklassen bereit.

Nutzung der Klasse:
1. zuerst mus in die instanzierte Klase ein dnd_class_dict und ein class_nme eingefügt werden
2. dann 'initialize_all_data(self) ausführen
	füllt self.spells, self.levels u. self.subclasses mit daten (von der api)
comment zu 2:
	da die geladenen spells, levels und subclass daten noch keine beschreibung der einzelnen datensäzte haben
	werden in punkt 3 für jeden spell, level/feature und subclass spell/feature, die descriptions von der api angefragt
3. spell_details, level_details und subclass_details ausführen
	lädt alle descriptions der spells, level/features, etc...



"""

from src.DnD_API.dnd_details_fetcher import DnDDetailsFetcher
from src.helper.progress_tracker import ProgressTracker

BASE_URL = "https://www.dnd5eapi.co"

# Diese Klasse verwaltet die Daten einer DnD-Klasse aus der 5e API.
# Sie lädt und verarbeitet Informationen über Zauber, Level und Subklassen.
class ClassDetails:
	def __init__(self, data: dict, class_name: str):
		"""Initialisiert die Klasse mit Basisdaten und prüft den Klassennamen."""
		self.data = data # ein dict mit base-daten einer DnD Klasse
		self.class_name = self.data.get('name', '').lower()
		self.d_fetcher = DnDDetailsFetcher()
		
		# überpft, ob das dictionary auch die daten der richtigen Klasse enthält
		if self.class_name != class_name.lower():
			raise ValueError(f"Wrong data input. Expected '{class_name}', got '{self.class_name}'.")
		
		# detaiil daten ohne descriptions
		self.spells = None
		self.levels = None
		self.subclasses = None
		
		# detaiil daten mit descriptions
		self.enriched_spells = None
		self.enriched_levels = None
		self.enriched_subclasses = [] # da es mögl. mehr subclasses gibt, ist hier eine leere Liste, statt None

	def initialize_all_data(self):
		"""Initialisiert alle Basisdaten: Zauber, Level und Subklassen."""
		# Überprüfen, ob Zauber vorhanden sind und laden
		self.spells = self.load_spells() if 'spells' in self.data else []
		# Laden der Leveldaten
		self.levels = self.load_levels()
		# Laden der Subklassendaten
		self.subclasses = self.load_subclasses()

	def load_spells(self):
		"""Lädt die Zauberinformationen für die Klasse."""
		# API-Call zur Zauber-URL
		url = f"{BASE_URL}{self.data['spells']}"
		
		self.d_fetcher.detail_url = url
		
		# führt api spell-request aus und gibt api spell-response zurück
		return self.d_fetcher.load_data()

	def load_levels(self):
		"""Lädt die Levelinformationen für die Klasse."""
		# erstellt request-url für class_levels
		url = f"{BASE_URL}{self.data['class_levels']}"
		
		# setzt detail_url auf class_level request url
		self.d_fetcher.detail_url = url
		
		# führt api level-request aus und gibt api level-response zurück
		return self.d_fetcher.load_data()

	def load_subclasses(self):
		"""Lädt die Subklasseninformationen für die Klasse."""
		# Erstellen von URLs für alle Subklassen
		urls = [f"{BASE_URL}{entry['url']}" for entry in self.data.get('subclasses', [])]
		all_data = []
		
		for i, url in enumerate(urls):
			self.d_fetcher.detail_url = url
			# führt api sublcass-request aus und gibt api subclass-response zurück
			data = self.d_fetcher.load_data()
			if data:
				all_data.append(data)
		
		# führt api spell-request aus und gibt api spell-response zurück

		# gibt hier nicht self.d_fetcher.load_data zurück, da mehrere 'loadt_data' calls gemacht werden müssen
		return all_data

	def spell_details(self):
		"""Lädt detaillierte Informationen zu den Zaubern der Klasse."""
		if not self.spells:
			return []
		
		# Fortschrittsverfolgung für das Laden der Zauber
		tracker = ProgressTracker(self.spells.get("count", 0), task_name=f"{self.class_name}-spell_details")
		detailed_spells = []

		for i, spell in enumerate(self.spells.get("results", [])):
			# API-Call zur Zauber-URL
			url = f"{BASE_URL}{spell['url']}"
			
			# setzt die url für den fetching prozess
			self.d_fetcher.detail_url = url
			details = self.d_fetcher.load_data()
			
			detailed_spells.append({
			    "index": spell["index"],
			    "name": spell["name"],
			    "level": spell.get("level"),
			    "details": details
			})
			
			tracker.update(message=f'loading spell details{url}')

		tracker.done()
		
		# speichere spells zwischen
		self.enriched_spells = detailed_spells

	def level_details(self):
		"""Lädt detaillierte Informationen zu den Leveln der Klasse.
		"""
		# Fortschrittsverfolgung für das Laden der Level
		tracker = ProgressTracker(len(self.levels), task_name=f"{self.class_name}-level/feature details")
		# leere liste die später in self.enriched_levels gespeichert wird
		# überprüft, ob self.levels überhaupt daten enthält
		if not self.levels:
			raise ValueError("self.data enthält keine daten!!!")
			
		enriched_levels = []
		
		# geht jedes der 20 level in self.levels durch
		for i, level in enumerate(self.levels):
			features = []

			# es wird über die features, in level iteriert
			for feature in level.get('features', []):
				# API-Call zur Feature-URL
				url = f"{BASE_URL}{feature['url']}"
				
				# url für api zugriff wird in fetcher gesetzt
				self.d_fetcher.detail_url = url
				details = self.d_fetcher.load_data()
				if details:
					features.append({
					    "index": feature["index"],
					    "name": feature["name"],
					    "details": details
					})
				else:
					raise ValueError(f"Error: Fehler beim laden von: {self.class_name}-feature: {url}")
				
				tracker.update(message=f'loading level/feature details{url}')

			enriched_levels.append({
									"level": level["level"],
			                        "ability_score_bonuses": level["ability_score_bonuses"],
			                        "prof_bonus": level["prof_bonus"],
			                        "features": features,
			                        "spellcasting": level.get("spellcasting", None),
			                        "class_specific": level["class_specific"],
			                        "index": level["index"],
			                        })

		# angefragte daten abspeichern
		self.enriched_levels = enriched_levels
		tracker.done()
		



	def subclass_details(self):
		"""Lädt detaillierte Informationen zu den Subklassen der Klasse."""
		# Fortschrittsverfolgung für das Laden der Subklassen
		tracker = ProgressTracker(len(self.subclasses), task_name=f"{self.class_name}-subclasses")
		
		for i, subclass in enumerate(self.subclasses):
			tracker.update(message='loading subclasses')
			self._enrich_subclass(subclass)
		
		tracker.done()

	def _enrich_subclass(self, subclass):
		"""Ergänzt die Subklasseninformationen mit Zaubern und Leveln/features."""
		# Spells
		if 'spells' in subclass:
			subclass_spells = []
			spell_list = subclass.get('spells', [])
			# Fortschrittsverfolgung für das Laden der Subklassenzauber
			spell_tracker = ProgressTracker(len(spell_list), task_name=f"{self.class_name}-subclass:{subclass['name']} spells")

			for s, spell_entry in enumerate(spell_list):
				spell = spell_entry.get('spell', {})
				# API-Call zur Zauber-URL
				url = f"{BASE_URL}{spell.get('url')}"
				self.d_fetcher.detail_url = url
				details = self.d_fetcher.load_data()
				
				subclass_spells.append({
				    "index": spell.get("index"),
				    "name": spell.get("name"),
				    "prerequisites": spell_entry.get("prerequisites"),
				    "details": details
				})
				
				spell_tracker.update(message=f'loading {subclass['name']} spells:{url}')
			
			spell_tracker.done()
			subclass['spells'] = subclass_spells

		# Subclass Levels
		if 'subclass_levels' in subclass:
			# API-Call zur Subclass Levels-URL
			url = f"{BASE_URL}{subclass['subclass_levels']}"
			self.d_fetcher.detail_url = url
			levels = self.d_fetcher.load_data()
			
			# Fortschrittsverfolgung für das Laden der Subklassenzauber
			feature_tracker = ProgressTracker(len(levels), task_name=f"{self.class_name}-subclass:{subclass['name']} levels/features")

			for level in levels:
				features = []
				for feature in level.get('features', []):
					# API-Call zur Feature-URL
					f_url = f"{BASE_URL}{feature['url']}"
					self.d_fetcher.detail_url = f_url
					details = self.d_fetcher.load_data()
					features.append({
					    "index": feature["index"],
					    "name": feature["name"],
					    "details": details
					})
					
					feature_tracker.update(message=f'loading {subclass['name']} levels/features: {f_url}')

				level["features"] = features

			subclass['subclass_levels'] = levels
			
			self.enriched_subclasses.append(subclass)


	def initialize_all_details(self) -> tuple:
		"""Lädt alle Details: Zauber, Level und Subklassen."""
		if self.spells:
			self.spell_details()
		self.level_details()
		self.subclass_details()
		return self.enriched_spells, self.enriched_levels, self.enriched_subclasses