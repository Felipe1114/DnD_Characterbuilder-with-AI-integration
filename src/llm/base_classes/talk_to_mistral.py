from mistralai import Mistral
from mistral.exceptions import InvalidActionException, NotAllowedException
from src.handle_data.env_loader import EnvLoader
from fastapi import HTTPException
from src.helper.logger import Logger

logger = Logger("llm")

env_loader = EnvLoader()
MISTRAL_KEY = EnvLoader.mistral_key()

class TalkToMistral:

	def __init__(self):
		
		# calls mistral api: https://docs.mistral.ai/getting-started/models/models_overview/
		self.model = "mistral-small-latest"
		
		self.client = Mistral(api_key=MISTRAL_KEY)
		
		self._mistral_response = None
		
		logger.info(f"initialize TalkToMistral with model: {self.model}")
		
	def ask(self, promt: str, user: str="user"):
		"""
		sends a request to miestral api
		"""
		try:
			logger.info(f"request to mistral api...")
			
			mistral_small_response = self.client.chat.complete(
				model=self.model,
				messages=[{"role": user, "content": f"{promt}"}]
			)
			logger.debug(f"response from mistral is: {mistral_small_response}" )
			
			self._mistral_response = mistral_small_response
			logger.info(f"mistral responded")
			
		except InvalidActionException as e:
			logger.error(f"Error with mistral-LLM: {e}")
			raise HTTPException(status_code=400, detail=f"Error with Mistral-LLM:{e}")
		
		except NotAllowedException as e:
			logger.error(f"prompt was out of policy!: {e}")
			raise HTTPException(status_code=403, detail=f"Action is not allowed!!!: {e}")
		
		except Exception as e:
			logger.error(f"Internal server error: {e}")
			raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
		
	def response(self) -> str:
		"""returns response of mistral api.
		if no request was set, the default message is:
		    "You did not ask anything. Please make a question!"
		"""
		if not self._mistral_response:
			logger.warning(f"can not find 'response' from mistral, cause nothing was asked before.")
			raise HTTPException(status_code=404, detail="can not find 'response' to request, cause nothing was asked before.")
			
		return self._mistral_response.choices[0].message.content
  

















