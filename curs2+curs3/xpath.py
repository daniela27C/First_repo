"""
xpath- selecteaza elemente care se afla pe o anumita cale pe care o definim noi
xpath:
          -absolut (descrie toata calea)
          -relativ (porneste de la un element)
                   punem //
                   la xpath putem specifica si textul de pe element fata de selectorii Css   ex: //a[text()='Submit']


 cand vrem sa cautam dupa Id in xpath:   Ex://input[@id='first-name' and @type='text']  #input e type  #la id,clasa,nume punem @
                                            //*[text()='Submit'] - toate elementele


Exista si aici last-of-type //option[last()], first-of-type //option[1], penultimul //option[last()-1]

Comentariu: Css e asemanator cu Xpath, doar ca Xpath iti da optiunea sa cauti dupa text
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#TC: Completarea formularului

# Rezultate asteptate:
# - linkul schimbat in https://formy-project.herokuapp.com/thanks
# - mesaj de succes afisat
# - textul mesajului de succes: The form was successfully submitted!

driver = webdriver.Chrome()
driver.get("https://formy-project.herokuapp.com/form")

driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Mihai")
time.sleep(2)

driver.find_element(By.XPATH, "(//input)[2]").send_keys("Pop")  #ia toate inputurile si de acolo ia al doilea ,daca puneam /input[2] ne refeream la al doilea copil al cuiva si in acest caz de exemplu nu exista
driver.find_element(By.XPATH, "//input[@placeholder='Enter your job title']").send_keys("QA Engineer")
driver.find_element(By.XPATH, "//input[@type='radio' and @value='radio-button-3']").click()
driver.find_element(By.XPATH, "//input[@value='checkbox-1']")

#selectam dupa text pe dropdown
dropdown_select = Select(driver.find_element(By.XPATH, "//select[@id='select-menu']"))
dropdown_select.select_by_visible_text("2-4")

#/ cauta copilul
#/.. cauta parintele sau //parent::type sau //parent::*  -orice tip
# cautam fratele urmator  /following-sibling::type
# cautam fratele anterior  /preceeding-sibling::type

#vrem sa selectam ziua de maine folosind xpath si selectam fratele imediat urmator
driver.find_element(By.XPATH, "//input[@id='datepicker']").click()
driver.find_element(By.XPATH, "//td[@class='today day']/following-sibling::td | //td[@class='today day']/../following-sibling::tr/td[1]").click()   #iar daca today cade duminica si imi trebuie luni : ma duc in parinte tr,apoi in fratele lui,apoi copil td

#gasim butonul submit dupa text
driver.find_element(By.XPATH, "//a[text()='Submit']").click()
time.sleep(1)  #e important aici sa fie time.sleep pentru ca el trece direct pe o alta pagina si nu reuseste sa se incarce si ne poate da eroare

#verificam ca mesajul de succes a fost afisat
success_message = driver.find_element(By.XPATH, "//div[@role='alert']")

#verificam daca s-a schimbat linkul
assert driver.current_url == "https://formy-project.herokuapp.com/thanks", "Eroare, URL-ul este incorect"
#vedem daca mesajul este afisat
assert success_message.is_displayed(), "Eroare, mesajul de succes nu este afisat!"     #ce se pune dupa virgula e mesaj afisat in consola cand testul pica
assert success_message.text == "The form was successfully submitted!", "Eroare, textul de pe element nu este corect"   #luam textul de pe un element, atentie acelasi element deci il salvez intro variabila sus ,aici l-am salvat in succes_message pentru ca interactionam cu el de mai multe ori
time.sleep(3)
driver.quit()