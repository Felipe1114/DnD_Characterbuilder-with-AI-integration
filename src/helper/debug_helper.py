"""This Class helps me, with my debugging.

It prints - if activated - given data in the terminal und gives info, what data it is"""

import inspect
from src.handle_data.crud_json import CrudJsonFiles

class DebugHelper:
	"""prints data for checking erros in files"""
	@staticmethod
	def activ(activ: bool=True):
		"""sets the DebugHelper activ oder inaktiv
		
		can be put on top on a code-file in outerscope, to activate oder deactivate the DebugHelper
		"""
		try:
			# checks, if input is a bool
			if isinstance(activ, bool):
				return activ
			
			raise ValueError("Argument for DebugHelper.active has to be a bool!")
			
		except ValueError as e:
			print(e)
			return False
		
	@staticmethod
	def debug_print(data_description: str, data, active: bool=True, data_type: bool=False, store_data: bool=False):
		"""prints given data and the meta data, where the data come from, like:
		file_name and line_number
		"""
		
		# if DebugHelper is activeted
		if DebugHelper.activ() and active:
			# create a frame for the file
			
			frame = inspect.currentframe()
			try:
				# where did the printet data came from?
				caller_frame = frame.f_back
				if caller_frame is not None:
					# Hole den Dateinamen und die Zeilennummer
					file_name = caller_frame.f_code.co_filename
					line_number = caller_frame.f_lineno
					# Gib die Debug-Informationen aus
					print(f"------------------------------------------------------------------------------------------------------------------------------------------------------\n"
					      f"Debug: {file_name}, line {line_number}: ")
			finally:
				# Wichtig: Lösche den Frame, um Speicherlecks zu vermeiden
				del frame
			
			# Führe den eigentlichen Print aus
			print(f"data description:\n {data_description}; \n")
			
			# if the data_type should also be printed
			if data_type:
				print(f"data_type: {type(data)}")
			
			print(f"data:\n {data}\n")
			      
			
			if store_data:
				DebugHelper._store_data(data, data_description, data_type)
			
			print("------------------------------------------------------------------------------------------------------------------------------------------------------")
	
	@staticmethod
	def _store_data(data, data_description, data_type):
		"""if the data should be testet in a nother file or stored for documentation"""
		from datetime import datetime
		
		# instantiate CrudJsonFiles-class for storing data
		j_crud = CrudJsonFiles("/data/debug_data/data_for_testing/data_for_testing.json")
		
		# if data_type is necesary:
		if data_type:
			type_of_data = type(data)
		else:
			type_of_data = "not specified"
			
		# create meta-data for data
		frame = inspect.currentframe()
		caller_frame = frame.f_back
		file_name = caller_frame.f_code.co_filename
		line_number = caller_frame.f_lineno
		date_and_time = datetime.now()
		
		# create dict
		data_dict = {"meta_data": f"Date and Time:{date_and_time},\nData from file:{file_name}, line {line_number}",
		             "data_description": data_description,
		             "data_type": str(type_of_data),
		             "data": data}
		
		# store dict
		j_crud.data = data_dict
		
		# print, that data was stored
		print("\ndata was saved in 'data_for_testing.json' for further testing tasks\n")