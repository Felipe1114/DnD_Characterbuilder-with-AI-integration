from DnD_API.class_list_fetcher import DnDClassListFetcher
from DnD_API.dnd_class_fetcher import DnDClassFetcher

class DnDClassManager:
    def __init__(self):
        self.classes = []

    def run(self):
        # instanziert DnDClassListFetcher
        fetcher = DnDClassListFetcher()
        # gets all urls for all classes, in a list
        class_urls = fetcher.get_class_urls()

        for url in class_urls:
            print(f"→ load class: {url}")
            # instanciates for evry 'round' DnDClassFetcher with new url
            # gets so all data for each class
            # all data means, all data, like spells, spell descripitons, etc...
            char_class = DnDClassFetcher(url)

            # saves data in SQLite database
            char_class.load_and_save()

            print(char_class.data)
            # saves dnd_classes for later use
            self.classes.append(char_class)