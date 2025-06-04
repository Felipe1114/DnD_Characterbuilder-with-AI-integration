"""
prüft den characterbuilder prozess in prozeduralem code
"""
from sqlalchemy.exc import OperationalError
from src.llm.system_request_builder import SystemRequestBuilder
from src.llm.talk_to_mistral import TalkToMistral
from src.database.db_manager import DatabaseManager
from json import loads


try:
	system_builder = SystemRequestBuilder(1)
	mistral = TalkToMistral()
	# prompt list wird correct vom systemRequest manager geladen
	prompt_list = system_builder.run()
	
	# generate chars with generator
	
	mistral.ask(prompt_list[0])
	response = mistral.response()
	print(response)

	
	
	
except OperationalError as e:
	print("ERROR!!!")
	raise e