from utils import web_reader


class HomePage:
    def __init__(self, driver):
        web = web_reader.load()
        self.url = web["yt_home_url"]
        self.driver = driver

    def visit(self):
        self.driver.get(self.url)
        return self


