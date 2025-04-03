"""Gegeben ist der folgende Nutzer-Prompt:
{user_promt}

Finde die zu diesem Prompt am besten passenden Klassen aus folgender 'class_name' Liste:
- barbarian
- bard
- cleric
- druid
- fighter
- monk
- paladin
- ranger
- rogue
- sorcerer
- warlock
- wizard

Gib als Ergebnis ein JSON mit folgendem Format zurück:
{
"matched_classes": [best_class, second_best_class, thrid_best_class],
"keywords": [keywords aus user_promt, die den character, seine Fähigkeiten und Eingeschaften beschreiben],
"rewritten_prompt_template": [umgeschriebene user_prompt mit best_class, umgeschriebener user_promt mit second_best_clas, ...]
}

Beispiel:
user_promt: "dunkler Magier, der tote beschwört und feuer Zauber beherrscht"
JSON rückgabe:
{
"matched_classes": ["wizard", "warlock", "cleric"],
"keywords": ["dunkel", "beschwörung", "feuer", "tote", "zauber"],
"rewritten_prompt_template": ["dunkler wizard, der tote beschwört und Feuerzauber beherrscht", "dunkler warlock, der tote beschwört und Feuerzauber beherrscht", "dunkler cleric', der tote beschwört und Feuerzauber beherrscht"]
}

"""
from src.LLM.talk_to_mistral import TalkToMistral
from src.handle_data.CRUD import CRUD

prompt_data_path = "../../static_dnd_data/system_messages/system_prompts_for_analysing.json"

class RewriteUserPromt(TalkToMistral):
    def __init__(self, user_prompt, prompt_key: str= "prompt_alpha_1"):
        """
        crud: the class, wich gets the prompt from the prompt file
        prompt_key: the key to geht the correct prompt from the prompt dict
        """
        super().__init__()
        self.crud = CRUD(prompt_data_path)
        self.prompt_key = prompt_key
        self._user_prompt = user_prompt

    def rewrite(self):
        """fragt das LLM, den User-Promt umzuschreiben"""
        #user_prompt = user_promt.strip() # definiert den user_promt
        request = self.generate_request_prompt()
        self.ask(request) # gibt Mistral den Auftrag den user_promt umzuschreiben

        return self.response() # gibt umgeschriebenen user_promt zurück


    @property
    def prompt(self):
        return self._user_prompt

    @prompt.setter
    def prompt(self, user_promt):
        """definiert einen user-promt"""
        self._user_prompt = user_promt


    def generate_request_prompt(self) -> str:
        """generates the prompt for the request, out of the given system_prompt and the user_prompt"""
        request: str = self.crud.data[self.prompt_key]

        request_prompt = request.replace("{PLACEHOLDER}", self._user_prompt)

        return request_prompt




if __name__ == "__main__":
    crud = CRUD()

    prompt_key = "prompt_alpha_3"
    user_promt = "dunkler Magier, der tote beschwört und feuer Zauber beherrscht"

    data_strukture = [
        {

        }
    ]

    rewrite = RewriteUserPromt(user_promt, prompt_key=prompt_key)

    rewritten_promt = rewrite.rewrite()


    print(type(rewritten_promt))
    print(rewritten_promt)