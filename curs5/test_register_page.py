import random
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class TestRegisterPage(unittest.TestCase):

    INPUT_FIRST_NAME = (By.ID, "FirstName")
    INPUT_LAST_NAME = (By.ID, "LastName")
    INPUT_EMAIL = (By.ID, "Email")
    INPUT_PASSWORD = (By.ID, "Password")
    INPUT_CONFIRM_PASSWORD = (By.ID, "ConfirmPassword")
    BUTTON_REGISTER = (By.ID, "register-button")
    DIV_SUCCESS_MESSAGE = (By.CLASS_NAME, "result")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demo.nopcommerce.com/register")

    def tearDown(self):
        self.driver.quit()

    def find(self, locator) -> WebElement:
        return self.driver.find_element(*locator)

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def test_page_title(self):
        expected_title = "nopCommerce demo store. Register"  #in head avem title in html
        actual_title = self.driver.title     #avem proprietatatea title care se uita la titlul paginii curente si returneaza un string
        self.assertEqual(expected_title, actual_title, "Unexpected title")

    def test_page_url(self):
        expected_url = "https://demo.nopcommerce.com/register"
        actual_url = self.driver.current_url     #avem proprietatea current url
        self.assertEqual(expected_url, actual_url, "Unexpected page url")

    def test_register_function_with_valid_data(self):
        self.type(self.INPUT_FIRST_NAME, "PY")
        self.type(self.INPUT_LAST_NAME, "TA")
        email_address_number = random.randint(0, 99999999999999999999)     #generam random o adresa de mail intre cat si cat
        self.type(self.INPUT_EMAIL, f"pyta14_{email_address_number}@gmail.com")
        self.type(self.INPUT_PASSWORD, "12345678")
        self.type(self.INPUT_CONFIRM_PASSWORD, "12345678")

        self.find(self.BUTTON_REGISTER).click()

        assert self.find(self.DIV_SUCCESS_MESSAGE).is_displayed()