from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
from utils.locators import YTHomeLocators, ResultsListLocators, SelectedVideoLocators
from conftest import TestVariables as TVar
from utils.test_data import Input
from time import sleep


class ListResultsPage(BaseTest):
    TVar.search_key = Input.search_keyword

    def test_TC_14_search_results_list_for_keyword(self):
        """Check correct search results for given keyword. Keyword appears in the page title"""
        expected_title = f'{TVar.search_key} - YouTube'
        self.results_list_page.visit(TVar.search_key)
        self.assert_if_element_is_visible(YTHomeLocators.cookies_accept_button)
        self.skip_popup(YTHomeLocators.cookies_accept_button)
        assert expected_title == self.driver.title, f'[{expected_title}] does not match [{self.driver.title}] title page'

    def test_TC_15_click_first_non_advert_video(self):
        """Verify the first, non advert, video is clicked and user is correctly redirected to its player page"""
        loaded_xpath = f'{ResultsListLocators.verify_xpath} "{TVar.search_key}")]'
        self.visibility_of_element_wait(self.driver, loaded_xpath)
        clicked_video_title = self.get_nth_element_text_value(ResultsListLocators.found_no_advert, 0)
        self.click_nth_list_element(ResultsListLocators.found_no_advert, 0)
        player_video_title = self.get_element_text_value(SelectedVideoLocators.video_title)
        assert clicked_video_title == player_video_title, f"{clicked_video_title} differ from {player_video_title}"

    def test_TC_16_play_first_non_advert_video_from_side_list(self):
        """Opens the first video of the side list"""
        self.click_nth_list_element(SelectedVideoLocators.first_side_video, 0)
        self.visibility_of_element_wait(self.driver, SelectedVideoLocators.advert_counter)
        self.skip_adverts()
        self.play_video_time(10)
        current_time = self.driver.find_element(By.XPATH, SelectedVideoLocators.current_play_time).text
        print(current_time)
        sec = current_time[-2:]
        print(sec)
        assert int(sec) == 10

