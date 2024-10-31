# pip install selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()    #driver este o variabila
                               #din modulul webdriver ne folosim de clasa Chrome()
driver.get("https://demo.nopcommerce.com/")   #driver.get ne va duce pe un anumit link, link-ul se da sub forma de string
time.sleep(1)
#ca sa caut un element de exemplu dupa id:
#1.command+f
#2.[id=small-searchterms]

#gasim elementele
search_box = driver.find_element(By.ID, "small-searchterms")   #search_box este o variabila de tip web element
                                                                     #pe browser care aici e driver apelez functia find_element(By.ID- tipul de selector pe care vreau sa il folosesc, "small-searchterms"-valoarea id-ului sub forma de string)
search_box.send_keys("phone")   #introduc un text in search box-ul respectiv apeland functia send_keys pe variabila search_box
time.sleep(1)


#identificam acelasi element dar dupa clasa
#scriem direct numele clasei acolo la cautare fara []
search_box_2 = driver.find_element(By.CLASS_NAME, "search-box-text")
search_box_2.clear()    #sterge elementul la sfarsit
time.sleep(1)

#identificam acelasi element dar dupa name
search_box_3 = driver.find_element(By.NAME, "q")
search_box_3.send_keys("phone")
time.sleep(1)


#putem identifica un element dupa textul de pe link
#Atentie! textul din HTML nu din pagina web, apare cu alb
#Daca dadeam cum e in pagina web aveam eroarea NoSuchElementException-nu exista un astfel de element
link_register = driver.find_element(By.LINK_TEXT, "Register")
link_register.click()  #sa dea click pe link
time.sleep(1)

#un alt tip de selecr Partial Link Text care ne permite sa nu dau tot textul de pe link ci doar o parte
digital_downloads_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Digital")
digital_downloads_link.click()
time.sleep(1)

#scriem phone dupa ce am dat click pe pagina Digital Dowlands
#search_box.send_keys("phone")   da eroare StaleElementReferenceException pentru ca pagina mea se reincarca,plec practic de pe pagina si elementul nu mai este disponibil
#deci daca vreau sa interactionez din nou cu elementul trebuie sa ii dau refresh, adica sa reegalez cu ceva, trebuie sa il gasesc dupa oricare din cele metode
search_box = driver.find_element(By.ID, "small-searchterms")

#caut un element dupa clasa picture si stiu ca sunt mai multe elemente cu acea clasa
element_picture = driver.find_element(By.CLASS_NAME, "picture")
# element_picture.click()    #dau click pe el si daca nu specificam al catalea atunci tot timpul o sa interactioneze cu primul element

#vreau toate elementele atunci in loc de find element, folosesc find elements cu s la final
#diferente intre find element si find elements
#1. find element returneaza primul element gasit si find elements returneaza toata lista cu elemente
#2. daca find element nu gaseste un element se da eroarea NoSuchElementException, iar daca find elements nu gaseste nimic da o lista goala
# Lista cu elementele care au clasa "picture"
lista_elemente = driver.find_elements(By.CLASS_NAME, "picture")
print(len(lista_elemente))   #verific ca mi le-a dat pe toate 3

#vreau sa interactionez cu al doilea element
lista_elemente[1].click()

#verific ca intr-adevar ca daca find elements nu gaseste nimic da o lista goala
lista_2 = driver.find_elements(By.ID, "id_inexistent_in_pagina")
print(len(lista_2))

time.sleep(5)


# Assert verifica o expresie la care se asteapta sa fie True
# Daca expresia nu este adevarata, atunci programul se va opri si da eroarea AssertionError
assert 3 + 2 == 5, "Expresia este falsa"

print("Am trecut de assert")


driver.quit()   #inchidem driver-ul