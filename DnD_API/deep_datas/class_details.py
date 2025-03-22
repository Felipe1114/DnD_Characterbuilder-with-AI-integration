"""
Basis classe für alle 12 dnd-Klassen
stellt die basis struktur für die sub-classen bereit

hat funktionen:
spells() X
levels() X
subclases() X

funktionen haben grobe grundstruktur
geben dict oder None zurück

weitere funktionen:
all feature descriptions
all spell descriptions

warlok braucht z.B noch die extra funktionen für eldrigde Invocations und pact boons
"""
from abc import ABC
from DnD_API.dnd_details_fetcher import DnDDetailsFetcher

BASE_URL = "https://www.dnd5eapi.co"

class ClassDetails(ABC):
    def __init__(self, data: dict, class_name: str):
        """
        data: the class_dictionary
        class_name: überprüfungsname für daten
        """
        try:
            self.data = data # class dictionary
            self.d_fetcher = DnDDetailsFetcher()

            # hier wird dann beim instanzieren der class schon ein api zugriff gemacht
            self.spells = self.spells()
            self.levels = self.levels()
            self.subclasses = self.subclasses()

            self.class_name = self.data['name']

            if self.class_name.lower() != class_name.lower():
                raise ValueError(f"Wrong data input. DnD Class name must be: {class_name}; Class name is: {self.class_name}")
        except ValueError as e:
            print(f"Error: {e}")


    def spells(self):
        spells_url = f"{BASE_URL}{self.data['spells']}"
        # bekommt dann ein dict mit allen spells
        # muss dann für jeden spell eine abfrage für die descirption machen
        self.d_fetcher.detail_url = spells_url

        spells_data = self.d_fetcher.load_data()

        return spells_data

    def levels(self):
        levels_url = f"{BASE_URL}{self.data['class_levels']}"
        # bekommt ein dict mit allen level resources
        self.d_fetcher.detail_url = levels_url

        levels_data = self.d_fetcher.load_data()

        return levels_data

        # muss dan noch eine abfrage für die description für alle features machen

    def subclasses(self):
        subclasses_urls = [f"{BASE_URL}{entry['url']}" for entry in self.data['subclasses']]
        # bekommt eine liste mit allen urls für subclases (momentan 1)
        # erhält nach abfrage ein dict mit subclass infos
        # wenn subclas spells enthält, dann spell description
        # subclass feature description abfragen

        all_subclass_data = []

        for subclass_url in subclasses_urls:
            self.d_fetcher.detail_url = subclass_url
            subclass_data = self.d_fetcher.load_data()
            all_subclass_data.append(subclass_data)

        return all_subclass_data

    def add_spell_details(self):
        # Durchlaufe alle Zauber-Einträge
        enriched_spells = []

        for spell in self.spells["results"]:
            spell_url = f"{BASE_URL}{spell['url']}"

            self.d_fetcher.detail_url = spell_url
            spell_details = self.d_fetcher.load_data()

            enriched_spell = {
                "index": spell["index"],
                "name": spell["name"],
                "level": spell["level"],
                "details": spell_details
            }
            enriched_spells.append(enriched_spell)

        return enriched_spells

    def add_level_details(self):
        # durchlaufe alle features für jedes level

        for level in self.levels:

            enriched_features = []

            for feature in level['features']:
                feature_url = f"{BASE_URL}{feature['url']}"

                self.d_fetcher.detail_url = feature_url
                feature_details = self.d_fetcher.load_data()

                enriched_features.append({
                    'index': feature['index'],
                    'name': feature['name'],
                    'details': feature_details
                })

            # alte features mit url werden mit features mit details ersetzt
            level['features'] = enriched_features


    def add_subclass_details(self):
        # durchlaufe alle subclasses und erhalte die informationen für die features und zauber der subclass

        # sublcass_details enthalten:
        # subclass
        # spells
        # - spells descriptions
        # - levels
        # -- feature-descriptions

        enrichted_subclass_spells = []

        for subclass in self.subclasses:

            # erhält alle spell details
            spells = subclass['spells']

            for spell in spells:
                spell_details_url = f"{BASE_URL}{spell['spell']['url']}"

                self.d_fetcher.detail_url = spell_details_url
                spell_details = self.d_fetcher.load_data()

                enrichted_subclass_spells.append({
                    'prerequisites': spell['spells']['prerequisites'],
                    'index': spell['spells']['index'],
                    'name': spell['spells']['name'],
                    'details': spell_details
                })

            # erhält alle features zur subclass
            enriched_subclasses = []

            subclass_levels_url = f"{BASE_URL}{subclass['subclass_levels']}"

            self.d_fetcher.detail_url = subclass_levels_url
            subclass_levels = self.d_fetcher.load_data()

            enriched_subclass_levels = []

            for subclass_level in subclass_levels:
                subclass_level_url = f"{BASE_URL}{subclass['subclass_levels']}"

                self.d_fetcher.detail_url = subclass_level_url
                subclass_level = self.d_fetcher.load_data()

                # erhält alle feature details
                enriched_features = []

                for feature in subclass_levels['features']:
                    subclass_feature_url = f"{BASE_URL}{subclass['subclass_levels']}"

                    self.d_fetcher.detail_url = subclass_feature_url
                    feature_details = self.d_fetcher.load_data()

                    # fügt feature detaisl aus api request in jedes feature hinzu
                    enriched_features.append({
                        'index': feature['index'],
                        'name': feature['name'],
                        'details': feature_details
                    })

                # fügt alle level freatures mit beschreibungen hinzu
                enriched_subclass_levels.append({
                    'level': subclass_level['level'],
                    'features': enriched_features,
                })

            # fügt die subclass mit allen spells und spellbeschreibungen und features und feature beschreibungen hinzu
            enriched_subclasses.append({
                'index': subclass['index'],
                'class': subclass['class'],
                'name': subclass['name'],
                'subclass_flavor': subclass['sublcass_flavor'],
                'description': subclass['desc'],
                'spells': enrichted_subclass_spells, # hier müssen dann noch die enrichted spells rein
                'subclass_levels': subclass_levels
            })
