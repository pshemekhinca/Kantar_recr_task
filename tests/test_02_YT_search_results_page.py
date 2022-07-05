from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
from utils.locators import YTHomeLocators, ResultsListLocators, SelectedVideoLocators
from conftest import TestVariables as TVar
from utils.test_data import Input
from time import sleep


class ListResultsPage(BaseTest):
    TVar.search_key = Input.search_keyword

    def test_TC_03_search_results_list_for_keyword(self):
        """Check correct search results for given keyword. Keyword appears in the page title"""
        expected_title = f'{TVar.search_key} - YouTube'
        self.results_list_page.visit(TVar.search_key)
        self.assert_if_element_is_visible(YTHomeLocators.cookies_accept_button)
        self.skip_popup(YTHomeLocators.cookies_accept_button)
        assert expected_title == self.driver.title, f'[{expected_title}] does not match [{self.driver.title}] title page'

    def test_TC_04_click_first_non_advert_video(self):
        """Verify the first, non advert, video is clicked and user is correctly redirected to its player page"""
        loaded_xpath = f'{ResultsListLocators.verify_xpath} "{TVar.search_key}")]'
        self.visibility_of_element_wait(self.driver, loaded_xpath)
        clicked_video_title = self.get_nth_element_text_value(ResultsListLocators.found_no_advert, 0)
        self.click_nth_list_element(ResultsListLocators.found_no_advert, 0)
        player_video_title = self.get_element_text_value(SelectedVideoLocators.video_title)
        assert clicked_video_title == player_video_title, f"{clicked_video_title} differ from {player_video_title}"

    def test_TC_05_play_pre_roll_adverts(self):
        """Plays pre-loaded adverts till the end"""
        self.visibility_of_element_wait(self.driver, SelectedVideoLocators.advert_counter)
        adv_player = self.driver.find_element(By.XPATH, SelectedVideoLocators.advert_counter)
        while adv_player:
            try:
                # self.driver.find_element(By.XPATH, SelectedVideoLocators.skip_advert_button)
                self.driver.find_element(By.XPATH, SelectedVideoLocators.advert_counter)
            except NoSuchElementException:
                break

    def test_TC_06_drag_slider(self):
        """Drags the player slider around the middle of total video length"""
        video_duration = self.get_duration_time(SelectedVideoLocators.video_duration)
        total_time_sec = self.time_to_seconds(video_duration)
        self.visibility_of_element_wait(self.driver, SelectedVideoLocators.sliderbar)
        self.move_slider(SelectedVideoLocators.sliderbar)
        play_time = self.get_duration_time(SelectedVideoLocators.current_play_time)
        current_play_time = self.time_to_seconds(play_time)
        assert total_time_sec / 2 - total_time_sec / 8 <= current_play_time <= total_time_sec / 2 + total_time_sec / 8

    def test_TC_07_play_and_mute_video(self):
        """Play and mute selected video"""
        self.visibility_of_element_wait(self.driver, SelectedVideoLocators.play_button)
        self.click_element(SelectedVideoLocators.play_button)
        self.visibility_of_element_wait(self.driver, SelectedVideoLocators.mute_button)
        self.click_element(SelectedVideoLocators.mute_button)



