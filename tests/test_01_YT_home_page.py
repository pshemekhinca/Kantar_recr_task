from selenium.webdriver.common.by import By

from tests.base_test import BaseTest
from utils.locators import YTHomeLocators, ResultsListLocators
from utils.test_data import Input


class HomePageTests(BaseTest):

    def test_home_page_title_TC_01(self):
        """Verify correct page title after skipping cookies prompt"""
        expected_title = "YouTube"
        self.home_page.visit()
        self.assert_if_element_is_visible(YTHomeLocators.cookies_accept_button)
        self.skip_popup(YTHomeLocators.cookies_accept_button)
        self.assertEqual(expected_title, self.driver.title,
                         f'Expected title differ from the {self.driver.current_url} title page')

    def test_search_result_for_Python_keyword_TC_02(self):
        """Verify if entered keyword search, returns url for search results"""
        self.visibility_of_element_wait(self.driver, YTHomeLocators.search_box)
        self.enter_data_and_click(YTHomeLocators.search_box, Input.search_keyword, YTHomeLocators.search_button)
        self.visibility_of_element_wait(self.driver, ResultsListLocators.found_no_advert)
        expected_url = f'https://www.youtube.com/results?search_query={Input.search_keyword}'
        assert expected_url == self.driver.current_url, f"{self.driver.current_url} differ from expected"


