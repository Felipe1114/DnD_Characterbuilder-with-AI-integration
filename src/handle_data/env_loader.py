from dotenv import load_dotenv
import os


class EnvLoader:
    """
    Lädt Umgebungsvariablen aus einer .env-Datei und stellt Zugriffsmethoden bereit.
    """

    def __init__(self, env_path: str = ".env"):
        """
        Initialisiert die Klasse und lädt die .env-Datei.

        :param env_path: Pfad zur .env-Datei (Standard: ".env" im Projektordner)
        """
        load_dotenv(dotenv_path=env_path)  # lädt alle Variablen aus der .env-Datei

    def get(self, key: str) -> str | None:
        """
        Gibt den Wert einer Umgebungsvariable zurück.

        :param key: Der Name der Variable, z.b. "Mistral_API_Key"
        :return: Der Wert als String oder None, falls nicht gefunden
        """
        if not key:
            print("API Key nicht gefunden, env_loader.py 26")
            quit('Programm_unvorhergesehen_beendet')

        return os.getenv(key)

    def get_mistral_api_key(self) -> str | None:
        """
        Spezielle Methode zum Abrufen deines Mistral API-Schlüssels.
        """
        return self.get("Mistral_API_Key")