import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestElementIsVisible(unittest.TestCase):

    BUTTON_START = (By.XPATH, "//button[text()='Start']")
    DIV_FINISH = (By.ID, "finish")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    def tearDown(self):
        self.driver.quit()

    def find(self, locator) -> WebElement:
        return self.driver.find_element(*locator)

    def wait_for_element_presence(self, locator, seconds):
        wait = WebDriverWait(self.driver, seconds)
        wait.until(EC.visibility_of_element_located(locator))

    def test_verify_element_is_displayed(self):
        self.find(self.BUTTON_START).click()
        self.wait_for_element_presence(self.DIV_FINISH, 10)
        assert self.find(self.DIV_FINISH).is_displayed()