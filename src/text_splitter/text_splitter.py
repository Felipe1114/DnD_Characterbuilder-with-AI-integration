from sympy.physics.units import length

from src.helper.logger import Logger
from src.handle_data.crud_txt import CrudTxtFiles
from textwrap import wrap

logger = Logger("splitter")

class TextSplitter:
	def __init__(self, dir_path, file_name, split_um: int=4):
		"""
		dir_path: the path to the dir in wich the text files will be stored
		file_name: the 'base' name of the splitted files;
		when file_name is: 'foo_bar' the file_names in the saving process will be: 'foo_bar_1, foo_bar_2, ...'
		split_num: in how many parts the main text should be splitted
		"""
		self._split_um = split_um
		
		self.dir_path = dir_path
		self.file_name = file_name
		self.data_path = f"{dir_path}/{self.file_name}"
		self.crud_txt = CrudTxtFiles(self.data_path)

		logger.info(f"initialize TextSplitter")
		
	def splitup(self, text: str):
		"""snipps text into smaller pieces and saves it into a file"""
		try:
			if not text:
				logger.warning(f"text has no value")
				raise ValueError("argument 'text' is empty")
			
			else:
				logger.info(f"start splitting text")
				lenght = len(text)
				logger.debug(f"leght of text is: {length}")
				split_num = lenght // self._split_um
				logger.debug(f"text is splitted in '{self._split_um}' files, with each '{split_num}' characters")
				
				logger.debug(f"start splitting text...")
				splitted_txt = wrap(text, width=split_num, fix_sentence_endings=True)
				logger.debug(f"splitting text sucessfull")

				for i, txt in enumerate(splitted_txt):
					logger.info(f"saving splitted text´s in files")
					self.crud_txt.data_path = f"{self.dir_path}/{self.file_name + '_' + str(i+1)}.txt"
					logger.debug(f"file_path {i + 1}: {self.crud_txt.data_path}")
					
					logger.debug(f"start saving text")
					self.crud_txt.data = txt
					
		except ValueError as e:
			logger.error(f"{e}")
			raise ValueError(e)
			
		except Exception as e:
			logger.error(f"{e}")
			raise Exception(e)
			
			
			
			
			