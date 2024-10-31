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


"""#libraria keys este o librarie prin intermediul careia putem introduce o simulare a tastelor direct prin intermediul automatizarii.
#Ca sa putem sa folosim aceasta librarie ne folosim de importul urmator: from selenium.webdriver.common.keys import Keys

import time
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

#metoda de test, data asta nu mai facem set-up si tear-down pentru ca avem un singur test

class TestKeys(unittest.TestCase):

    INPUT_ID = (By.ID, "username")

    def test_keys(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/login")

        input_username = self.driver.find_element(*self.INPUT_ID)

        input_username.send_keys("tomsmith")
        time.sleep(1)

#vreau sa sterg continutul textului pe care l-am scris cu simulari de taste
        #input_username.send_keys(Keys.CONTROL + "A")
        input_username.send_keys(Keys.COMMAND + "A")

        time.sleep(1)
        input_username.send_keys(Keys.DELETE)
        time.sleep(1)

#vreau sa ma duc la stanga cu 6 pozitii
        input_username.send_keys("tomsmith134567")
        input_username.send_keys(Keys.ARROW_LEFT)
        input_username.send_keys(Keys.ARROW_LEFT)
        input_username.send_keys(Keys.ARROW_LEFT)
        input_username.send_keys(Keys.ARROW_LEFT)
        input_username.send_keys(Keys.ARROW_LEFT)
        input_username.send_keys(Keys.ARROW_LEFT)
        time.sleep(2)
#sau
        input_username.send_keys(6*Keys.ARROW_RIGHT)
        time.sleep(2)

        input_username.send_keys(6*"A")
        time.sleep(2)

        self.driver.quit()
"""

