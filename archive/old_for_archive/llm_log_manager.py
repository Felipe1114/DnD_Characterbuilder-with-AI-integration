from src.handle_data.crud_json import CrudJsonFiles

class LlmLogManager:
	def __init__(self, prompt_version="prompt_alpha_3"):
		self.llm_log_path = "../../debug_data/LLM_log/LLM_log_analyse.json"
		self.crud_j = CrudJsonFiles(self.llm_log_path)
		self.prompt_version = prompt_version
		self.user_prompt = None
		
	def load_log_data(self):
		"""gets the llm_log data"""
		data = self.crud_j.data
		return data
	
	def save_character_to_llm_log(self, character_list):
		"""saves all characters into the llm_log file"""
		character_dict = {}
		
		# creates a dictionary with all four characters
		for i, character in enumerate(character_list):
			char_key = f"character_{i}"
			character_dict[char_key] = character
		
		self._save_characters(character_dict)
	
	def _save_characters(self, character_dict):
		"""loads log_data, inserts characters into last prompt and saves new data to log"""
		log_data = self.load_log_data()
		for i, data in enumerate(log_data[0]):
			
			# finds correct dict on base of prompt_version
			if data[i]["prompt_generation"] == self.prompt_version:
				
				for j, dict in enumerate(data[i]["llm_answers"]):
					
					# finds correct dict on base of user_prompt
					if dict["user_prompt"] == self.user_prompt:
						log_data[0][i]["llm_answers"][j]["characters"] = character_dict
						
		self.crud_j.reset()
		self.crud_j.data = log_data
		
	def set_user_prompt(self, new_user_prompt: str):
			"""defines self.user_prompt"""
			self.user_prompt = new_user_prompt
	
	def save_analysed_prompt(self, user_prompt, rewritten_prompt):
		"""saves the analysed user prompt to llm_log"""
		analyse_log_data = {
			"user_prompt": user_prompt,
			"answer": rewritten_prompt,
			"characters": None
		}
		
		log_data = self.load_log_data()
		for i, data in enumerate(log_data):
			# finds correct dict on base of prompt_version
			if data[i]["prompt_generation"] == self.prompt_version:
				# fügt neues analysiertes prompt an
				log_data[-1][i]["llm_answers"].append(analyse_log_data)
		
		self.crud_j.reset()
		self.crud_j.data = log_data