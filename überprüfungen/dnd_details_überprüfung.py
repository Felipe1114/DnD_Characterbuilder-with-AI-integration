from DnD_API.deep_datas.class_details import ClassDetails
from DnD_API.CRUD_for_Classes import CRUD
CLASS_NAMES = {
            'barbarian': 0,
            'bard': 1,
            'cleric': 2,
            'druid': 3,
            'fighter': 4,
            'monk': 5,
            'paladin': 6,
            'ranger': 7,
            'rogue': 8,
            'sorcerer': 9,
            'warlock': 10,
            'wizard': 11
                        }

# erhält gesamte base_class_datas von allen 12 Klassen
crud = CRUD('../data_test/all_classes.json')
# den index des 'wizards'
wizard_id = CLASS_NAMES['wizard']
# wizard base_data aus großer base_data liste extrahieren
wizard_base_data = crud.data[wizard_id]

wizard_details = ClassDetails(wizard_base_data, 'wizard')

wizard_details.initialize_all_data()
wizard_data = wizard_details.initialize_all_details()

file_name_list = ['wizard_spells.json', 'wizard_levels_features.json', 'wizard_subclass(es).json']
for i, data in enumerate(wizard_data):
    crud_2 = CRUD(f'.././data_test/{file_name_list[i]}')
    crud_2.data = data

