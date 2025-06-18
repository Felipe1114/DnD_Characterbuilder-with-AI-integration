from src.dnd_api.class_url_fetcher import DnDClassUrlFetcher
from src.dnd_api.dnd_class_fetcher import DnDClassFetcher
from src.dnd_api.class_details import ClassDetails
from src.handle_data.crud_json import CrudJsonFiles
from src.handle_data.env_loader import EnvLoader
from src.helper.progress_tracker import ProgressTracker

"""
Note:
	1. after loading all data and detailed data, the progress tracker is showing an error. Why?
"""

class DnDApiManager:
	"""loads all DnD-class data from the DnD5e-API and saves it in a huge JSON file"""
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
		
		self.all_dnd_classes_path = EnvLoader.all_dnd_classes()
		self.detailed_class_data_path = EnvLoader.detailed_class_data_dir()
		
	def load_detaild_calss_datas(self):
		tracker = ProgressTracker(len(self.class_ids), task_name="Load and Save 'Detail Class-data' for ")
		
		crud = CrudJsonFiles(self.all_dnd_classes_path)
		
		# loads data from 'all_classes.json'
		class_base_data = crud.data
		
		# extract the base_data for each dnd class
		for class_name, indent in self.class_ids.items():
			
			base_data = class_base_data[indent]
			
			detail_data = ClassDetails(base_data, class_name)
			
			detail_data.initialize_all_data()
			
			enriched_detail_data = detail_data.initialize_all_details()
			
			file_name_list = [f"{class_name}_spells.json", f"{class_name}_levels_features.json",
			                  f"{class_name}_subclass(es).json"]
			
			for i, data in enumerate(enriched_detail_data):
				
				crud = CrudJsonFiles(f"{self.detailed_class_data_path}/{class_name}/{file_name_list[i]}")
				
				crud.check_path()
				crud.data = data
			
			tracker.update(message=f"-{class_name}")
	
	def load_base_class_datas(self):
		"""Loads the base datas for all dnd_classes from the DnD5e-api"""
		# instanciates crud and fetcher
		crud = CrudJsonFiles(self.all_dnd_classes_path)
		fetcher = DnDClassUrlFetcher()

		# cleans up 'all_classes.json' so their will be no doubles
		crud.reset()
		
		# gets all urls for all classes, in a list
		class_urls = fetcher.get_class_urls()
		
		tracker = ProgressTracker(len(class_urls), task_name="Loading 'Base Class-data' for all classes")
		
		# loads all base_class data for all 12 dnd classes and saves them in a
		for i, url in enumerate(class_urls):
			char_class = DnDClassFetcher(url)
			char_class.load_and_save()
			
			tracker.update()
		
		tracker.done()
		
	@DebugLog.debug_log
	def run(self):
		# load base_data
		self.load_base_class_datas()
		
		# load details for base_data
		self.load_detaild_calss_datas()
	
