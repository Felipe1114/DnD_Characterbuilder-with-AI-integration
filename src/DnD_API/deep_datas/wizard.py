from src.DnD_API import ClassDetails
import requests

class Wizard(ClassDetails):
    def spells(self):
        if not self.data.get("spells"):
            return None
        url = f"https://www.dnd5eapi.co{self.data['spells']}"
        response = requests.get(url)
        spells_data = response.json().get("results", [])
        descriptions = []

        for spell in spells_data:
            spell_url = f"https://www.dnd5eapi.co{spell['url']}"
            desc = requests.get(spell_url).json()
            descriptions.append(desc)
        return descriptions

    def levels(self):
        url = f"https://www.dnd5eapi.co{self.data['class_levels']}"
        levels_data = requests.get(url).json()
        return levels_data

    def subclasses(self):
        urls = [f"https://www.dnd5eapi.co{entry['url']}" for entry in self.data['subclasses']]
        all_subs = [requests.get(url).json() for url in urls]
        return all_subs