"""
Basis classe für alle 12 dnd-Klassen
stellt die basis struktur für die sub-classen bereit

hat funktionen:
spells()
levels()
subclases()

funktionen haben grobe grundstruktur
geben dict oder None zurück

weitere funktionen:
all feature descriptions
all spell descriptions

warlok braucht z.B noch die extra funktionen für eldrigde Invocations und pact boons
"""
#TODO funktionen für alle nötigen descripitons einfügen
from abc import ABC, abstractmethod

BASE_URL = "https://www.dnd5eapi.co"

class ClassDetails(ABC):
    def __init__(self, data: dict, class_index: str):
        """
        data: the class_dictionary
        class_index: the 'class_name' like 'sourcerer' or 'barbarian'
        """
        self.data = data # class dictionary
        self.mid_url = f"api/2014/classes/{class_index}"

    def build_url(self, index):
        return f"{BASE_URL}/{self.mid_url}/{index}"

    @abstractmethod
    def spells(self):
        url = f"{BASE_URL}{self.data['spells']}"
        # bekommt dann ein dict mit allen spells
        # muss dann für jeden spell eine abfrage für die descirption machen

    def levels(self):
        url = f"{BASE_URL}{self.data['class_levels']}"
        # bekommt ein dict mit allen level resources
        # muss dan noch eine abfrage für die description für alle features machen

    def subclases(self):
        urls = [f"{BASE_URL}{entry['url']}" for entry in self.data['subclasses']]
        # bekommt eine liste mit allen urls für subclases (momentan 1)
        # erhält nach abfrage ein dict mit subclass infos
        # wenn subclas spells enthält, dann spell description
        # subclass feature description abfragen
