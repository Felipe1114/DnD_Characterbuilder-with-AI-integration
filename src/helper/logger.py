"""
how to use:

import class
>>> from src.helper.logger import Logger
instanciate class with module name
>>> logger = Logger(module="module_name")
possible module names:
- api
- db
- dnd_api
- llm
- tracker

with the five log-methods you can logg your stuff
Examples for using different log levels:

1. DEBUG:
   - Detailed information for developers
   - Typically used during development
   - Example: Debug information about database queries or API calls

2. INFO:
   - Important information about normal program flow
   - Example: Successful operations or important milestones

3. WARNING:
   - Warnings about unexpected but non-critical events
   - Example: Invalid user inputs or non-critical errors

4. ERROR:
   - Errors that prevent execution of specific operations
   - Example: Database errors or failed API calls

5. CRITICAL:
   - Severe errors that could crash the application
   - Example: Critical system errors or unrecoverable failures


# 1. DEBUG - Detailed debug information
logger.debug("Executing database query: SELECT * FROM characters WHERE user_prompt_id = %s", user_prompt_id)
logger.debug("API response received: %s", api_response, stack_info=True)  # With stack trace for debugging
logger.debug("Character generation parameters: %s", character_params)

# 2. INFO - Important program flow information
logger.info("Character generation started for user_prompt_id %s", user_prompt_id)
logger.info("Successfully loaded %d characters from database", len(characters))
logger.info("API call to DnD API completed successfully")

# 3. WARNING - Warnings about unexpected events
logger.warning("Invalid user input: %s is not a valid user_prompt_id", user_input)
logger.warning("Database query returned no results for user_prompt_id %s", user_prompt_id)
logger.warning("API response contains unexpected data: %s", api_response)

# 4. ERROR - Errors preventing operations
logger.error("Database access error: %s", str(e), exc_info=True)  # With exception information
logger.error("API call failed with status code %s", response.status_code)
logger.error("Character generation failed for user_prompt_id %s", user_prompt_id)

# 5. CRITICAL - Severe system errors
logger.critical("Failed to establish database connection: %s", str(e), exc_info=True)
logger.critical("Critical error: Server out of disk space!")
logger.critical("Terminating application due to critical error: %s", str(e))

"""
import logging
from logging.handlers import RotatingFileHandler
import os
from src.handle_data.env_loader import EnvLoader
from typing import Optional

LEVEL = {"DEBUG": logging.DEBUG,
          "INFO": logging.INFO,
          "WARNING": logging.WARNING,
          "ERROR": logging.ERROR,
          "CRITICAL": logging.CRITICAL}

MODULE = {"api": "api",
          "db": "db",
          "dnd_api": "dnd_api",
          "llm": "llm",
          "tracker": "tracker",
          "data_handler": "data_handler",
          "splitter": "splitter"}

class LogLevelSwitch:
	"""with this calss the logg-level can bet set for all log classes"""
	@staticmethod
	def set_level():
		return LEVEL["DEBUG"]	

class Logger:
	_initialized = False
	_general_handler = None  # Class attribute for general handler
	_module_handlers = {}  # Class attribute for modul specific handler
	
	log_level = LogLevelSwitch.set_level()
	def __init__(self, module: str):
		# is module aceptable
		if module not in MODULE:
			raise ValueError(
				f"'module' must be one of: {', '.join(MODULE.keys())}"
			)
		
		self.module = MODULE[module]
		self.log_dir = EnvLoader.log_dir()
		self._formatter = logging.Formatter(
			'%(asctime)s - %(name)s - %(levelname)s - %(message)s'
		)
		
		# initializes logging system, if not done yet
		if not Logger._initialized:
			self._initialize_logging()
			Logger._initialized = True
		
		# cerate logger
		self._logger = logging.getLogger(self.module)
		self._logger.setLevel(Logger.log_level)
		
		# adds handler, if not done yet
		self._add_handlers()
	
	def _initialize_logging(self):
		"""initializes the basic logging system, once"""
		i = 1
		print(f"initialize logging...\nbug_catch_message: if i:{i} is higher than '1', a bug is in logging mudule")
		i += 1
		# creates logging-dir, if it does not exist
		os.makedirs(self.log_dir, exist_ok=True)
		
		# konfigure logging-system
		logging.basicConfig(
			level=Logger.log_level,
			format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
			handlers=[logging.StreamHandler()]  # Standardmäßig auf stderr ausgeben
		)
		
		# creates general handler
		Logger._general_handler = RotatingFileHandler(
			f"{self.log_dir}/.log", maxBytes=8*1024*1024, backupCount=4
		)
		Logger._general_handler.setLevel(Logger.log_level)
		Logger._general_handler.setFormatter(self._formatter)
	
	def _add_handlers(self):
		"""adds module_handler to logger, if it does not exist"""
		# adds general_handler to handler, if it does not exist
		if Logger._general_handler not in self._logger.handlers:
			self._logger.addHandler(Logger._general_handler)
			print(f"'general_handler' was added to 'logger'")
		
		# create or gets module handler
		if self.module not in Logger._module_handlers:
			module_handler = RotatingFileHandler(filename=f"{self.log_dir}/{self.module}.log",
				maxBytes=5*1024*1024, backupCount=2
                )
			
			module_handler.setLevel(Logger.log_level)
			module_handler.setFormatter(self._formatter)
			# adds module_handler to module_handler dict
			Logger._module_handlers[self.module] = module_handler
			
			print(f"module_handler: '{self.module}' was added to module handler dictionar\n"
			      f"all module_handlers: {Logger._module_handlers}")
		
		# adds module_handler to logger, if it does not exist
		if Logger._module_handlers[self.module] not in self._logger.handlers:
			self._logger.addHandler(Logger._module_handlers[self.module])

	def debug(self, message: str, exc_info: Optional[bool] = None, stack_info: Optional[bool] = None):
		"""loggs debug-message"""
		self._logger.debug(message, exc_info=exc_info, stack_info=stack_info)
	
	def info(self, message: str):
		"""loggs info-message"""
		self._logger.info(message)
	
	def warning(self, message: str, exc_info: Optional[bool] = None, stack_info: Optional[bool] = None):
		"""loggs waring-message"""
		self._logger.warning(message, exc_info=exc_info, stack_info=stack_info)
	
	def error(self, message: str, exc_info: Optional[bool] = None, stack_info: Optional[bool] = None):
		"""loggs error-message"""
		self._logger.error(message, exc_info=exc_info, stack_info=stack_info)
	
	def critical(self, message: str, exc_info: Optional[bool] = None, stack_info: Optional[bool] = None):
		"""loggs critical-message"""
		self._logger.critical(message, exc_info=exc_info, stack_info=stack_info)
		
