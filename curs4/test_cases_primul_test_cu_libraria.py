import time
import unittest
from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class TestDemoSite(unittest.TestCase):

    # Declaram locatorii sub forma de tuplu ca sa nu le re-declaram mereu in teste, tuplurile sunt imutabile nu pot schimba ordinea in ele
    # Numele variabilelor le-am scris cu litera mare pt ca sunt constante
    INPUT_EMAIL = (By.ID, "Email")
    INPUT_PASSWORD = (By.ID, "Password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "button.login-button")
    LINK_LOGIN = (By.CSS_SELECTOR, "a.ico-login")
    INPUT_SEARCH = (By.ID, "small-searchterms")
    ERROR_EMAIL = (By.ID, "Email-error")
    BUTTON_SEARCH = (By.CLASS_NAME, "search-box-button")
    PRICE_LIST = (By.CSS_SELECTOR, "span.actual-price")
    ERROR_LOGIN = (By.CSS_SELECTOR, "div.message-error")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("https://demo.nopcommerce.com/")
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    # Medtoda ajutatoare care cauta si returneaza un WebElement dupa un locator dat, face inclusiv despachetarea
    # Despachetarea tuplului (cu steluta) se intampla in interiorul metodei
    def find(self, locator) -> WebElement:
        #Tuplul va fi despachetat deoarece metoda find_element() primeste 2 argumente
        return self.driver.find_element(*locator)

    # Medtoda ajutatoare care cauta si returneaza o lista de WebElemente
    def find_all(self, locator) -> list[WebElement]:
        return self.driver.find_elements(*locator)

    # Metoda ajutatoare pt click pe un element
    def click(self, locator):
        self.find(locator).click()    #il gaseste apoi da click

    # Metoda ajutatoare care scrie pe un element
    def type(self, locator, text):
        self.find(locator).send_keys(text)

#acest testcase verifica daca cel mai mic pret este 100.0
    def test_product_with_lowest_price(self):
        search_box = self.find(self.INPUT_SEARCH)
        search_box.send_keys("phone")

        button_search = self.find(self.BUTTON_SEARCH)
        button_search.click()

        time.sleep(2)

        price_list = self.find_all(self.PRICE_LIST)
        price_value_list = []

        for element in price_list:
            text = element.text
            # $300.00
            value = float(text.replace("$", ""))
            price_value_list.append(value)

        price_value_list.sort()

        # assert price_value_list[0] == 100.0
        self.assertEqual(price_value_list[0], 100.0)

#acest testcase verifica daca titlul paginii este "nopCommerce demo store"
    #atentie nu mai suntem pe search ca si cand faceam exerctiile, pentru ca de data asta folosind aceasta librarie testele sunt independente si noi suntem de fiecare data pe pagina principala
    def test_page_title(self):
        # assert self.driver.title == "nopCommerce demo store. Search"
        self.assertEqual(self.driver.title, "nopCommerce demo store", "Error, incorrect page title!")
#test case care verifica daca introducem o parola si un user care nu sunt identificate ramanem pe pagina de log in
    def test_login_with_invalid_credentials(self):
        # self.driver.find_element(*self.LINK_LOGIN).click()
        self.click(self.LINK_LOGIN)
        time.sleep(1)

        url_before_login = self.driver.current_url

        # self.driver.find_element(*self.INPUT_EMAIL).send_keys("pyta14@gmail.com")
        # self.driver.find_element(*self.INPUT_PASSWORD).send_keys("12345678")
        # self.driver.find_element(*self.BUTTON_LOGIN).click()

        self.type(self.INPUT_EMAIL, "pyta14@gmail.com")
        self.type(self.INPUT_PASSWORD, "12345678")
        self.click(self.BUTTON_LOGIN)

        url_after_login = self.driver.current_url

        expected_error_text = "Login was unsuccessful. Please correct the errors and try again.\nNo customer account found"

        actual_error_text = self.find(self.ERROR_LOGIN).text

        assert url_before_login.lower() in url_after_login.lower(), "Error, unexpected url after click on login button"
        assert expected_error_text == actual_error_text, "Error, unexpected error message"
#testcase cu email invalid, nu avea @
    #atentie, cand faceam ex eram deja pe pag de login din testul precedent,acum nu mai suntem, deci ar trebui mai intai sa deschidem pagina de log in,in plus mai inainte la ex noi mai intai stergeam cu clear ce aveam si dupa introduceam textul,pai acum nu mai avem nevoie de clear
    def test_email_field_validation(self):
        self.click(self.LINK_LOGIN)
        self.type(self.INPUT_EMAIL, "pyta14")
        self.click(self.INPUT_PASSWORD)   #trebuia sa dau un click undeva inafara

        email_error = self.find(self.ERROR_EMAIL)
        assert email_error.is_displayed(), "Error, email error message not displayed"
        assert email_error.text == "Wrong email", "Unexpected error text"