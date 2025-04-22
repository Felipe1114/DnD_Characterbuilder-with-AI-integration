"""Diese Klasse baut die Systemnachricht zusammen.
Sie analysiert den Prompt und kombiniert ihn mit den JSON-Daten.

Aufgabe:
erhält Klassen daten und umgeschriebenen User-Promt
Kombiniert alles zu einem “System Prompt”"""

from src.database.db_manager import DatabaseManager
from src.handle_data.crud_txt import CrudTxtFiles

class SystemRequestBuilder:
	def __init__(self, idea_id):
		self.idea_id = idea_id
		self.db_path = "db_path"
		self.db = DatabaseManager(self.db_path)
		self.system_message_path = "../../debug_data/LLM_log/system_message_alpha_01.txt"
		self.crud = CrudTxtFiles(self.system_message_path)
		self.get_class_data = ...
		
	
	def get_system_message_template(self):
		"""gets the System message-template from the local storage"""
		system_message = self.crud.data
		return system_message
	
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
	
	def generate_system_prompts(self):
		"""creates a list with four system prompts. Each for a character.
		Each system prompt contains the system_prompt_template, the rewritten_prompt for each possible class
		and all necessary data for each class"""
		system_message_with_char_prompt = []
		char_prompt_dcit = self.load_char_prompts()
		
		for key, data in char_prompt_dcit.items():
			char_details = f"Erstelle einen {data["rewritten_prompt"]}. Orientiere dich bei dem {data["class"]} an folgenden details: {data["key_descriptions"]}"
			# for each char a clean system_message_template
			system_message = self.get_system_message_template()
			# replaces Placeholder: __RewrittenPrompt__ with char_details
			system_message = system_message.replace("__RewrittenPrompt__", char_details)
			
			system_message_with_char_prompt.append(system_message)
			
		return system_message_with_char_prompt
			
		
		
			
			
		
		