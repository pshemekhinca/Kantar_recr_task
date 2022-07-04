import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.locators import YTHomeLocators as YTHome
from pages.YT_home_page import HomePage


class BaseTest(unittest.TestCase):
    """Base test class is created to reuse all methods common for all tested pages"""

    @classmethod
    def setUpClass(self):
        """Setup method to prepare entry settings before each test set/file"""
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.home_page = HomePage(self.driver)
        print('Class driver initialized')

    @classmethod
    def tearDownClass(self):
        """TearDown method to quit browser session after each test set/file run"""
        self.driver.quit()
        print('Class driver finished')

    def click_element(self, element_xpath):
        """Click action on given button xpath element
                :param button_xpath: given button xpath
        """
        self.visibility_of_element_wait(self.driver, element_xpath)
        elem = self.driver.find_element(By.XPATH, element_xpath)
        elem.click()

    def assert_if_element_is_visible(self, element_xpath):
        """Checks if web element is displayed
        :param element_xpath: element xpath to look for
        """
        self.assertTrue(self.driver.find_element(By.XPATH, element_xpath), f'Element not found')

    def skip_popup(self, xpath_element):
        """Skips cookies prompt"""
        consent = self.driver.find_element(By.XPATH, xpath_element)
        consent.click()

    def visibility_of_element_wait(self, driver, xpath, timeout=10) -> WebElement:
        """Check if element specified by xpath is visible on page
                  :param driver: webdriver or event firing webdriver instance
                  :param xpath:  web element xpath
                  :param timeout: after timeout waiting will be stopped (default: 10)
                  :return found element
        """
        locator = (By.XPATH, xpath)
        element_located = EC.visibility_of_element_located(locator)

        if hasattr(driver, 'wrapped_driver'):
            unwrapped_driver = driver.wrapped_driver
            wait = WebDriverWait(unwrapped_driver, timeout)
        else:
            wait = WebDriverWait(driver, timeout)
        return wait.until(element_located, f"Element for xpath: '{xpath}'and url: {driver.current_url} not found")


