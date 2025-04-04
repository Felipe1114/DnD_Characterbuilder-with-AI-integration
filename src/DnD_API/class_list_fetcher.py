from src.DnD_API.dnd_api_base import DnDAPIBase

class DnDClassListFetcher(DnDAPIBase):
    def __init__(self):
        super().__init__('https://www.dnd5eapi.co/api/classes')

    def get_class_urls(self):
        self.load_data()
        # returns a list of all class urls
        return [f"https://www.dnd5eapi.co{entry['url']}" for entry in self.data.get('results', [])]