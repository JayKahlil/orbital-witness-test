import json

DATA_FILE_PATH = 'app/data.json'


def get_title_data():
    """
    Get all title data from the data store. In this case the data store is a JSON file.
    :return: A JSON representation of all title data.
    """
    with open(DATA_FILE_PATH) as data_file:
        return json.load(data_file)
