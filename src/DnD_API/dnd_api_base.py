import requests
from requests import RequestException
import time


class DnDAPIBase:
    def __init__(self, url):
        self.url = url
        self.data = {}

    def load_data(self):
        """loads data from DnD5e-API, depending on given url"""
        try:
            print(f"Load data from {self.url}")
            response = requests.get(self.url)

            if response.status_code == 200:
                self.data = response.json()
                time.sleep(0.1)  # delay for API

            else:
                raise RequestException(f"Error at loading: {response.status_code}; dnd_api_base.py 20")

        except RequestException as e:
            print(f"Error with request: {e}")
