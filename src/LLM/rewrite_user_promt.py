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

    def rewrite(self, user_promt):
        """fragt das LLM, den User-Promt umzuschreiben"""
        stippted_user_prompt = user_promt.strip() # definiert den user_promt
        request = (f"Schreibe den folgenden Satz um, wobei du das zentrale Wesen durch "
                 f"'{self.class_name}' ersetzt: '''{stippted_user_prompt}'''."
                   f"Gebe nur den umgeschriebenen Satz zurück. Füge keine erklärungen hinzu.")
        self.ask(request) # gibt Mistral den Auftrag den user_promt umzuschreiben

        return self.response() # gibt umgeschriebenen user_promt zurück


    @property
    def prompt(self):
        return self._user_prompt

    @prompt.setter
    def prompt(self, user_promt):
        """definiert einen user-promt"""
        self._user_prompt = user_promt




if __name__ == "__main__":
    rewrite = RewriteUserPromt('fighter')

    user_promt = "dunkler Magier, der tote beschwört und feuer Zauber beherrscht"

    rewritten_promt = rewrite.rewrite(user_promt)

    print(rewritten_promt)