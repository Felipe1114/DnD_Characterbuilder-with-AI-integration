"""
Basis-Klasse für alle 12 DnD-Klassen.
Stellt die Grundstruktur für Subklassen bereit.
"""

from DnD_API.dnd_details_fetcher import DnDDetailsFetcher
from DnD_API.progress_tracker import ProgressTracker

BASE_URL = "https://www.dnd5eapi.co"

# Diese Klasse verwaltet die Daten einer DnD-Klasse aus der 5e API.
# Sie lädt und verarbeitet Informationen über Zauber, Level und Subklassen.
class ClassDetails:
    def __init__(self, data: dict, class_name: str):
        """Initialisiert die Klasse mit Basisdaten und prüft den Klassennamen."""
        self.data = data # ein dict mit base-daten einer DnD Klasse
        self.class_name = self.data.get('name', '').lower()
        self.d_fetcher = DnDDetailsFetcher()

        if self.class_name != class_name.lower():
            raise ValueError(f"Wrong data input. Expected '{class_name}', got '{self.class_name}'.")

        self.spells = None
        self.levels = None
        self.subclasses = None

        self.enriched_spells = None
        self.enriched_levels = None
        self.enriched_subclasses = []

    def initialize_all_data(self):
        """Initialisiert alle Basisdaten: Zauber, Level und Subklassen."""
        # Überprüfen, ob Zauber vorhanden sind und laden
        self.spells = self.load_spells() if 'spells' in self.data else None
        # Laden der Leveldaten
        self.levels = self.load_levels()
        # Laden der Subklassendaten
        self.subclasses = self.load_subclasses()

    def load_spells(self):
        """Lädt die Zauberinformationen für die Klasse."""
        # API-Call zur Zauber-URL
        url = f"{BASE_URL}{self.data['spells']}"

        self.d_fetcher.detail_url = url
        print("Loading base spell data")
        return self.d_fetcher.load_data()

    def load_levels(self):
        """Lädt die Levelinformationen für die Klasse."""
        # API-Call zur Level-URL
        url = f"{BASE_URL}{self.data['class_levels']}"

        self.d_fetcher.detail_url = url
        print("Loading base level data")
        return self.d_fetcher.load_data()

    def load_subclasses(self):
        """Lädt die Subklasseninformationen für die Klasse."""
        # Erstellen von URLs für alle Subklassen
        urls = [f"{BASE_URL}{entry['url']}" for entry in self.data.get('subclasses', [])]
        all_data = []

        print("Loading base subclass data")
        for i, url in enumerate(urls):
            print(f"Loading subclass-{i}")
            self.d_fetcher.detail_url = url
            # API-Call zur Subklassen-URL
            data = self.d_fetcher.load_data()
            if data:
                all_data.append(data)

        return all_data

    def spell_details(self):
        """Lädt detaillierte Informationen zu den Zaubern der Klasse."""
        if not self.spells:
            return []

        # Fortschrittsverfolgung für das Laden der Zauber
        tracker = ProgressTracker(self.spells.get("count", 0), task_name="spell_details")
        detailed_spells = []

        for i, spell in enumerate(self.spells.get("results", [])):
            # API-Call zur Zauber-URL
            url = f"{BASE_URL}{spell['url']}"

            # setzt die url für den fetching prozess
            self.d_fetcher.detail_url = url
            details = self.d_fetcher.load_data()

            detailed_spells.append({
                "index": spell["index"],
                "name": spell["name"],
                "level": spell.get("level"), # TODO warum hier spell.geht('level')?
                "details": details
            })

            tracker.update(message='loading spell details')

        tracker.done()

        # speichere spells zwischen
        self.enriched_spells = detailed_spells


    def level_details(self):
        """Lädt detaillierte Informationen zu den Leveln der Klasse."""
        # Fortschrittsverfolgung für das Laden der Level
        tracker = ProgressTracker(len(self.levels), task_name="level/feature details")
        # leehre liste die später in self.enriched_levels gespeichert wird
        enriched_levels = []

        for i, level in enumerate(self.levels):
            features = []

            # hier gehen wir in die feature liste hinein und iterieren darüber
            for feature in level.get('features', []):
                # API-Call zur Feature-URL
                url = f"{BASE_URL}{feature['url']}"

                # url für api zugriff wird in fetcher gesetzt
                self.d_fetcher.detail_url = url
                details = self.d_fetcher.load_data()
                features.append({
                    "index": feature["index"],
                    "name": feature["name"],
                    "details": details
                })

            level["features"] = features
            tracker.update(message='loading level/feature details')

        # gefechte daten abspeichern
        self.enriched_levels = enriched_levels
        tracker.done()



    def subclass_details(self):
        """Lädt detaillierte Informationen zu den Subklassen der Klasse."""
        # Fortschrittsverfolgung für das Laden der Subklassen
        tracker = ProgressTracker(len(self.subclasses), task_name="subclasses")

        for i, subclass in enumerate(self.subclasses):
            tracker.update(message='loading subclasses')
            self._enrich_subclass(subclass)

        tracker.done()

    def _enrich_subclass(self, subclass):
        """Ergänzt die Subklasseninformationen mit Zaubern und Leveln/features."""
        # Spells
        if 'spells' in subclass:
            subclass_spells = []
            spell_list = subclass.get('spells', [])
            # Fortschrittsverfolgung für das Laden der Subklassenzauber
            spell_tracker = ProgressTracker(len(spell_list), task_name=f"subclass:{subclass['name']} spells")

            for s, spell_entry in enumerate(spell_list):
                spell = spell_entry.get('spell', {})
                # API-Call zur Zauber-URL
                url = f"{BASE_URL}{spell.get('url')}"
                self.d_fetcher.detail_url = url
                details = self.d_fetcher.load_data()

                subclass_spells.append({
                    "index": spell.get("index"),
                    "name": spell.get("name"),
                    "prerequisites": spell_entry.get("prerequisites"),
                    "details": details
                })

                spell_tracker.update(message=f'loading {subclass['name']} spells')

            spell_tracker.done()
            subclass['spells'] = subclass_spells

        # Subclass Levels
        if 'subclass_levels' in subclass:
            # API-Call zur Subclass Levels-URL
            url = f"{BASE_URL}{subclass['subclass_levels']}"
            self.d_fetcher.detail_url = url
            levels = self.d_fetcher.load_data()

            # Fortschrittsverfolgung für das Laden der Subklassenzauber
            feature_tracker = ProgressTracker(len(levels), task_name=f"subclass:{subclass['name']} levels/features")

            for level in levels:
                features = []
                for feature in level.get('features', []):
                    # API-Call zur Feature-URL
                    f_url = f"{BASE_URL}{feature['url']}"
                    self.d_fetcher.detail_url = f_url
                    details = self.d_fetcher.load_data()
                    features.append({
                        "index": feature["index"],
                        "name": feature["name"],
                        "details": details
                    })

                    feature_tracker.update(message=f'loading {subclass['name']} levels/features')

                level["features"] = features

            subclass['subclass_levels'] = levels

            self.enriched_subclasses.append(subclass)


    def initialate_all_details(self) -> tuple:
        """Lädt alle Details: Zauber, Level und Subklassen."""
        if self.spells:
            self.spell_details()
        self.level_details()
        self.subclass_details()
        return self.enriched_spells, self.enriched_levels, self.enriched_subclasses