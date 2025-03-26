from DnD_API.dnd_api_base import DnDAPIBase
from DnD_API.CRUD_for_Classes import CRUD
# TODO hier noch die databe_Class importieren

class DnDClassFetcher(DnDAPIBase):
    def __init__(self, url):
        super().__init__(url)
        self.crud = CRUD("../data_test/all_classes.json")
        # TODO hier noch ClassDetails einbauen

    def load_and_save(self):
        self.load_data()
        indicies = [key for key in self.data.keys() if key != 'updated_at']
        class_data_dict = {i: self.data.get(i) for i in indicies}

        class_name = class_data_dict['index']

        # hier kommt der code für die tiefer liegenden daten hin

        self.save_data(class_data_dict)

    # temporary method
    def save_data(self, new_data):
       # TODO hier muss dann, statt CRUD der SQLAlchemy code hin
        self.crud.data(new_data)



        # TODO hier kann dann der SQlAclhemy part angedockt
        #  werden um die tables zu erstellen und die daten in das SQLite file zu packen


