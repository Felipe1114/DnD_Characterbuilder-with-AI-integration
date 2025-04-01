"""Diese Klasse baut die Systemnachricht zusammen.
Sie analysiert den Prompt und kombiniert ihn mit den JSON-Daten.

Aufgabe:
	•	erkennt aus dem Prompt, welche Klassen gefragt sind (z. B. Wizard, Sorcerer)
	•	lädt die entsprechenden JSON-Dateien
	•	kombiniert alles zu einem “System Prompt”"""
from src.handle_data.CRUD import CRUD


class CharacterRequestBuilder:
    def __init__(self):
        self.class_data = None # TODO hier character_data_loader einfügen
        self.class_details_message = None # TODO analyse_user_promt einfügen

        self.class_name = None # TODO aus analyse_user_promt einfügen
        # system nachricht, die dem LLM mehr details über die aufgabe gibt
        self.crud = CRUD("../../static_dnd_data/system_messages/system_message_alpha_01.txt")
        self.system_message = self.crud.data

    def build_request_message(self):
        """build from class data and user promt message for LLM"""
        class_data_message = f"Hier sind die Klassen-daten in einer Liste: {self.class_data}"
        class_details_message = f"Hier sind die Character Details: {self.class_details_message}"

        return self.system_message + class_data_message + class_details_message

