# 1. Deschidem browserul și intrăm pe https://magento.softwaretestingboard.com/
# 2. Acceptăm termenii și condițiile
# 3. Căutăm produse după cuvântul “jacket”
# 4. Identificăm primul produs dintre rezultate și facem click pe numele acestuia
# 5. Alegem mărimea XS
# 6. Alegem culoarea gri
# 7. Adaugam produsul in cos
# 8. Validăm (assert) că avem 1 articol în coș
# 9. Facem click pe cos
# 10. Validăm (assert) că numele produsului din coș coincide cu numele produsului din pagină
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# 1. Deschidem browserul și intrăm pe https://magento.softwaretestingboard.com/
driver = webdriver.Chrome()
driver.get("https://magento.softwaretestingboard.com/")

# 2. Acceptăm termenii și condițiile
driver.find_element(By.CLASS_NAME, "fc-cta-consent").click()

# 3. Căutăm produse după cuvântul “jacket”
# Keys.ENTER simuleaza apasarea tastei Enter
# si va cauta direct cuvantul scris inaintea lui
driver.find_element(By.ID, "search").send_keys("jacket" + Keys.ENTER)     #find element ia primul element mereu sau puneam find elements si puneam [1]

# 4. Identificăm primul produs dintre rezultate și facem click pe numele acestuia
# Aici chiar daca locatorul "bate" spre mai multe elemente,
# daca folosim driver.find_element (nu driver.find_elements),
# selenium va returna fix prmul element din HTML
driver.find_element(By.CLASS_NAME, "product-item-link").click()

# 5. Alegem mărimea XS
driver.find_element(By.XPATH, "//div[@aria-label='XS']").click()

# 6. Alegem culoarea gri
driver.find_element(By.CSS_SELECTOR, "div[aria-label='Gray']").click()

# 7. Adaugam produsul in cos
driver.find_element(By.ID, "product-addtocart-button").click()

# Facem un locator de tip tuplu pentru numarul de articole din cos (pt ca il vom folosi de mai multe ori)
COUNTER_LOCATOR = (By.CLASS_NAME, "counter-number")

# Facem un wait explicit pana cand textul "1" apare pe elementul COUNTER_LOCATOR
wait = WebDriverWait(driver, 3)
wait.until(expected_conditions.text_to_be_present_in_element(COUNTER_LOCATOR, "1"))

# Luam cantitatea reala (din site) de produse din cos ca sa o validam
quantity = driver.find_element(*COUNTER_LOCATOR).text

# 8. Validăm că avem 1 articol în coș
assert quantity == "1", f"Wrong quantity. \nExpected: 1, \nActual: {quantity}"

# 9. Facem click pe cos
# Aici am ales sa facem click pe nr-ul de langa cos, deoarece deschide acelasi pop-up
driver.find_element(*COUNTER_LOCATOR).click()

# Luam textul produsului din pagina si textul produsului din cos
product_name_in_page = driver.find_element(By.CSS_SELECTOR, "[itemprop='name']").text
product_name_in_cart = driver.find_element(By.CSS_SELECTOR, "[class='product-item-name']").text

# 10. Validăm că numele produsului din coș coincide cu numele produsului din pagină
assert product_name_in_page == product_name_in_cart, "Add to cart validation failed."

time.sleep(3)


