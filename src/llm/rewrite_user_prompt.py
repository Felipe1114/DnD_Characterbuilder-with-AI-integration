from src.llm.base_classes.talk_to_mistral import TalkToMistral
from src.database.db_manager import DatabaseManager
from src.helper.logger import Logger
from src.llm.system_messages import SYSTSEM_MESSAGE_FOR_REWRITE_USER_PROMPT

logger = Logger("llm")

class RewriteUserPrompt(TalkToMistral):
	def __init__(self, user_prompt, system_prompt_key: str= "prompt_alpha_3"):
		"""
		crud: the class, wich gets the prompt from the prompt file
		prompt_key: the key to geht the correct prompt from the prompt dict
		
		self.ask() und self.response() sind base-methods aus TalkToMistral
		"""
		logger.info(f"initialize RewriteUserPrompt")
		
		super().__init__()
		
		self.prompt_key = system_prompt_key # key for the system prompt
		logger.debug(f"intialize self.prompt_key as: {self.prompt_key}")
		
		self._user_prompt = user_prompt # prompt from user, with character idea
		logger.debug(f"initialize self._user_prompt as: {self._user_prompt}")
		
		self.db = DatabaseManager()
		
	def rewrite(self):
		"""asks the llm to rewrite the user prompt"""
		logger.info(f"rewrite user_prompt...")
		
		request = self.generate_request_prompt()
	
		self.ask(request)
		
		response = self.response()
		
		logger.info(f"rewriting user_prompt was succesfull")
		
		return response


	@property
	def prompt(self):
		"""returns prompt for llm"""
		logger.debug(f"return given userprompt: {self._user_prompt}")
		
		return self._user_prompt

	@prompt.setter
	def prompt(self, user_prompt):
		"""defines prompt for llm"""
		logger.debug(f"set user_prompt as: {user_prompt}")
		
		self._user_prompt = user_prompt


	def generate_request_prompt(self) -> str:
		"""generates the prompt for the request, out of the given system_prompt and the user_prompt"""
		logger.info(f"generate request prompt...")
		
		request: str = SYSTSEM_MESSAGE_FOR_REWRITE_USER_PROMPT
		logger.debug(f"request to llm is: {request}")
		
		request_prompt = request.replace("{PLACEHOLDER}", self._user_prompt)
		logger.debug(f"put self._user_prompt into request to llm; request is now: {request_prompt}")
		
		return request_prompt
	
