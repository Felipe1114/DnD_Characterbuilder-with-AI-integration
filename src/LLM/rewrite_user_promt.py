"""
schreibt den user promt um.
von ‘dunkler Magier, der tote beschwört und feuer Zauber beherrscht’
 wird: 'dunkler {Klassen_name}, der tote beschwört und feuer Zauber beherrscht.
"""
from src.LLM.talk_to_mistral import TalkToMistral

class RewriteUserPromt(TalkToMistral):
    def __init__(self, class_name: str):
        super().__init__()
        self.class_name = class_name
        self._user_prompt = None
        self.__system_prompt = f"Schreibe den folgenden Satz um, wobei du das zentrale Wesen durch '{self.class_name}' ersetzt: '''{self._user_prompt}'''\n"

    def rewrite(self, user_promt):
        """fragt das LLM, den User-Promt umzuschreiben"""
        self.prompt = user_promt.strip() # definiert den user_promt

        self.ask(self.__system_prompt) # gibt Mistral den Auftrag den user_promt umzuschreiben

        return self.response() # gibt umgeschriebenen user_promt zurück


    @property
    def prompt(self):
        return self._user_prompt

    @prompt.setter
    def prompt(self, user_promt):
        """definiert einen user-promt"""
        self._user_prompt = user_promt




if __name__ == "__main__":
    rewrite = RewriteUserPromt('wizard')

    user_promt = "dunkler Magier, der tote beschwört und feuer Zauber beherrscht"

    rewritten_promt = rewrite.rewrite(user_promt)

    print(rewritten_promt)