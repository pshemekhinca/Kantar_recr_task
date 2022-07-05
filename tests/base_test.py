import unittest
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.locators import *
from pages.YT_home_page import HomePage
from pages.YT_results_list_page import ResultsListPage
from selenium.webdriver.common.action_chains import ActionChains


class BaseTest(unittest.TestCase):
    """Base test class is created to reuse all methods common for all tested pages"""

    @classmethod
    def setUpClass(self):
        """Setup method to prepare entry settings before each test set/file"""
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.home_page = HomePage(self.driver)
        self.results_list_page = ResultsListPage(self.driver)
        print('Class driver initialized')

    @classmethod
    def tearDownClass(self):
        """TearDown method to quit browser session after each test set/file run"""
        self.driver.quit()
        print('Class driver finished')

    def click_element(self, element_xpath):
        """Click action on given button xpath element
                :param element_xpath: given button xpath
        """
        self.visibility_of_element_wait(self.driver, element_xpath)
        elem = self.driver.find_element(By.XPATH, element_xpath)
        try:
            elem.click()
        except StaleElementReferenceException as Exception:
            print('StaleElementReferenceException while trying to CLICK element, trying to find element again')
            elem = self.driver.find_element(By.XPATH, element_xpath)
            elem.click()

    def assert_if_element_is_visible(self, element_xpath):
        """Checks if web element is displayed
        :param element_xpath: element xpath to look for
        """
        self.assertTrue(self.driver.find_element(By.XPATH, element_xpath), f'Element not found')

    def skip_popup(self, element_xpath):
        """Skips cookies prompt
        :param element_xpath: given accept button xpath
        """
        accept_button = self.driver.find_element(By.XPATH, element_xpath)
        try:
            accept_button.click()
        except NoSuchElementException:
            print('NoSuchElementException while trying to CLICK accept, trying to find element again')
            accept_button = self.driver.find_element(By.XPATH, element_xpath)
            accept_button.click()

    def send_text_to_input_field(self, input_field_xpath, input_text):
        """Fill selected input field with given text
                :param input_field_xpath: given input field xpath
                :param input_text: text to fill with
                :return: self
        """
        input_field = self.driver.find_element(By.XPATH, input_field_xpath)
        input_field.send_keys(input_text)
        try:
            input_field.send_keys(input_text)
        except NoSuchElementException:
            print('NoSuchElementException while trying to SEND INPUT to element, trying to find element again')
            input_field = self.driver.find_element(By.XPATH, input_field_xpath)
            input_field.send_keys(input_text)
        return self

    def enter_data_and_click(self, input_field_xpath, input_text, button):
        """Fill selected input field with given text and click the button
                :param input_field_xpath: given input field xpath
                :param input_text: text to fill with
                :param button: button xpath passed to click_button method
        """
        self.driver.find_element(By.XPATH, input_field_xpath).clear()
        self.send_text_to_input_field(input_field_xpath, input_text)
        self.click_element(button)

    def get_element_text_value(self, element_xpath):
        """Gets text value of web element
                :param element_xpath: webpage element xpath
                :return: element text value
        """
        try:
            self.visibility_of_element_wait(self.driver, element_xpath)
            return self.driver.find_element(By.XPATH, element_xpath).text
        except TimeoutException:
            print('TimeoutException while trying to get element TEXT value, trying to find element again')
            self.visibility_of_element_wait(self.driver, element_xpath)
            return self.driver.find_element(By.XPATH, element_xpath).text

    def get_nth_element_text_value(self, elements_xpath, idx):
        """Gets text value of selected web element from elements list
                :param elements_xpath: webpage elements xpath
                :param idx: element index in the list
                :return: element text value
        """
        self.visibility_of_element_wait(self.driver, elements_xpath)
        try:
            element = self.driver.find_elements(By.XPATH, elements_xpath)[idx]
            return element.text
        except StaleElementReferenceException:
            print('StaleElementReferenceException while trying to get element value, trying to find element again')
            element = self.driver.find_elements(By.XPATH, elements_xpath)[idx]
            return element.text

    def get_duration_time(self, xpath):
        """Gets text value of video duration
                :param elements_xpath: webpage elements xpath
                :return: duration text value
        """
        self.visibility_of_element_wait(self.driver, xpath)
        video_duration = self.get_element_text_value(xpath)
        return video_duration

    def click_nth_list_element(self, elements_xpath, idx):
        """Click nth element from elements list
                :param element_xpath: webpage elements xpath
                :param idx: element index in the list
        """
        self.visibility_of_element_wait(self.driver, elements_xpath)
        elements_list = self.driver.find_elements(By.XPATH, elements_xpath)[idx]
        el_x = f'//*[@class="style-scope ytd-video-renderer" and contains(text(),"{elements_list.text}")]'
        try:
            self.click_element(el_x)
        except:
            self.visibility_of_element_wait(self.driver, elements_xpath)
            self.click_element(el_x)

    def time_to_seconds(self, time_format):
        """Converts time format into seconds
                :param time_format: given time format
                :param return: time in total seconds amount
        """
        convertion = sum(x * int(t) for x, t in zip([3600, 60, 1], time_format.split(":")))
        return convertion

    def move_slider(self, element_xpath):
        move = ActionChains(self.driver)
        slider = self.driver.find_element(By.XPATH, element_xpath)
        move.drag_and_drop_by_offset(slider, 70, 0).perform()


    def visibility_of_element_wait(self, driver, element_xpath, timeout=10) -> WebElement:
        """Waits until element specified by xpath is visible on page
                  :param driver: webdriver or event trigger webdriver instance
                  :param element_xpath:  web element xpath
                  :param timeout: after timeout waiting will be stopped (default: 10)
                  :return found element
        """
        locator = (By.XPATH, element_xpath)
        element_located = EC.visibility_of_element_located(locator)

        if hasattr(driver, 'wrapped_driver'):
            unwrapped_driver = driver.wrapped_driver
            wait = WebDriverWait(unwrapped_driver, timeout)
        else:
            wait = WebDriverWait(driver, timeout)
        return wait.until(element_located,
                          f"Element for xpath: '{element_xpath}'and url: {driver.current_url} not found")

    def invisibility_of_element_wait(self, driver, element_xpath, timeout=10) -> WebElement:
        """Waits until element specified by xpath disappears
                  :param driver: webdriver or event trigger webdriver instance
                  :param element_xpath:  web element xpath
                  :param timeout: after timeout waiting will be stopped (default: 10)
                  :return found element
        """
        locator = (By.XPATH, element_xpath)
        element_dissapear = EC.invisibility_of_element_located(locator)

        if hasattr(driver, 'wrapped_driver'):
            unwrapped_driver = driver.wrapped_driver
            wait = WebDriverWait(unwrapped_driver, timeout)
        else:
            wait = WebDriverWait(driver, timeout)
        return wait.until(element_dissapear,
                          f"Element for xpath: '{element_xpath}'and url: {driver.current_url} not found")

