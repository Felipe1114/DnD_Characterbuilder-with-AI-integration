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
from src.debug.debug_log import DebugLog
from src.debug.debug_helper import DebugHelper

DebugHelper.activ(activ=True)

class CharacterBuilderApp:
	""""""
	#TODO: in CharacterDataLoader muss noch der character name festgeelegt werden
	def __init__(self, idea_id):
		self.idea_id = idea_id
		self.db = DatabaseManager()
		self.system_builder = SystemRequestBuilder(idea_id)
		self.mistral = TalkToMistral()
		self.log_mngr = LlmLogManager()
		
	def generate_character_builder_prompts(self):
		"""returns a list of 4 character_builder_prompts"""
		character_prompt_list = self.system_builder.run()
		
		DebugHelper.debug_print(
			data_description="character_prompt_list, contains four system_messages for the LLM.\n"
			                 "In this case the list contains the prompts for: conan the barbar, conan the barbar, conan the fighter, conan the ranger",
			data=character_prompt_list,
			active=True)
		
		return character_prompt_list
	
	def generate_character(self, character_prompt):
		"""generates a chracter on base of a character_prompt"""
		self.mistral.ask(character_prompt)
		response = self.mistral.response()
		
		return response
	
	@DebugLog.debug_log
	def run(self):
		"""generates pompt list an loops over the list and creates for dnd characters"""
		character_prompt_list = self.generate_character_builder_prompts()
		character_list = []
		for i, characater_prompt in enumerate(character_prompt_list):
			character_json_string = self.generate_character(characater_prompt)
			# converts the string in a json-objekt
			
			DebugHelper.debug_print(data_description="character_json_string: einer von vier generierten charcteren",
			                        data=character_json_string,
			                        active=True,
			                        store_data=True)
		
			character_json = loads(character_json_string)
			
			DebugHelper.debug_print(data_description="character_json: ein generierter character, umgewandelt in einen Json-string",
			                        data=character_json,
			                        active=True,
			                        store_data=True)
			
			character_list.append(character_json)
			
		DebugHelper.debug_print(data_description="character_list: should contain a list of characters as a json-string",
		                        data=character_list,
		                        active=True,
		                        store_data=False)
		
		# saves character to llm_log für dekumentation and testing
		#self.log_mngr.save_character_to_llm_log(character_list)
		# save character_json in db
		self.db.save_generated_characters(character_list, idea_id=self.idea_id)
		
		# for i, char in enumerate(character_list):
		# 	print(f"\n=====================Character_{i+1}=========================\n")
		# 	print(char)
		# print("\nFour characters where generated and saved in database, as Json-objects")
		#