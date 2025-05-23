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
from scipy.optimize import brent

from src.LLM.talk_to_mistral import TalkToMistral
from src.handle_data.CRUD import CRUD
from src.handle_data.algo.binary_dict import BinaryDict

class RewriteUserprompt(TalkToMistral):
	def __init__(self, user_prompt, prompt_key: str="prompt_alpha_3"):
		"""
		crud: the class, wich gets the prompt from the prompt file
		prompt_key: the key to geht the correct prompt from the prompt dict
		"""
		super().__init__()
		self.llm_log_prompt_path = "../../debug_data/LLM_log/LLM_log_prompt.json"
		self.prompt_crud = CRUD(self.llm_log_prompt_path)
		self.prompt_key = prompt_key
		self._user_prompt = user_prompt

	def rewrite(self):
		"""fragt das LLM, den User-prompt umzuschreiben"""
		#user_prompt = user_prompt.strip() # definiert den user_prompt
		request = self.generate_request_prompt()
		# gibt Mistral den Auftrag den user_prompt umzuschreiben
		self.ask(request)
		
		# gibt umgeschriebenen user_prompt zurück
		return self.response()


	@property
	def prompt(self):
		return self._user_prompt

	@prompt.setter
	def prompt(self, user_prompt):
		"""definiert einen user-prompt"""
		self._user_prompt = user_prompt


	def generate_request_prompt(self) -> str:
		"""generates the prompt for the request, out of the given system_prompt and the user_prompt"""
		request: str = self.prompt_crud.data[self.prompt_key]
		
		request_prompt = request.replace("{PLACEHOLDER}", self._user_prompt)
		
		return request_prompt




if __name__ == "__main__":
	# crud für llm_log_analyse instanzieren
	llm_log_analysis_path = "../../debug_data/LLM_log/LLM_log_analyse.json"
	analyse_crud = CRUD(llm_log_analysis_path)
	
	# holt die daten aus LLM_log_analyse.json
	analyse_data:list = analyse_crud.data
	
	# prompt key und user_prompt
	prompt_alpha_version = "prompt_alpha_3" # pormpt_alpha_version ist 'prompt_alpha_version' in BinaryDict
	user_prompt = "Aang aus 'Avatar - the last airbender'"
	
	# analysiere user_prompt und füge ihn in system_prompt ein
	rewrite = RewriteUserprompt(user_prompt, prompt_key=prompt_alpha_version)
	rewritten_prompt = rewrite.rewrite()
	
	# finde passendes dict in analyse_data über binary_algo
	bnry_dct = BinaryDict(analyse_data, prompt_alpha_version)
	i_of_version_dict = bnry_dct.result()
	i = i_of_version_dict
	
	analyse_log_data = {
        "user_prompt": user_prompt,
        "answer": rewritten_prompt
	}
 
	# füge rewritten_prompt in analyse_data[i] ein
	analyse_data[i]["llm_answers"].append(analyse_log_data)
	
	# speichere neue analyse_data ab
	analyse_crud.reset()
	analyse_crud.data = analyse_data

	print(analyse_log_data)