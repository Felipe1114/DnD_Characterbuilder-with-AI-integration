from DnD_API.dnd_api_base import DnDAPIBase
import requests
from requests import RequestException
import time

class DnDDetailsFetcher(DnDAPIBase):
    def __init__(self, url=None):
        super().__init__(url)
        self.detail_url = None

    def load_data(self):
        """loads detailed data for a class from DnD5e-API, depending on given url"""
        try:
            print(f"Loadt data from {self.detail_url}")
            response = requests.get(self.detail_url)

            if response.status_code == 200:
                self.data = response.json()
                time.sleep(0.1)  # delay for API

            else:
                raise RequestException(f"Error at loading: {response.status_code}; dnd_api_base.py 20")

        except RequestException as e:
            print(f"Error with request: {e}")

    @property
    def detail_url(self):
        return self.detail_url

    @detail_url.setter
    def detail_url(self, new_detail_url):
        self.detail_url = new_detail_url