from DnD_API.base.class_base import ClassDetails
import requests

class Fighter(ClassDetails):
    def spells(self):
        return None  # Fighter hat keine spells

    def levels(self):
        url = f"https://www.dnd5eapi.co{self.data['class_levels']}"
        levels_data = requests.get(url).json()
        return levels_data

    def subclasses(self):
        urls = [f"https://www.dnd5eapi.co{entry['url']}" for entry in self.data['subclasses']]
        all_subs = [requests.get(url).json() for url in urls]
        return all_subs