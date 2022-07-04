import os
import json


def load():
    """Regardless of the OS used, the path will be formatted correctly """

    config_path = os.path.join(os.path.dirname(__file__), '', 'web_urls.json')
    with open(config_path, 'r') as file:
        config = file.read()
        return json.loads(config)