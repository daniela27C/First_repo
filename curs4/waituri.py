# Waituri
#driver.impicitly wait(6)    asteapta maxim  6 sec cand se foloseste de find element
#wait explixit se aplica o singura data pentru un singur element, nu se foloseste doar pentru find
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
driver.maximize_window()

# EXERCITIU Wait Implicit
# - Click pe butonul "Change Text to Selenium Webdriver"
# - Dupa 10 secunde textul "site" se va schimba in "Selenium Webdriver"
# - Vom folosi un implicit wait pentru a face driverul sa astepte maxim 11 secunde inainte sa dea eroare
driver.find_element(By.ID, "populate-text").click()
time.sleep(10)
driver.implicitly_wait(20)
element_gasit = driver.find_element(By.XPATH, "//h2[text()='Selenium Webdriver']")

driver.implicitly_wait(0)
# element_gasit_2 = driver.find_element(By.XPATH, "//h2[text()='Selenium Webdriver INEXISTENT']")

# EXERCITIU Wait Explicit
# Deoarece elementul se afla deja in pagina si este invizibil,
# wait-ul implicit nu ne ajuta
# Vom folosi un wait explicit care asteapta ca elementul sa devina vizibil
hidden_button = driver.find_element(By.ID, "hidden")    #de gasit il gaseste,dar nu poate da click pe el, in acest moment implicit nici nu ma ajuta cu ceva ca el asteapta pana cand apare, dar el de aparut apare in cod html,dar nu pot sa il vad pe pagina decat dupa un timp si respectiv nu pod interactiona cu el

driver.find_element(By.ID, "display-other-button").click()   #trebuie mai intai sa dau click ca se porneasca numararea

# Declarare wait explicit - inca nu se declanseaza procesul de asteptare
wait = WebDriverWait(driver, 20)   #declaram o variabila numita wait care este o instanta a clasei WebDriverWait

# Aici incepem sa asteptam
wait.until(expected_conditions.visibility_of(hidden_button))   #expected_conditions este o librarie

hidden_button.click()