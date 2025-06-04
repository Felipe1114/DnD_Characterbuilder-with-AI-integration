"""Diese Klasse baut die Systemnachricht zusammen.
Sie analysiert den Prompt und kombiniert ihn mit den JSON-Daten.

Aufgabe:
erhält Klassen daten und umgeschriebenen User-Promt
Kombiniert alles zu einem “System Prompt”"""
from src.database.db_manager import DatabaseManager
from src.handle_data.character_data_loader import CharacterDataLoader
from src.handle_data.crud_txt import CrudTxtFiles
from src.helper.debug_log import DebugLog
from src.helper.debug_helper import DebugHelper
from src.handle_data.env_loader import EnvLoader

# activates the DebugHelper

class SystemRequestBuilder:
	def __init__(self, idea_id):
		if isinstance(idea_id, int):
			self.idea_id = idea_id
		else:
			raise ValueError("idea_id has to be an integer")
		
		self.db = DatabaseManager()
		
		self.system_message_path = EnvLoader.system_message()
		self.crud_message = CrudTxtFiles(self.system_message_path)
		
		self.class_data_template_path = EnvLoader.all_class_data_template()
		self.crud_template = CrudTxtFiles(self.class_data_template_path)
		
		self.place_holder_keys = [
			"__PLACEHOLDER_BASE_DATA__",
			"__PLACEHOLDER_LEVEL_FEATURES__",
			"__PLACEHOLDER_SPELLS__",
			"__PLACEHOLDER_SUBCLASS_DATA__"
		]
		# sets the DebugHelber on or off
		DebugHelper.activ(activ=False)
	
	def get_system_message_template(self):
		"""gets the System message-template from the local storage"""
		system_message = self.crud_message.data
		
		return system_message
	
	def get_class_data_template(self):
		"""gets class_data_template as text"""
		class_data_template = self.crud_template.data
		
		DebugHelper.debug_print(
			data_description="class_data_template from: /Users/felipepietzsch/Masterschool/Ohne Titel/DnD_Characterbuilder-with-AI-integration/static_dnd_data/detailed_class_data/all_class_data_template.txt",
			data=class_data_template,
			active=False)
		
		return class_data_template
		
	def load_char_prompts(self):
		"""gets char_ideas from database
		returns a dict with 3 different classes and rewirtten_user_prompts
		
		char_prompts looks like this:
		
		"""
		# char_prompts is a dcitionary with informations for the character generation.
		# It looks like this:
		# 	{
		# 		'classes': classes_for_idea,  # -> three classes [class_1, class_2, class_3]
		# 		'key_descriptions': descriptions_for_idea,  # -> ["great", "big", "strong", "fire", ...]
		# 		'rewritten_prompts': rewritten_prompts  # -> ["a Paladin wich...", "a warlock wich...", "a wizard wich..."]
		# 	}
		char_prompts = self.db.load_character_prompts(self.idea_id)
		
		DebugHelper.debug_print(
			data_description="char_prompts, from the database; It should look like this:\n"
			                 "{\n"
				"'classes': [class_1, class_2, class_3]\n"
				"'key_descriptions': [great, big, strong, fire, ...]\n"
				"'rewritten_prompts': [a Paladin wich..., a warlock wich..., a wizard wich...]\n"
			                 "}\n",
			data=char_prompts,
			active=False)
		
		char_prompt_dict = {
								"char_1": {
											"class": char_prompts["classes"][0],
											"key_descriptions": char_prompts["key_descriptions"],
											"rewritten_prompt": char_prompts["rewritten_prompts"][0]
											},
								"char_2": {
											"class": char_prompts["classes"][0],
											"key_descriptions": char_prompts["key_descriptions"],
											"rewritten_prompt": char_prompts["rewritten_prompts"][0]
											},
								"char_3": {
											"class": char_prompts["classes"][1],
											"key_descriptions": char_prompts["key_descriptions"],
											"rewritten_prompt": char_prompts["rewritten_prompts"][1]
											},
								"char_4": {
											"class": char_prompts["classes"][2],
											"key_descriptions": char_prompts["key_descriptions"],
											"rewritten_prompt": char_prompts["rewritten_prompts"][2]
											}
		}
		
		return char_prompt_dict
	
	def generate_system_prompts(self) -> list:
		"""creates a list with four system prompts. Each for a character.
		Each system prompt contains the system_prompt_template, the rewritten_prompt for each possible class
		and all necessary data for each class"""
		system_message_list = []
		# char_prompt_dict enthält 1. classes 2. key_descriptions 3. rewritten_prompts
		char_prompt_dict = self.load_char_prompts()
		
		DebugHelper.debug_print(data_description="char_prompt_dict contains a dict with for dicts, with char_promt informations",
		                        data=char_prompt_dict,
		                        active=False)
		
		# for each of the 4 characters
		for key, data in char_prompt_dict.items():
			# loads a clean system_message template for each character
			system_message = self.get_system_message_template()
			
			DebugHelper.debug_print(
				data_description="unfilled system_message from: ../debug_data/LLM_log/system_message_alpha_01.txt\n"
				                 "This unfilled Template will be filled with more character information in the next steps",
				data=system_message,
				active=False)
			# adds char_details to system_message with .replace()
			system_message = self.add_char_details(data, system_message)
			
			DebugHelper.debug_print(
				data_description="system_message, filled with character_details bzw. system_promt: ../debug_data/LLM_log/system_message_alpha_01.txt\n",
				data=system_message,
				active=False)
			
			# adds class_data to system_message with .replace()
			system_message = self.add_class_data(data, system_message)
			
			DebugHelper.debug_print(
				data_description="system_message, filled with class_data: ../debug_data/LLM_log/system_message_alpha_01.txt\n",
				data=system_message,
				active=False)
			
			# appends system_message to the system_message list
			system_message_list.append(system_message)
		
		
		return system_message_list
	
	def add_class_data(self, char_idea_data, system_message):
		"""loads class_data and puts them all together in class_data_template"""
		# instanciate the CaracterDataLoader Class
		class_name = char_idea_data["class"]
		c_data_lodr = CharacterDataLoader(class_name=class_name)
		
		# gets the text template wehre all class_data(dicts) will be packed together
		class_data_template = self.get_class_data_template()
		# returns a list with all three class_data parts (level_features, spells, subclass_data)
		class_data = c_data_lodr.class_data()
		# puts class_data in class_data_template
		for i, data in enumerate(class_data):
			class_data_template = class_data_template.replace(self.place_holder_keys[i], str(class_data[i]))
		
		# replaces Placeholder in the System_message: __ClassData__ with class_data_template
		system_message = system_message.replace("__ClassData__", class_data_template)
		return system_message
	
	def add_char_details(self, data, system_message):
		"""generates char_details and replaces the PlaceHolder in system_message with char_details"""
		char_details = f"Erstelle einen {data["rewritten_prompt"]}. Orientiere dich bei dem {data["class"]} an folgenden details: {data["key_descriptions"]}"
		system_message = system_message.replace("__RewrittenPrompt__", char_details)
		return system_message
		
	@DebugLog.debug_log
	def run(self):
		"""casts generate_system_prompts and returns the prompt list"""
		prompt_list = self.generate_system_prompts()
		
		return prompt_list
		
			
			
		
		