from mistralai import Mistral
from src.handle_data.env_loader import EnvLoader

env_loader = EnvLoader()
MISTRAL_KEY = EnvLoader.mistral_key()

class TalkToMistral:

	def __init__(self):
		# greif auf 'mistral_small' zurück link: https://docs.mistral.ai/getting-started/models/models_overview/
		self.model = "mistral-small-latest"

		self.client = Mistral(api_key=MISTRAL_KEY)
		
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
  

















