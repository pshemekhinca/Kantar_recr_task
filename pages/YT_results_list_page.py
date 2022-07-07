from utils import json_reader


class ResultsListPage:
    def __init__(self, driver):
        web = json_reader.load('web_urls.json')
        self.url = web["yt_results_url"]
        self.driver = driver

    def visit(self, keyword):
        self.driver.get(f'{self.url}{keyword}')
        return self
