from utils import web_reader


class ResultsListPage:
    def __init__(self, driver):
        web = web_reader.load()
        self.url = web["yt_results_url"]
        self.driver = driver

    def visit(self, keyword):
        self.driver.get(f'{self.url}{keyword}')
        return self
