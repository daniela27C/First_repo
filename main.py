import time
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestKeys(unittest.TestCase):

    INPUT_ID = (By.ID, "username")

    def test_keys(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/login")

        input_username = self.driver.find_element(*self.INPUT_ID)

        input_username.send_keys("tomsmith")
        time.sleep(1)

        input_username.send_keys(Keys.CONTROL + "A")
        time.sleep(1)
        input_username.send_keys(Keys.DELETE)
        time.sleep(1)

        input_username.send_keys("tomsmith134567")
        input_username.send_keys(Keys.ARROW_LEFT)
        input_username.send_keys(Keys.ARROW_LEFT)
        input_username.send_keys(Keys.ARROW_LEFT)
        input_username.send_keys(Keys.ARROW_LEFT)
        input_username.send_keys(Keys.ARROW_LEFT)
        input_username.send_keys(Keys.ARROW_LEFT)
        time.sleep(2)

        input_username.send_keys(6*Keys.ARROW_RIGHT)
        time.sleep(2)

        input_username.send_keys(6*"A")
        time.sleep(2)

        self.driver.quit()