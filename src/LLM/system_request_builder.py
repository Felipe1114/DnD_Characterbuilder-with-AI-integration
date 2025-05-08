"""Diese Klasse baut die Systemnachricht zusammen.
Sie analysiert den Prompt und kombiniert ihn mit den JSON-Daten.

Aufgabe:
erhält Klassen daten und umgeschriebenen User-Promt
Kombiniert alles zu einem “System Prompt”"""
from src.database.db_manager import DatabaseManager
from src.handle_data.character_data_loader import CharacterDataLoader, CLASS_INDICIES
from src.handle_data.crud_txt import CrudTxtFiles

class SystemRequestBuilder:
	def __init__(self, idea_id):
		self.idea_id = idea_id
		self.db_path = "sqlite:///../../data/db/dnd_db.sqlite" # TODO db_path könnte man noch in env file packen
		self.db = DatabaseManager(self.db_path)
		self.system_message_path = "../../debug_data/LLM_log/system_message_alpha_01.txt"
		self.crud_message = CrudTxtFiles(self.system_message_path)
		self.place_holder_keys = [
			"__PLACEHOLDER_LEVEL_FEATURES__",
			"__PLACEHOLDER_SPELLS__",
			"__PLACEHOLDER_SUBCLASS_DATA__"
			]
		self.data_loader = CharacterDataLoader()
		self.class_data_template_path = "../../static_dnd_data/detailed_class_data/all_class_data_template.txt"
		self.crud_template = CrudTxtFiles(self.class_data_template_path)
	
	def get_system_message_template(self):
		"""gets the System message-template from the local storage"""
		system_message = self.crud_message.data
		return system_message
	
	def get_class_data_template(self):
		"""gets class_data_template as text"""
		class_data_template = self.crud_template.data
		return class_data_template
		
	def load_char_prompts(self):
		"""gets char_ideas from database
		returns a dict with 3 different classes and rewirtten_user_prompts
		"""
		char_prompts = self.db.load_character_prompts(self.idea_id)
		
		char_prompt_dict = {
								"char_1": {
											"class": char_prompts["classes"][0],
											"key_descriptions": char_prompts["key_descriptions"],
											"rewritten_prompt": char_prompts["rewritten_prompt"[0]]
											},
								"char_2": {
											"class": char_prompts["classes"][0],
											"key_descriptions": char_prompts["key_descriptions"],
											"rewritten_prompt": char_prompts["rewritten_prompt"[0]]
											},
								"char_3": {
											"class": char_prompts["classes"][1],
											"key_descriptions": char_prompts["key_descriptions"],
											"rewritten_prompt": char_prompts["rewritten_prompt"[1]]
											},
								"char_4": {
											"class": char_prompts["classes"][2],
											"key_descriptions": char_prompts["key_descriptions"],
											"rewritten_prompt": char_prompts["rewritten_prompt"[2]]
											}
		}
		
		return char_prompt_dict
	
	def generate_system_prompts(self) -> list:
		"""creates a list with four system prompts. Each for a character.
		Each system prompt contains the system_prompt_template, the rewritten_prompt for each possible class
		and all necessary data for each class"""
		system_message_list = []
		char_prompt_dcit = self.load_char_prompts()
		
		# for each of the 4 characters
		for key, data in char_prompt_dcit.items():
			# loads a clean system_message template for each character
			system_message = self.get_system_message_template()
			
			# adds char_details to system_message with .replace()
			system_message = self.add_char_details(data, system_message)
			
			# adds class_data to system_message with .replace()
			system_message = self.add_class_data(system_message)
			
			# appends system_message to the system_message list
			system_message_list.append(system_message)
			
		return system_message_list
	
	# TODO hier müssen (über eine forlschleife?) die class_names eingefügt werden.
	def add_class_data(self, system_message):
		"""loads class_data and puts them all together in class_data_template"""
		# loads a template, where all class_data come together in a big string
		class_data_template = self.get_class_data_template()
		# sets the class_name in the data_loader Class -> nececary for loading the correct class
		self.data_loader.class_name = CLASS_INDICIES[self.idea_id] # TODO idea_id lädt nicht die classe!!!!
		# returns a list with all three class_data parts (level_features, spells, subclass_data)
		class_data = self.data_loader.class_data()
		# puts class_data in one big string
		for i, data in enumerate(class_data):
			class_data_template = class_data_template.replace(self.place_holder_keys[i], class_data[i])
		# replaces Placeholder: __ClassData__ with class_data_template
		system_message = system_message.replace("__ClassData__", class_data_template)
		return system_message
	
	def add_char_details(self, data, system_message):
		"""generates char_details and replaces the PlaceHolder in system_message with char_details"""
		char_details = f"Erstelle einen {data["rewritten_prompt"]}. Orientiere dich bei dem {data["class"]} an folgenden details: {data["key_descriptions"]}"
		system_message = system_message.replace("__RewrittenPrompt__", char_details)
		return system_message
		
	def run(self):
		"""casts generate_system_prompts and returns the prompt list"""
		prompt_list = self.generate_system_prompts()
		return prompt_list
		
			
			
		
		