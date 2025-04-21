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
		
	
	def get_system_message(self):
		"""gets the System message from the local storage"""
		system_message = self.crud.data
		return system_message
	
	def load_char_prompts(self):
		"""gets char_ideas from database
		returns a dict with 3 different classes and rewirtten_user_prompts
		"""
		char_prompts = self.db.load_character_prompts(self.idea_id)
		# TODO bereite daten so auf, dass man einfach über sie iterieren kann
		"""
		dieses dict :
		{
			'classes': classes_for_idea,
			'key_descriptions': descriptions_for_idea,
			'rewritten_prompts': rewritten_prompts
		}
		
		soll in diese struktur überführt werden:
		{
			char_1: {"class": class_1, "key_descriptions": [key_descriptions], "rewritten_prompt": rewritten_prompt},
			char_2: {"class": class_1, "key_descriptions": [key_descriptions], "rewritten_prompt": rewritten_prompt},
			char_3: {"class": class_2, "key_descriptions": [key_descriptions], "rewritten_prompt": rewritten_prompt},
			char_4: {"class": class_3, "key_descriptions": [key_descriptions], "rewritten_prompt": rewritten_prompt}
			}
		"""
		return char_prompts
	
	def generate_system_prompt(self):
		"""puts rewritten_prompt and system_message to system_prompt together"""
		"""
		es sollen vier charactere generiert werden.
		Aus der datenbank kommt ein dict, mit jeweils drei unterschiedlichen classen und rewritten_prompts
		
		es muss eine for-schleife (4 mal) geschrieben werden, die 4 charactere auf basis der classen und rewritten prompts erstellt
		class_list = [class_1, class_2, class_3]
		character aufteilung: 2x class_1, 1x class_2, 1x class_3
			->  system_messages = []
				for i in range(4):
					if i <= 1:
						system_messages.append(generieree system_message für class_list[0])
					else:
						system_messages.append(generieree system_message für class_list[i-1])
					
		"""
		system_message = self.get_system_message()
		
		#TODO hier muss vieleicht mit "yield" gearbeitet werden, da es ja drei system messages gibt, die ausgegeben werden sollen
		
		