from src.database.db_manager import DatabaseManager
from src.handle_data.character_data_loader import CharacterDataLoader
from src.handle_data.crud_txt import CrudTxtFiles
from src.handle_data.env_loader import EnvLoader
from src.helper.logger import Logger
from fastapi import HTTPException
from src.llm.system_messages import SYSTEM_MESSAGE_FOR_CHARACTER_GENERATION

logger = Logger("llm")

class SystemRequestBuilder:
	"""
	builds up final prompt for llm.
	Prompt contains system_message, rewritten_prompt and dnd_class_data
	"""
	def __init__(self, user_prompt_id):
		try:
			logger.info(f"initialize SystemRequestBuilder")
			
			if isinstance(user_prompt_id, int):
				self.user_prompt_id = user_prompt_id
				logger.debug(f"initialize self.idea_id as: {self.user_prompt_id}")
			else:
				logger.warning(f"idea_id has to be an integer; not: {user_prompt_id}")
				raise ValueError("idea_id has to be an integer")
			
			self.db = DatabaseManager()
			
			self.class_data_template_path = EnvLoader.all_class_data_template()
			logger.debug(f"initialize self.class_data_template_path as: {self.class_data_template_path}")
			self.crud_template = CrudTxtFiles(self.class_data_template_path)
			
			self.place_holder_keys = [
				"__PLACEHOLDER_BASE_DATA__",
				"__PLACEHOLDER_LEVEL_FEATURES__",
				"__PLACEHOLDER_SPELLS__",
				"__PLACEHOLDER_SUBCLASS_DATA__"
			]
			logger.debug(f"initialize self.place_holder_keys as: {self.place_holder_keys}")
			# sets the DebugHelber on or off
		
		except ValueError as e:
			logger.error(f"internal server error: {e}")
			raise HTTPException(status_code=500, detail=f"internal server error: {e}")

	def get_system_message_template(self):
		"""gets the System message-template from the local storage"""
		try:
			logger.info(f"get system message tempalte")
			system_message = SYSTEM_MESSAGE_FOR_CHARACTER_GENERATION
			logger.debug(f"system_message loaded as: {system_message}")
			
			return system_message
		
		except Exception as e:
			logger.warning(f"could not load system_message: {e}")
			raise HTTPException(status_code=500, detail=e)
		
	def get_class_data_template(self):
		"""gets class_data_template as text"""
		try:
			logger.info(f"get class data template")
			class_data_template = self.crud_template.data
			logger.debug(f"class_data_template loaded as: {class_data_template}")
			
			return class_data_template
		
		except Exception as e:
			logger.warning(f"could not get calss data template: {e}")
			raise HTTPException(status_code=500, detail=e)
		
	def load_char_prompts(self):
		"""gets char_ideas from database
		returns a dict with 3 different classes and rewirtten_user_prompts
		
		char_prompts looks like this:
		{
				'classes': classes_for_idea,  # -> three classes [class_1, class_2, class_3]
				'key_descriptions': descriptions_for_idea,  # -> ["great", "big", "strong", "fire", ...]
				'rewritten_prompts': rewritten_prompts  # -> ["a Paladin wich...", "a warlock wich...", "a wizard wich..."]
			}
		"""
		try:
			logger.info(f"load char prompts")
			char_prompts = self.db.load_character_prompts(self.user_prompt_id)
			
			char_prompt_dict = {
									"char_1": {
												"class": char_prompts["classes"][0],
												"key_descriptions": char_prompts["key_descriptions"],
												"rewritten_prompt": char_prompts["rewritten_prompts"][0]
												},
									"char_2": {
												"class": char_prompts["classes"][0],
												"key_descriptions": char_prompts["key_descriptions"],
												"rewritten_prompt": char_prompts["rewritten_prompts"][0]
												},
									"char_3": {
												"class": char_prompts["classes"][1],
												"key_descriptions": char_prompts["key_descriptions"],
												"rewritten_prompt": char_prompts["rewritten_prompts"][1]
												},
									"char_4": {
												"class": char_prompts["classes"][2],
												"key_descriptions": char_prompts["key_descriptions"],
												"rewritten_prompt": char_prompts["rewritten_prompts"][2]
												}
			}
			logger.debug(f"loaded char prompts as: {char_prompts} and packet it into the dict: {char_prompt_dict}")
			
			return char_prompt_dict
		
		except KeyError as e:
			logger.error(f"Error with Keys in dictionary 'char_prompt_dict': {e}")
			raise HTTPException(status_code=500, detail=f"Error with Keys in dictionary 'char_prompt_dict': {e}")
		
		except Exception as e:
			logger.error(f"Error with load_char_prompts: {e}")
			raise HTTPException(status_code=500, detail=f"Error with load_char_prompts: {e}")
	
	def generate_system_prompts(self) -> list:
		"""creates a list with four system prompts. Each for a character.
		Each system prompt contains the system_prompt_template, the rewritten_prompt for each possible class
		and all necessary data for each class"""
		try:
			logger.info(f"generate system prompts...")
			system_message_list = []
			# char_prompt_dict enthält 1. classes 2. key_descriptions 3. rewritten_prompts
			char_prompt_dict = self.load_char_prompts()
			# for each of the 4 characters
			for key, data in char_prompt_dict.items():
				# loads a clean system_message template for each character
				system_message = self.get_system_message_template()
				
				# adds char_details to system_message with .replace()
				system_message = self.add_char_details(data, system_message)
				
				# adds class_data to system_message with .replace()
				system_message = self.add_class_data(data, system_message)
				
				# appends system_message to the system_message list
				system_message_list.append(system_message)
			
			logger.info(f"genearte system prompt was succesfull")
			return system_message_list
		
		except Exception as e:
			logger.error(f"Error with generate_system_prompts: {e}")
			raise HTTPException(status_code=500, detail=f"Error with generate_system_prompts: {e}")
		
	def add_class_data(self, char_idea_data, system_message):
		"""loads class_data and puts them all together in class_data_template"""
		# instanciate the CaracterDataLoader Class
		try:
			logger.info(f"add class data")
			
			class_name = char_idea_data["class"]
			c_data_lodr = CharacterDataLoader(class_name=class_name)
			
			# gets the text template wehre all class_data(dicts) will be packed together
			class_data_template = self.get_class_data_template()
			# returns a list with all three class_data parts (level_features, spells, subclass_data)
			class_data = c_data_lodr.class_data()
			# puts class_data in class_data_template
			for i, data in enumerate(class_data):
				logger.debug(f"replace class_data template: {self.place_holder_keys[i]} with: {class_data[i]}\nreplace process {i +1}. of {len(class_data)}.")
				class_data_template = class_data_template.replace(self.place_holder_keys[i], str(class_data[i]))
			
			# replaces Placeholder in the System_message: __ClassData__ with class_data_template
			system_message = system_message.replace("__ClassData__", class_data_template)
			logger.debug(f"replace class_data_template in system_message with class_data: {class_data}")
			
			return system_message
		
		except TypeError as e:
			raise HTTPException(status_code=500, detail=f"Error with self.place_holder_keys; {e}")
		
		except Exception as e:
			raise HTTPException(status_code=500, detail=f"internal server error: {e}")
			
	def add_char_details(self, data, system_message):
		"""generates char_details and replaces the PlaceHolder in system_message with char_details"""
		logger.info(f"add char details...")
		
		char_details = f"Erstelle einen {data["rewritten_prompt"]}. Orientiere dich bei dem {data["class"]} an folgenden details: {data["key_descriptions"]}"
		logger.debug(f"create char_details-string: {char_details}")
		
		system_message = system_message.replace("__RewrittenPrompt__", char_details)
		logger.debug(f"sytem_message with details is: {system_message}")
		
		return system_message
		
	def run(self):
		"""calls generate_system_prompts and returns the prompt list"""
		logger.info(f"run SystemRequestBuilder...")
		prompt_list = self.generate_system_prompts()
		
		return prompt_list
		
			
			
		
		