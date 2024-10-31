import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class TestAlerts(unittest.TestCase):

#locatori pentru fiecare buton
    BUTTON_JS_ALERT = (By.CSS_SELECTOR, "button[onclick='jsAlert()']")
    BUTTON_JS_CONFIRM = (By.CSS_SELECTOR, "button[onclick='jsConfirm()']")
    BUTTON_JS_PROMPT = (By.CSS_SELECTOR, "button[onclick='jsPrompt()']")
    TEXT_RESULT = (By.ID, "result")

    def find(self, locator) -> WebElement:
        return self.driver.find_element(*locator)

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    def tearDown(self) -> None:
        self.driver

    def test_accept_simple_alert(self):
        self.find(self.BUTTON_JS_ALERT).click()
        alert = self.driver.switch_to.alert    #cauta daca exista o alerta JS in pagina mea
        time.sleep(1)

        alert.accept()

        expected_text = "You successfully clicked an alert"
        actual_text = self.find(self.TEXT_RESULT).text     #luam textul de pe element

        self.assertEqual(expected_text, actual_text, "Unexpected text")

    def test_dismiss_alert(self):
        self.find(self.BUTTON_JS_CONFIRM).click()
        alert = self.driver.switch_to.alert
        time.sleep(1)

        alert.dismiss()

        expected_text = "You clicked: Cancel"
        actual_text = self.find(self.TEXT_RESULT).text

        self.assertEqual(expected_text, actual_text, "Unexpected text")


    def test_js_alert_with_prompt(self):
        self.find(self.BUTTON_JS_PROMPT).click()
        time.sleep(1)

        alert = self.driver.switch_to.alert
        time.sleep(1)

        text_alerta = "pyta14@gmail.com"

        alert.send_keys(text_alerta)
        time.sleep(1)
        alert.accept()

        expected_text = "You entered: " + text_alerta
        actual_text = self.find(self.TEXT_RESULT).text

        self.assertEqual(expected_text, actual_text, "Unexpected text")