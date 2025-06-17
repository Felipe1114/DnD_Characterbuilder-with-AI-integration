from mistralai import Mistral
from mistral.exceptions import InvalidActionException, NotAllowedException
from src.handle_data.env_loader import EnvLoader
from fastapi import HTTPException

env_loader = EnvLoader()
MISTRAL_KEY = EnvLoader.mistral_key()

class TalkToMistral:

	def __init__(self):
		# calls mistral api: https://docs.mistral.ai/getting-started/models/models_overview/
		self.model = "mistral-small-latest"

		self.client = Mistral(api_key=MISTRAL_KEY)
		
		self._mistral_response = None

	def ask(self, promt: str, user: str="user"):
		"""
		sends a request to miestral api
		"""
		try:
			mistral_small_response = self.client.chat.complete(
				model=self.model,
				messages=[{"role": user, "content": f"{promt}"}]
			)
			
			self._mistral_response = mistral_small_response
		except InvalidActionException as e:
			raise HTTPException(status_code=400, detail=f"Error with Mistral-LLM:{e}")
		
		except NotAllowedException as e:
			raise HTTPException(status_code=403, detail=f"Action is not allowed!!!: {e}")
		
		except Exception as e:
			raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
		
	def response(self) -> str:
		"""returns response of mistral api.
		if no request was set, the default message is:
		    "You did not ask anything. Please make a question!"
		"""
		if not self._mistral_response:
			raise HTTPException(status_code=404, detail="can not find 'response' to request, cause nothing was asked before.")
			
		return self._mistral_response.choices[0].message.content
  

















