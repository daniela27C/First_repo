import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://primeng.org/dropdown")
time.sleep(1)

dropdown_select = driver.find_element(By.CSS_SELECTOR, "p-dropdown[optionlabel='name']")
# dropdown_select.click()
# time.sleep(1)
#
# option = driver.find_element(By.CSS_SELECTOR, "li[aria-label='Rome']")
# option.click()
# time.sleep(1)

#generalizam totul print-o functie
def select_dropdown_by_text(dropdown: WebElement, text: str, has_search=False):  #text-textul pe care vreau sa il scriu pe el
                                                                                 # : inseamna de tip
    dropdown.click()
    time.sleep(1)

    if has_search:
        dropdown.find_element(By.CLASS_NAME, "p-dropdown-filter").send_keys(text)  #libraria keys ma ajuta sa imitez simulari de taste de exemplu enter
        time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, f"li[aria-label='{text}']").click()

#apelez functia
select_dropdown_by_text(dropdown_select, "Rome")
time.sleep(1)

select_dropdown_by_text(dropdown_select, "New York")
time.sleep(1)

select_dropdown_by_text(dropdown_select, "London")


dropdown_2 = driver.find_element(By.CSS_SELECTOR, "p-dropdown.ng-pristine[filterby='name']")

select_dropdown_by_text(dropdown_2, "China", True)
time.sleep(3)

driver.quit()