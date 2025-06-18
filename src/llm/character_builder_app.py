"""

"""
from src.llm.system_request_builder import SystemRequestBuilder
from src.llm.talk_to_mistral import TalkToMistral
from src.database.db_manager import DatabaseManager
from src.helper.debug_helper import DebugHelper

class CharacterBuilderApp:
	"""generates a dnd character on base of rewritten-prompt and dnd_class data"""
	def __init__(self, idea_id):
		try:
			self.idea_id = int(idea_id)
		except ValueError as e:
			print(f"idea_id has to be an integer: {e}")
			
		
		self.db = DatabaseManager()
		self.system_builder = SystemRequestBuilder(idea_id)
		self.mistral = TalkToMistral()
		
		# sets the DebugHelber on or off
		DebugHelper.activ(activ=False)
		
	def generate_character_builder_prompts(self):
		"""returns a list of 4 character_builder_prompts"""
		character_prompt_list = self.system_builder.run()
		
		DebugHelper.debug_print(
			data_description="character_prompt_list, contains four system_messages for the llm.\n"
			                 "In this case the list contains the prompts for: conan the barbar, conan the barbar, conan the fighter, conan the ranger",
			data=character_prompt_list,
			active=False)
		
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
		
		DebugHelper.debug_print(data_description="character_prompt_list: eine liste mit 4 elementen, die jeweils einen genereirungspromt enthalten",
		                        data=character_prompt_list,
		                        active=True,
		                        store_data=True)
		
		for i, characater_prompt in enumerate(character_prompt_list):
			character = self.generate_character(characater_prompt)
			
			DebugHelper.debug_print(data_description="character_json: ein generierter character, umgewandelt in einen Json-string",
			                        data=character,
			                        active=False,
			                        store_data=True)
			
			character_list.append(character)
		
		DebugHelper.debug_print(data_description="character_list: should contain a list of characters as a json-string",
		                        data=character_list,
		                        active=False,
		                        store_data=False)
		
		# save character_json in db
		self.db.save_generated_characters(character_list, idea_id=self.idea_id)
		