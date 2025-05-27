import inspect


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
	def debug_print(*args, **kwargs):
		"""prints given data and the meta data, where the data come from, like:
		file_name and line_number
		"""
		
		# if DebugHelper is activeted
		if DebugHelper.activ():
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
					print(f"Debug: {file_name}, line {line_number}: ", end="")
			finally:
				# Wichtig: Lösche den Frame, um Speicherlecks zu vermeiden
				del frame
			
			# Führe den eigentlichen Print aus
			print(*args, **kwargs)
