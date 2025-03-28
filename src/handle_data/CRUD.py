import json

class CRUD:
    def __init__(self, data_path):
        self.data_path = data_path

    def _save(self, data):
        with open(self.data_path, 'w') as json_obj:
            json.dump(data, json_obj, indent=4)


    @property
    def data(self):
        try:
            with open(self.data_path, 'r') as json_obj:
                existing_data = json.load(json_obj)

                return existing_data

        except (FileNotFoundError, json.JSONDecodeError):
            print(f"Error: {self.data_path} could not be found")
            existing_data = []

            return existing_data

    @data.setter
    def data(self, new_data):
            existing_data = self.data

            existing_data.append(new_data)

            self._save(existing_data)


    def new_file(self, new_data):
        self._save(new_data)
