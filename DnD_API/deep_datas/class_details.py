"""
Basis classe für alle 12 dnd-Klassen
stellt die basis struktur für die sub-classen bereit

programm ablauf:
bekommt ein class_dict mit allen base-class informationen.
Aus diesem dict werden drei urls gezogen:
- spells
- levels
- subclasses

diese urls geben ein json zurück, aus dem tiefere details zu spells, levels und subclasses gezogen werden.
diese details werden auch über eine url gezogen.


hat funktionen:
spells() X
load_levels() X
load_subclasses() X

funktionen haben grobe grundstruktur
geben dict oder None zurück

weitere funktionen:
all feature details
all spell details
all subclass details

warlok braucht z.B noch die extra funktionen für eldrigde Invocations und pact boons
"""
from DnD_API.dnd_details_fetcher import DnDDetailsFetcher
from DnD_API.progress_tracker import ProgressTracker

BASE_URL = "https://www.dnd5eapi.co"

class ClassDetails:
    def __init__(self, data: dict, class_name: str):
        """
        data: the class_dictionary
        data wird mit: class_dictionary[i] eingegeben.
        class_name: überprüfungsname für daten
        """
        try:
            self.data = data # dictionary mit basis infos für nur eine einzige klasse
            self.d_fetcher = DnDDetailsFetcher()

            # hier wird dann beim instanzieren der class schon ein api zugriff gemacht
            if 'spells' not in self.data.keys():
                self.spells = None
            else:
                self.spells = self.load_spells()


            self.levels = self.load_levels()
            self.subclasses = self.load_subclasses()

            self.class_name = self.data['name']

            if self.class_name.lower() != class_name.lower():
                raise ValueError(f"Wrong data input. DnD Class name must be: {class_name}; Class name is: {self.class_name}")
        except ValueError as e:
            print(f"Error: {e}")


    def load_spells(self):
        spells_url = f"{BASE_URL}{self.data['spells']}"
        # bekommt dann ein dict mit allen spells
        # muss dann für jeden spell eine abfrage für die descirption machen
        self.d_fetcher.detail_url = spells_url

        print(f"laoding base spell data")
        spells_data = self.d_fetcher.load_data()

        return spells_data

    def load_levels(self):
        levels_url = f"{BASE_URL}{self.data['class_levels']}"
        # bekommt ein dict mit allen level resources
        self.d_fetcher.detail_url = levels_url

        print(f"laoding base level data")
        levels_data = self.d_fetcher.load_data()

        return levels_data

        # muss dan noch eine abfrage für die description für alle features machen

    def load_subclasses(self):
        subclasses_urls = [f"{BASE_URL}{entry['url']}" for entry in self.data['subclasses']]
        # bekommt eine liste mit allen urls für subclaces (momentan 1)
        # erhält nach abfrage ein dict mit subclass infos
        # wenn subclas spells enthält, dann spell description
        # subclass feature description abfragen

        all_subclass_data = []

        print(f"loading base subclass data:")
        for i, subclass_url in enumerate(subclasses_urls):
            print(f"loading subclass-{i}")
            self.d_fetcher.detail_url = subclass_url
            subclass_data = self.d_fetcher.load_data()
            all_subclass_data.append(subclass_data)

        return all_subclass_data

    def spell_details(self):
        enriched_spells = []
        tracker = ProgressTracker(self.spells["count"], task_name="spell_details")

        for i, spell in enumerate(self.spells["results"]):
            spell_url = f"{BASE_URL}{spell['url']}"
            self.d_fetcher.detail_url = spell_url
            spell_details_data = self.d_fetcher.load_data()

            enriched_spell = {
                "index": spell["index"],
                "name": spell["name"],
                "level": spell["level"],
                "details": spell_details_data
            }
            enriched_spells.append(enriched_spell)

            tracker.update(message=f"{i + 1}/{self.spells['count']}")

        tracker.done()
        return enriched_spells

    def level_details(self):
        tracker = ProgressTracker(len(self.levels), task_name="level_details")

        for i, level in enumerate(self.levels):
            enriched_features = []

            for j, feature in enumerate(level['features']):
                feature_url = f"{BASE_URL}{feature['url']}"
                self.d_fetcher.detail_url = feature_url
                feature_details_data = self.d_fetcher.load_data()

                enriched_features.append({
                    'index': feature['index'],
                    'name': feature['name'],
                    'details': feature_details_data
                })

            level['features'] = enriched_features
            tracker.update(message=f"{i + 1}/{len(self.levels)}")

        tracker.done()

    def subclass_details(self):
        enrichted_subclass_spells = []
        tracker_subclasses = ProgressTracker(len(self.subclasses), task_name="subclass_details")

        for i, subclass in enumerate(self.subclasses):
            if not subclass:
                print(f"Warning: subclass {i} is None – skipping.")
                continue

            # wenn keine zauber in der subclasse sind
            if 'spells' not in subclass.keys():
                return None

            else:
                spells = subclass['spells']
                tracker_spells = ProgressTracker(len(spells), task_name=f"subclass_{i+1}_spells")

                for j, spell in enumerate(spells):
                    spell_details_url = f"{BASE_URL}{spell['spell']['url']}"
                    self.d_fetcher.detail_url = spell_details_url
                    spell_details_data = self.d_fetcher.load_data()

                    enrichted_subclass_spells.append({
                        'prerequisites': spell['spells']['prerequisites'],
                        'index': spell['spells']['index'],
                        'name': spell['spells']['name'],
                        'details': spell_details_data
                    })

                    tracker_spells.update(message=f"{j + 1}/{len(spells)}")

                tracker_spells.done()

            enriched_subclasses = []
            subclass_levels_url = f"{BASE_URL}{subclass['subclass_levels']}"
            self.d_fetcher.detail_url = subclass_levels_url
            subclass_levels_data = self.d_fetcher.load_data()

            enriched_subclass_levels = []

            for k, subclass_level in enumerate(subclass_levels_data):
                subclass_level_url = f"{BASE_URL}{subclass['subclass_levels']}"
                self.d_fetcher.detail_url = subclass_level_url
                subclass_level = self.d_fetcher.load_data()

                enriched_features = []

                for l, feature in enumerate(subclass_levels_data['features']):
                    subclass_feature_url = f"{BASE_URL}{subclass['subclass_levels']}"
                    self.d_fetcher.detail_url = subclass_feature_url
                    feature_details_data = self.d_fetcher.load_data()

                    enriched_features.append({
                        'index': feature['index'],
                        'name': feature['name'],
                        'details': feature_details_data
                    })

                enriched_subclass_levels.append({
                    'level': subclass_level['level'],
                    'features': enriched_features,
                })

            enriched_subclasses.append({
                'index': subclass['index'],
                'class': subclass['class'],
                'name': subclass['name'],
                'subclass_flavor': subclass['sublcass_flavor'],
                'description': subclass['desc'],
                'spells': enrichted_subclass_spells,
                'subclass_levels': subclass_levels_data
            })

            tracker_subclasses.update(message=f"{i + 1}/{len(self.subclasses)}")

        tracker_subclasses.done()




    def all_details(self) -> tuple:
        if self.spells:
            self.spell_details()

        self.level_details()
        self.subclass_details()

        return self.spells, self.levels, self.subclasses