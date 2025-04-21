"""Diese Klasse baut die Systemnachricht zusammen.
Sie analysiert den Prompt und kombiniert ihn mit den JSON-Daten.

Aufgabe:
erhält Klassen daten und umgeschriebenen User-Promt
Kombiniert alles zu einem “System Prompt”"""
from src.LLM.rewrite_user_promt import RewriteUserprompt
from src.handle_data.crud_json import CrudJsonFiles

class SystemRequestBuilder:
	def __init__(self, user_prompt: str):
		self.rewrite = RewriteUserprompt(user_prompt)
		self.system_message_path = "../../debug_data/LLM_log/system_message_alpha_01.txt"
		self.crud = CrudJsonFiles(self.system_message_path)
		
	def generate_rewritten_prompt(self):
		"""generiert den umgeschriebenen Prompt aus dem user_prompt
		dieser Prompt wird din die System_message eingefügt"""
		rewritten_prompt = self.rewrite.rewrite()
		return rewritten_prompt
	
	def get_system_message(self):
		"""gets the System message from the local storage"""
		
	# hier weiter machen mit zusammenführen und erstellen des system-prompts
	