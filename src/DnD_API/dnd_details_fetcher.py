import requests
import time
from requests import RequestException
from src.DnD_API.base_classes.dnd_api_base import DnDAPIBase
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
		self.data = {}  # Hier werden die geladenen Daten gespeichert

	def load_data(self, delay=0.1):
		"""
	    Lädt die Klassendaten von der aktuell gesetzten URL (class_detail_url).
	    Ein Delay zwischen Anfragen schützt die öffentliche API vor Überlastung.
	    
	    """

		if not self.class_detail_url:
			print("Fehler: Keine class_detail_url gesetzt.")
			return

		try:
			response = requests.get(self.class_detail_url)
			
			if response.status_code == 200:
				self.data = response.json() # hier werden die daten der Api-response gespeichert
				time.sleep(delay)  # Kurze Pause für API-Rate-Limiting
			else:
				raise RequestException(
				    f"Fehler beim Laden der Daten. HTTP-Status: {response.status_code}"
				)
			
			# gibt self.data zürck. hier sind die daten aus der api-response als Json enthalten
			return self.data

		except RequestException as e:
			print(f"Fehler bei der Anfrage: {e}")
			self.data = None

	@property
	def detail_url(self):
		"""gibt die class_detail_url zurück"""
		return self.class_detail_url

	# TODO hier kann man mit pydantic und BaseModel überprüfen, dass ein echter url-string eingefügt wird
	@detail_url.setter
	def detail_url(self, new_detail_url):
		"""setzt eine neue class_detail_url"""
		self.class_detail_url = new_detail_url