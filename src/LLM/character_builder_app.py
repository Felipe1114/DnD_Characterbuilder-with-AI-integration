"""	fungiert als LLM-main
kombiniert
- Class CharacterRequestBuilder
- Class TalkToMistral


kombiniert alles und gibt das - von dem LLM - erstelle Character Json zurück.

"""
from xml.sax import parse

from src.LLM.system_request_builder import SystemRequestBuilder
from src.LLM.talk_to_mistral import TalkToMistral
from src.database.db_manager import DatabaseManager
from json import loads
from src.handle_data.llm_log_manager import LlmLogManager
from src.handle_data.env_loader import EnvLoader


class CharacterBuilderApp:
	""""""
	#TODO: in CharacterDataLoader muss noch der character name festgeelegt werden
	def __init__(self, idea_id):
		self.idea_id = idea_id
		self.db_path = EnvLoader.db_path()
		self.db = DatabaseManager(self.db_path)
		self.system_builder = SystemRequestBuilder(idea_id)
		self.mistral = TalkToMistral()
		self.log_mngr = LlmLogManager()
		
	def generate_character_builder_prompts(self):
		"""returns a list of 4 character_builder_prompts"""
		character_prompt_list = self.system_builder.run()
		return character_prompt_list
	
	def generate_character(self, character_prompt):
		"""generates a chracter on base of a character_prompt"""
		self.mistral.ask(character_prompt)
		response = self.mistral.response()
		
		return response
	
	def run(self):
		"""generates pompt list an loops over the list and creates for dnd characters"""
		character_prompt_list = self.generate_character_builder_prompts()
		character_list = []
		for i, characater_prompt in enumerate(character_prompt_list):
			charcter_json_string = self.generate_character(characater_prompt)
			# converts the string in a json-objekt
			character_json = loads(charcter_json_string)
			character_list.append(character_json)
		
		# saves character to llm_log für dekumentation and testing
		#self.log_mngr.save_character_to_llm_log(character_list)
		# save character_json in db
		self.db.save_generated_characters(character_list, idea_id=self.idea_id)
		
		for i, char in enumerate(character_list):
			print(f"\n=====================Character_{i+1}=========================\n")
			print(char)
		print("\nFour characters where generated and saved in database, as Json-objects")
		