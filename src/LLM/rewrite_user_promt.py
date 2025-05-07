"""Gegeben ist der folgende Nutzer-Prompt:
{user_prompt}

Finde die zu diesem Prompt am besten passenden Klassen aus folgender 'class_name' Liste:
- barbarian
- bard
- cleric
- druid
- fighter
- monk
- paladin
- ranger
- rogue
- sorcerer
- warlock
- wizard

Gib als Ergebnis ein JSON mit folgendem Format zurück:
{
"matched_classes": [best_class, second_best_class, thrid_best_class],
"keywords": [keywords aus user_prompt, die den character, seine Fähigkeiten und Eingeschaften beschreiben],
"rewritten_prompt_template": [umgeschriebene user_prompt mit best_class, umgeschriebener user_prompt mit second_best_clas, ...]
}

Beispiel:
user_prompt: "dunkler Magier, der tote beschwört und feuer Zauber beherrscht"
JSON rückgabe:
{
"matched_classes": ["wizard", "warlock", "cleric"],
"keywords": ["dunkel", "beschwörung", "feuer", "tote", "zauber"],
"rewritten_prompt_template": ["dunkler wizard, der tote beschwört und Feuerzauber beherrscht", "dunkler warlock, der tote beschwört und Feuerzauber beherrscht", "dunkler cleric', der tote beschwört und Feuerzauber beherrscht"]
}

"""
from src.LLM.talk_to_mistral import TalkToMistral
from src.handle_data.crud_json import CrudJsonFiles
from src.handle_data.algo.binary_dict import BinaryDict
from src.database.db_manager import DatabaseManager
from src.handle_data.llm_log_manager import LlmLogManager

class RewriteUserprompt(TalkToMistral):
	def __init__(self, user_prompt, system_prompt_key: str= "prompt_alpha_3"):
		"""
		crud: the class, wich gets the prompt from the prompt file
		prompt_key: the key to geht the correct prompt from the prompt dict
		
		self.ask() und self.response() sind base-methods aus TalkToMistral
		"""
		super().__init__()
		self.system_prompt_path = "../../debug_data/LLM_log/system_prompts_for_rewrite.json"
		self.prompt_crud = CrudJsonFiles(self.system_prompt_path)
		self.prompt_key = system_prompt_key # key for the system prompt
		self._user_prompt = user_prompt # prompt from user, with character idea
		self.db_path = "sqlite:///../../data/db/dnd_db.sqlite" # TODO db_path könnte man noch in env file packen
		self.db = DatabaseManager(self.db_path)
		self.log_mngr = LlmLogManager(self.prompt_key)
		
	def rewrite(self):
		"""fragt das LLM, den User-prompt umzuschreiben"""
		#user_prompt = user_prompt.strip() # definiert den user_prompt
		request = self.generate_request_prompt()
		# gibt Mistral den Auftrag den user_prompt umzuschreiben
		self.ask(request)
		
		# gibt die antwort von Mistral zurück
		respone = self.response()
		
		"""
		Log datei hat irgendein problem
		# speichert rewritten prompt in llm_log für die dokumentation und ds testing ab
		self.log_mngr.save_analysed_prompt(self._user_prompt, respone)
		"""
		return respone


	@property
	def prompt(self):
		return self._user_prompt

	@prompt.setter
	def prompt(self, user_prompt):
		"""definiert einen user-prompt"""
		self._user_prompt = user_prompt


	def generate_request_prompt(self) -> str:
		"""generates the prompt for the request, out of the given system_prompt and the user_prompt"""
		"""
		folgender fehler ist hier aufgetreten:
		
		request: str = self.prompt_crud.data[0][self.prompt_key]
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
		TypeError: list indices must be integers or slices, not str
		
		um den FEhler zu beheben werde ich den systemprompt hard coden
		"""
		
		#request: str = self.prompt_crud.data[0][self.prompt_key]
		request: str = "Gegeben ist der folgende Nutzer-Prompt:\\n{PLACEHOLDER}\\n\\nFinde die zu diesem Prompt am besten passenden Klassen aus folgender 'class_name' Liste:\\n- barbarian\\n- bard\\n- cleric\\n- druid\\n- fighter\\n- monk\\n- paladin\\n- ranger\\n- rogue\\n- sorcerer\\n- warlock\\n- wizard\\n\\nGib als Ergebnis ein JSON mit folgendem Format zurück:\\n{\\n\\\"matched_classes\\\": [best_class, second_best_class, thrid_best_class],\\n\\\"keywords\\\": [keywords aus user_promt, die den character, seine Fähigkeiten und Eingeschaften beschreiben],\\n\\\"rewritten_prompt_template\\\": [umgeschriebene user_prompt mit best_class, umgeschriebener user_promt mit second_best_clas, ...]\\n}\\n\\nBeispiel:\\nuser_promt: \\\"dunkler Magier, der tote beschwört und feuer Zauber beherrscht\\\"\\nJSON rückgabe:\\n{\\n\\\"matched_classes\\\": [\\\"wizard\\\", \\\"warlock\\\", \\\"cleric\\\"],\\n\\\"keywords\\\": [\\\"dunkel\\\", \\\"beschwörung\\\", \\\"feuer\\\", \\\"tote\\\", \\\"zauber\\\"],\\n\\\"rewritten_prompt_template\\\": [\\\"dunkler wizard, der tote beschwört und Feuerzauber beherrscht\\\", \\\"dunkler warlock, der tote beschwört und Feuerzauber beherrscht\\\", \\\"dunkler cleric', der tote beschwört und Feuerzauber beherrscht\\\"]\\n}\nGebe als Antwort nur das Json zurück. Keine erklärungen, oder kommentare. Keine ''' oder \"\"\" am Anfang oder Ende deiner antwort. Auch kein Json: oder json am Anfnag der Antwort. Nur das reine Json, das mit '{' beginnt und mit '}' endet.\n"
		
		request_prompt = request.replace("{PLACEHOLDER}", self._user_prompt)
		
		return request_prompt
	




if __name__ == "__main__":
	# crud für llm_log_analyse instanzieren
	llm_log_analysis_path = "../../debug_data/LLM_log/LLM_log_analyse.json"
	analyse_crud = CrudJsonFiles(llm_log_analysis_path)

	# holt die daten aus LLM_log_analyse.json
	analyse_data:list = analyse_crud.data

	# prompt key und user_prompt
	prompt_alpha_version = "prompt_alpha_3" # pormpt_alpha_version ist 'prompt_alpha_version' in BinaryDict
	user_prompt = "Eine Mischung aus: Valentine aus der Adamsfamilie und Calipso aus Fluch der Karibik"

	# analysiere user_prompt und füge ihn in system_prompt ein
	rewrite = RewriteUserprompt(user_prompt, system_prompt_key=prompt_alpha_version)
	rewritten_prompt = rewrite.rewrite()

	# finde passendes dict in analyse_data über binary_algo
	bnry_dct = BinaryDict(analyse_data, prompt_alpha_version)
	i_of_version_dict = bnry_dct.result()
	i = i_of_version_dict
	
	analyse_log_data = {
        "user_prompt": user_prompt,
        "answer": rewritten_prompt,
		"characters": None
	}

	# füge rewritten_prompt in analyse_data[i] ein
	analyse_data[i]["llm_answers"].append(analyse_log_data)

	# speichere neue analyse_data ab
	analyse_crud.reset()
	analyse_crud.data = analyse_data

	print(analyse_log_data)