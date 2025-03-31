"""Diese Klasse lädt die JSON-Dateien aus dem lokalen Speicher.

Aufgabe:
	•	load_class_data("wizard") → gibt wizard.json zurück
	•	ggf. auch: load_spells("wizard"), load_features("sorcerer"), etc.

arbeitet mit f-string.
f-string sieht in etwa so aus:
f" (erstelle einen DnD character mit der Klasse: {Klannen_name}.
nutze diese daten für die erstellung.
Orientiere dich bei der erstellung an diesen details: {user promt-details}
)


"""
from openai import file_from_path

from src.handle_data.CRUD import CRUD

CLASS_INDICIES = {
  "barbarian": 0,
  "bard": 1,
  "cleric": 2,
  "druid": 3,
  "fighter": 4,
  "monk": 5,
  "paladin": 6,
  "ranger": 7,
  "rogue": 8,
  "sorcerer": 9,
  "warlock": 10,
  "wizard": 11
                }

class CharacterDataLoader:
    def __init__(self, class_name):
        self.crud = CRUD(None)

        self.class_name = class_name.lower()
        # TODO pfad muss vielleicht noch mal angepasst werden, je nach dem, wo die Klasse referenziert wird
        # TODO wenn pfad probleme macht, vielleicht mit OS arbeiten?
        self.data_base_path = "../../static_dnd_data/"
        self.base_data_path = "all_classes.json"
        self.class_data_path = f"{class_name}/{class_name}"

        self.detail_base_path = self.data_base_path + self.class_data_path

        self.class_base_data = self.data_base_path +  self.base_data_path
        self.spell_file_path = self.detail_base_path + "_spells.json"
        self.level_file_path = self.detail_base_path + "_levels_features.json"
        self.subclass_file_path = self.detail_base_path + "_subclass(es).json"

               # erstellt eine liste mit spell-, level- und subclass-datapath


    def class_data(self):
        """gibt alle klassen daten in einer liste zurück"""
        base_crud = CRUD(self.class_base_data)
        spell_crud = CRUD(self.spell_file_path)
        level_crud = CRUD(self.level_file_path)
        subclass_crud = CRUD(self.subclass_file_path)

        base_data = base_crud.data[CLASS_INDICIES[self.class_name]]

        spells = spell_crud.data
        level_features = level_crud.data
        subclasses = subclass_crud.data

        return base_data, spells, level_features, subclasses








