import json

DATA_FILE_PATH = 'app/data.json'


def get_title_data():
    with open(DATA_FILE_PATH) as data_file:
        return json.load(data_file)
