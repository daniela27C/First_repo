#Un Css este un sir de caractere folosit pentru identificarea unui element folosind-une
#de propritatile pe care le are elementele (mai mult clasele)
#input.clasa     putem si input.clasa.clasa
#input#id
#input[atribut]
#input[id=small-searchterms]

#intre frati cum ar fi putem folosi: first-of-type
                                   # last-of-type
                                   # nth-of-type(3)
                                   # +  fratele urmator

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")

# search_box = driver.find_element(By.CSS_SELECTOR, "#small-searchterms")   #este echivalent cu cel de cautare dupa id
# search_box.send_keys("phone")

#putem face direct si fara sa salvam totul intro variabila daca interactionam o singura data
driver.find_element(By.CSS_SELECTOR, "#small-searchterms").send_keys("phone")
time.sleep(1)

#vreau sa caut dupa Css un element de tip input care are atributul name=q
driver.find_element(By.CSS_SELECTOR, "input[name='q']").clear()

#selector cu 2 perechi de atribut-valoare
driver.find_element(By.CSS_SELECTOR, "input[type='text'][placeholder='Search store']").send_keys("Laptop")
time.sleep(1)


#navigam pe o alta pagina pe care avem select
driver.get("https://formy-project.herokuapp.com/form")
time.sleep(1)

#de pe un dropdown putem selecta in 3 feluri:dupa index, dupa textul de pe optiune, dupa atributul value
dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#select-menu"))
dropdown.select_by_visible_text("2-4")  #apelez functia select_by_visible_text pe variabila noastra si pun exact ce vreau sa selectez din cod html
time.sleep(1)

#selectam dupa index
dropdown.select_by_index(1)
time.sleep(1)

#selectam dupa valoare
dropdown.select_by_value("4")
time.sleep(3)





driver.quit() #inchidem procesul