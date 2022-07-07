import os
import json


def load(file_name):
    """Regardless of the OS used, the path will be formatted correctly """
    print(file_name)
    config_path = os.path.join(os.path.dirname(__file__), '', file_name)
    with open(config_path, 'r') as file:
        config = file.read()
        return json.loads(config)