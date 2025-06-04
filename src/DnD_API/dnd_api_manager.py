from src.DnD_API.class_url_fetcher import DnDClassUrlFetcher
from src.DnD_API.dnd_class_fetcher import DnDClassFetcher
from src.DnD_API.class_details import ClassDetails
from src.helper.progress_tracker import ProgressTracker
from src.handle_data.crud_json import CrudJsonFiles
from src.helper.debug_log import DebugLog

"""
Note:
	1. nach dem laden der detailed daten einer class wierden für alle drei detail-files ein Error angezeigt
		Woher kommen diese Error nachrichten?
"""

class DnDApiManager:
	"""holt alle 'base'-Klassen daten von der DnD5e-API und erstellt ein großes Josn mit allen 12 Klassen und base-daten"""
	def __init__(self):
		self.class_ids = {
            'barbarian': 0,
            'bard': 1,
            'cleric': 2,
            'druid': 3,
            'fighter': 4,
            'monk': 5,
            'paladin': 6,
            'ranger': 7,
            'rogue': 8,
            'sorcerer': 9,
            'warlock': 10,
            'wizard': 11
                        }
	@DebugLog.debug_log
	def run(self):
		# instanziert DnDClassListFetcher
		self.load_base_class_datas()
		
		self.load_detaild_calss_datas()
		
	def load_detaild_calss_datas(self):
		tracker = ProgressTracker(len(self.class_ids), task_name="Load and Save 'Detail Class-data' for ")
		crud = CrudJsonFiles("../../static_dnd_data/all_classes.json")
		
		# lädt von 'all_classes.jons' die daten
		class_base_data = crud.data
		for class_name, indent in self.class_ids.items():
			
			# extrahiert die base data der jeweiligen Klasse
			base_data = class_base_data[indent]
			detail_data = ClassDetails(base_data, class_name)
			
			detail_data.initialize_all_data()
			
			enriched_detail_data = detail_data.initialize_all_details()
			
			file_name_list = [f"{class_name}_spells.json", f"{class_name}_levels_features.json",
			                  f"{class_name}_subclass(es).json"]
			
			for i, data in enumerate(enriched_detail_data):
				crud = CrudJsonFiles(f"../../static_dnd_data/detailed_class_data/{class_name}/{file_name_list[i]}")
				crud.check_path()
				crud.data = data
			
			tracker.update(message=f"-{class_name}")
	
	def load_base_class_datas(self):
		crud = CrudJsonFiles("../../static_dnd_data/all_classes.json")
		# reinigt 'all_classes.json' damit es nicht zu dopplungen kommt
		crud.reset()
		
		# wenn 'all_classes.json' nicht vollständig ist:
		fetcher = DnDClassUrlFetcher()
		
		# gets all urls for all classes, in a list
		# hier kommt raus:
		# ['https://www.dnd5eapi.co/api/2014/classes/barbarian', 'https://www.dnd5eapi.co/api/2014/classes/bard', ...
		class_urls = fetcher.get_class_urls()
		tracker = ProgressTracker(len(class_urls), task_name="Loading 'Base Class-data' for all classes")
		
		# lädt alle basis Klassen daten von der DnD5e-API und speichert sie in Json: 'all_classes.json'
		for i, url in enumerate(class_urls):
			char_class = DnDClassFetcher(url)
			char_class.load_and_save()
			# über self.classes wird dann später iteriert um die details zu erhalten
			
			tracker.update()
		tracker.done()
		
