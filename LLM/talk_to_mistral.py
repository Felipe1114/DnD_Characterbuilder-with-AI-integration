from mistralai import Mistral
from env_loader import EnvLoader

env_loader = EnvLoader()
MISTRAL_KEY = env_loader.get_mistral_api_key()

class TalkToMistral:

    def __init__(self):
        # greif auf 'mistral_small' zurück link: https://docs.mistral.ai/getting-started/models/models_overview/
        self.model = "mistral-small-latest"
        self.client = Mistral(api_key=MISTRAL_KEY)

        self.mistral_response = None

    def ask(self, promt):
        """
        schckt eine frage an Mistral_small_api und gibt die antwort zruück
        """
        mistral_small_response = self.client.chat.complete(
            model=model,
            messages=[{"role": "user", "content": f"{promt}"}]
        )

        self.mistral_response = mistral_small_response

    def response(self):
        """Gibt die anwort von Mistral_small zurück; falls keine antwort zwischen gespeichert ist.
        wird ausgegeben: 'You did not ask anything. Please make a question!'"""
        if not self.mistral_response:
            return "You did not ask anything. Please make a question!"

        return self.mistral_response.choices[0].message.content

    def system_message(self):
        """erklärt dem LLM, was es genau mit den erhaltenen daten machen soll"""
        ...















