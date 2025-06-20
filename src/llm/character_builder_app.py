from src.llm.system_request_builder import SystemRequestBuilder
from src.llm.talk_to_mistral import TalkToMistral
from src.database.db_manager import DatabaseManager
from src.helper.logger import Logger
from fastapi import HTTPException

logger = Logger("llm")

class CharacterBuilderApp:
	"""generates a dnd character on base of rewritten-prompt and dnd_class data"""
	def __init__(self, user_prompt_id):
		try:
			self.user_prompt_id = int(user_prompt_id)
		except ValueError as e:
			raise HTTPException(status_code=400, detail=f"user_prompt_id: {user_prompt_id} is not valid: {e}")
		
		logger.info(f"initialize CharacterBuilderApp")
		
		self.db = DatabaseManager()
		self.system_builder = SystemRequestBuilder(user_prompt_id)
		self.mistral = TalkToMistral()
		
		logger.debug(f"initialized CharacterBuilderApp as: {__name__}")
		
	def generate_character_builder_prompts(self):
		"""returns a list of 4 character_builder_prompts"""
		logger.info(f"generate character builder prompts")
		
		character_prompt_list = self.system_builder.run()
		
		return character_prompt_list
	
	def generate_character(self, character_prompt):
		"""generates a chracter on base of a character_prompt"""
		logger.info(f"genearte charcter...")
		logger.debug(f"generate character from prompt: {character_prompt}")
		
		self.mistral.ask(character_prompt)
		response = self.mistral.response()
		
		return response
	
	def run(self):
		"""generates pompt list an loops over the list and creates for dnd characters"""
		logger.info(f"run CharcterBuilderApp")
		
		character_prompt_list = self.generate_character_builder_prompts()
		character_list = []
		
		logger.info(f"generating all characters...")
		for i, characater_prompt in enumerate(character_prompt_list):
			logger.debug(f"generating character with character_prompt: {character_list} from character_prompt_list: {character_prompt_list}; character_prompt nmbr: {i + 1}. of {len(character_prompt_list)}.")
			character = self.generate_character(characater_prompt)
			
			logger.debug(f"append created character to character_list")
			character_list.append(character)
		
		# save character_json in db
		self.db.save_generated_characters(character_list, user_prompt_id=self.user_prompt_id)
		