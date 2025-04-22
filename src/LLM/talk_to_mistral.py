from mistralai import Mistral
from src.handle_data.env_loader import EnvLoader

env_loader = EnvLoader()
MISTRAL_KEY = env_loader.get_mistral_api_key()

class TalkToMistral:

	def __init__(self):
		# greif auf 'mistral_small' zurück link: https://docs.mistral.ai/getting-started/models/models_overview/
		self.model = "mistral-small-latest"
		# TODO api key muss aus env_loader kommen!!!!!!!!!!!!
		self.client = Mistral(api_key="EBBtyAxkHIZOWJcTz3AzsTH0xyDKcDKt")
		
		self._mistral_response = None

	def ask(self, promt: str, user: str="user"):
		"""
		schickt eine frage an Mistral_small_api und gibt die antwort zruück
		"""
		mistral_small_response = self.client.chat.complete(
			model=self.model,
			messages=[{"role": user, "content": f"{promt}"}]
		)
		
		self._mistral_response = mistral_small_response

	def response(self) -> str:
		"""Gibt die anwort von Mistral_small zurück; falls keine antwort zwischen gespeichert ist.
		wird ausgegeben: 'You did not ask anything. Please make a question!'"""
		if not self._mistral_response:
			return "You did not ask anything. Please make a question!"
		
		return self._mistral_response.choices[0].message.content
  
	def send_file(self, file_path: str, message: str, custom_filename: str = None, user: str = "user"):
		"""
		Lädt eine Datei hoch und sendet sie zusammen mit einer Nachricht an die Mistral-API.
		"""
		try:
			with open(file_path, 'rb') as file:
				file_content = file.read()
	   
			files = {
				"file": (custom_filename if custom_filename else file_path, file_content)
			}
	  
			mistral_small_response = self.client.chat.complete(
				model=self.model,
				messages=[{"role": user, "content": message}],
				files=files
			)
			self._mistral_response = mistral_small_response
   
		except FileNotFoundError:
			return "File not found. Please check the file path."
		except Exception as e:
			return f"An error occurred: {e}"

	# noch nicht definiert
    def system_message(self):
		"""erklärt dem LLM, was es genau mit den erhaltenen daten machen soll"""
		...

















