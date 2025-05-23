"""Diese Klasse baut die Systemnachricht zusammen.
Sie analysiert den Prompt und kombiniert ihn mit den JSON-Daten.

Aufgabe:
erhält Klassen daten, klassen_name und umgeschriebenen User-Promt
Kombiniert alles zu einem “System Prompt”"""
from src.handle_data.CRUD import CRUD


class CharacterRequestBuilder:
    def __init__(self):
        self.class_data = None # TODO hier character_data_loader einfügen
        self.class_details_message = None # TODO analyse_user_promt einfügen

        self.class_name = None # TODO aus analyse_user_promt einfügen
        # system nachricht, die dem LLM mehr details über die aufgabe gibt
        self.crud = CRUD("../../debug_data/LLM_log/system_message_alpha_01.txt")
        self.system_message = self.crud.data

    def build_request_message(self):
        """build from class data and user promt message for LLM"""
        class_data_message = f"Hier sind die Klassen-daten in einer Liste: {self.class_data}"
        class_details_message = f"Hier sind die Character Details: {self.class_details_message}"

        return self.system_message + class_data_message + class_details_message

