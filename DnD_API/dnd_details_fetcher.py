import requests
import time
from requests import RequestException
from DnD_API.dnd_api_base import DnDAPIBase

class DnDDetailsFetcher(DnDAPIBase):
    """
    Diese Klasse ist für das Laden von Detaildaten zu DnD-Klassen zuständig.
    Sie erbt von DnDAPIBase und erweitert sie um eine einstellbare URL sowie um eine Datenlade-Funktion.
    """

    def __init__(self, base_url=None):
        """
        Initialisiert den Fetcher. Optional kann eine Basis-URL angegeben werden.
        """
        super().__init__(base_url)
        self.class_detail_url = None  # Diese URL wird später gesetzt, um Klassendaten zu laden
        self.data = None  # Hier werden die geladenen Daten gespeichert

    def load_data(self, delay=0.1):
        """
        Lädt die Klassendaten von der aktuell gesetzten URL (class_detail_url).
        Ein Delay zwischen Anfragen schützt die öffentliche API vor Überlastung.
        """

        if not self.class_detail_url:
            print("Fehler: Keine class_detail_url gesetzt.")
            return

        try:
            print(f"Lade Klassendaten von: {self.class_detail_url}")
            response = requests.get(self.class_detail_url)
            print(response)

            if response.status_code == 200:
                self.data = response.json()
                time.sleep(delay)  # Kurze Pause für API-Rate-Limiting
            else:
                raise RequestException(
                    f"Fehler beim Laden der Daten. HTTP-Status: {response.status_code}"
                )

            return self.data

        except RequestException as e:
            print(f"Fehler bei der Anfrage: {e}")
            self.data = None

    @property
    def detail_url(self):
        return self.class_detail_url

    @detail_url.setter
    def detail_url(self, new_detail_url):
        self.class_detail_url = new_detail_url