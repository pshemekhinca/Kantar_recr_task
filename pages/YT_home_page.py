from utils import json_reader


class HomePage:
    def __init__(self, driver):
        web = json_reader.load('web_urls.json')
        self.url = web["yt_home_url"]
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)
        return self


