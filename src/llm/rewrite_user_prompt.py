from src.llm.talk_to_mistral import TalkToMistral
from src.database.db_manager import DatabaseManager
from src.handle_data.crud_txt import CrudTxtFiles
from src.handle_data.env_loader import EnvLoader
from src.helper.logger import Logger

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
		self.system_message_path = EnvLoader.system_message()
		logger.debug(f"initialize self.system_message_path as: {self.system_message_path}")
		self.crud_message = CrudTxtFiles(self.system_message_path)
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
		
		request: str = "Gegeben ist der folgende Nutzer-Prompt:\\n{PLACEHOLDER}\\n\\nFinde die zu diesem Prompt am besten passenden Klassen aus folgender 'class_name' Liste:\\n- barbarian\\n- bard\\n- cleric\\n- druid\\n- fighter\\n- monk\\n- paladin\\n- ranger\\n- rogue\\n- sorcerer\\n- warlock\\n- wizard\\n\\nGib als Ergebnis ein JSON mit folgendem Format zurück:\\n{\\n\\\"matched_classes\\\": [best_class, second_best_class, thrid_best_class],\\n\\\"keywords\\\": [keywords aus user_promt, die den character, seine Fähigkeiten und Eingeschaften beschreiben],\\n\\\"rewritten_prompt_template\\\": [umgeschriebene user_prompt mit best_class, umgeschriebener user_promt mit second_best_clas, ...]\\n}\\n\\nBeispiel:\\nuser_promt: \\\"dunkler Magier, der tote beschwört und feuer Zauber beherrscht\\\"\\nJSON rückgabe:\\n{\\n\\\"matched_classes\\\": [\\\"wizard\\\", \\\"warlock\\\", \\\"cleric\\\"],\\n\\\"keywords\\\": [\\\"dunkel\\\", \\\"beschwörung\\\", \\\"feuer\\\", \\\"tote\\\", \\\"zauber\\\"],\\n\\\"rewritten_prompt_template\\\": [\\\"dunkler wizard, der tote beschwört und Feuerzauber beherrscht\\\", \\\"dunkler warlock, der tote beschwört und Feuerzauber beherrscht\\\", \\\"dunkler cleric', der tote beschwört und Feuerzauber beherrscht\\\"]\\n}\nGebe als Antwort nur das Json zurück. Keine erklärungen, oder kommentare. Keine ''' oder \"\"\" am Anfang oder Ende deiner antwort. Auch kein Json: oder json am Anfnag der Antwort. Nur das reine Json, das mit '{' beginnt und mit '}' endet.\n"
		logger.debug(f"request to llm is: {request}")
		
		request_prompt = request.replace("{PLACEHOLDER}", self._user_prompt)
		logger.debug(f"put self._user_prompt into request to llm; request is now: {request_prompt}")
		
		return request_prompt
	
