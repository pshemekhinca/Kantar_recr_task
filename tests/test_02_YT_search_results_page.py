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
        self.visibility_of_element_wait(self.driver, ResultsListLocators.found_no_advert)
        clicked_video_title = self.get_nth_element_text_value(ResultsListLocators.found_no_advert, 0)
        self.click_nth_list_element(ResultsListLocators.found_no_advert, 0)
        self.visibility_of_element_wait(self.driver, SelectedVideoLocators.video_player)
        self.play_pause_video()
        player_video_title = self.get_element_text_value(SelectedVideoLocators.video_title)
        print(player_video_title)
        assert clicked_video_title == player_video_title, f"{clicked_video_title} differ from {player_video_title}"

    def test_TC_05_play_pre_roll_adverts(self):
        """Plays pre-loaded adverts till the end"""
        advert_counter = self.visibility_of_element_wait(self.driver, SelectedVideoLocators.advert_counter)
        if advert_counter:
            self.wait_until_adverts_end()
        else:
            pass

    def test_TC_06_drag_slider(self):
        """Drags the player slider around the middle of total video length"""
        video_duration = self.get_duration_time(SelectedVideoLocators.video_duration)
        total_time_sec = self.time_to_seconds(video_duration)
        self.visibility_of_element_wait(self.driver, SelectedVideoLocators.sliderbar_pointer)
        self.move_slider_to_middle(SelectedVideoLocators.sliderbar_pointer)
        sleep(1)
        play_time = self.get_duration_time(SelectedVideoLocators.current_play_time)
        current_play_time = self.time_to_seconds(play_time)
        assert total_time_sec / 2 - total_time_sec / 8 <= current_play_time <= total_time_sec / 2 + total_time_sec / 8


    def test_TC_07_play_and_mute_video(self):
        """Press play button and mute selected video"""
        self.visibility_of_element_wait(self.driver, SelectedVideoLocators.play_button)
        self.click_element(SelectedVideoLocators.play_button)
        self.visibility_of_element_wait(self.driver, SelectedVideoLocators.mute_button)
        self.click_element(SelectedVideoLocators.mute_button)

    def test_TC_08_get_video_title_and_write_to_file(self):
        """Gets video title and writes the value into the json file"""
        self.assert_element_value_equals_file_value(SelectedVideoLocators.video_title, "video title", "video_title")

    def test_TC_09_get_video_duration_and_write_to_file(self):
        """Gets video duration and writes the value into the json file"""
        self.assert_element_value_equals_file_value(SelectedVideoLocators.video_duration, "video duration",
                                                    "video_duration")

    def test_TC_10_get_video_channel_name_and_write_to_file(self):
        """Gets channel name of played video and writes the value into the json file"""
        channel_name = self.get_nth_element_text_value(SelectedVideoLocators.channel_name, 1)
        TVar.video_info.update({"channel name": f"{channel_name}"})
        self.write_to_file(TVar.video_info)
        sleep(1)
        assert self.read_file_data("channel name") == channel_name

    def test_TC_11_get_views_amount_and_write_to_file(self):
        """Gets views amount of played video and writes the value into the json file"""
        self.assert_element_value_equals_file_value(SelectedVideoLocators.views_amount, "views amount", "views_amount")

    def test_TC_12_get_video_upload_date_and_write_to_file(self):
        """Gets upload date of played video and writes the value into the json file"""
        self.assert_element_value_equals_file_value(SelectedVideoLocators.upload_date, "upload date", "upload_date")

    def test_TC_13_get_likes_amount_and_write_to_file(self):
        """Gets likes amount of played video and writes the value into the json file"""
        likes_amount = self.get_nth_element_text_value(SelectedVideoLocators.likes_amount, 0)
        TVar.video_info.update({"likes amount": f"{likes_amount}"})
        self.write_to_file(TVar.video_info)
        sleep(1)
        assert self.read_file_data("likes amount") == likes_amount

