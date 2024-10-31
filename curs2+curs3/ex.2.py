
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(1)

# EX1:
#extragem din lista produsul cu pretul cel mai mic
#span.actual-price in html, unde span e tipul si actual price e clasa
search_box = driver.find_element(By.ID, "small-searchterms")
search_box.send_keys("phone")

button_search = driver.find_element(By.CLASS_NAME, "search-box-button")
button_search.click()

time.sleep(2)

#gasim toate elementele din care vrem sa extragem pr4etul cel mai mic, o lista o cautam cu find elements ,facem cautarea dupa Css
price_list = driver.find_elements(By.CSS_SELECTOR, "span.actual-price")
price_value_list = []

#sunt elemente web deci nu le pot ordona,dar pot lua textul de pe elemente, asa ca parcurg lista cu un for
for element in price_list:
    text = element.text    #iau textul de pe element
    # $300.00
    value = float(text.replace("$", ""))   #observ ca taote preturile au semnul dolar in fata, asa ca scap de el mai intai,apoi le transform in float si le adaug in lista goala
    price_value_list.append(value)         #replace inlocuieste ceva cu ceva intr-un string
                                           #adaugam in lista
price_value_list.sort()                    #sorteaza lista,este ddar o actiune de aia se pune in fata,mai intai sorteaza lista,dupa afisam din nou lista deja sortata

print(price_value_list[0])                 #iau elementul cu indexul 0, cel mai mic element

# EX 2:
#extragem titlul paginii si verificam dca este corect
#driver.title returneaza titlul paginii
#titlul la care ne asteptam "nopCommerce demo store. Search"  il luam din head>title
assert driver.title == "nopCommerce demo store. Search"

# EX 3:
#intrati pe site,accesati butonul cont si click pe conectare.Identificati elementele de tip user si parola si inserati valori incorecte
#in plus verificati ca nu v-ati logat

#accesam pagina de log in
driver.find_element(By.CSS_SELECTOR, "a.ico-login").click()
time.sleep(1)

url_before_login = driver.current_url

driver.find_element(By.ID, "Email").send_keys("pyta14@gmail.com")
driver.find_element(By.ID, "Password").send_keys("12345678")
driver.find_element(By.CSS_SELECTOR, "button.login-button").click()

url_after_login = driver.current_url

expected_error_text = "Login was unsuccessful. Please correct the errors and try again.\nNo customer account found"
#vrem sa verificam ca nu ne-am logat,cel mai simplu mod de a o face e sa verifici daca linkul este acelasi, observam ca atunci cand logarea nu se face se aduga ceva la link dar prima parte e aceaasi,deci verific ca este in
actual_error_text = driver.find_element(By.CSS_SELECTOR, "div.message-error").text

#print(url_before_login)
#print(url_after_login)
#si observam ca intro parte avem U si intro parte u,rezolvam aceasta panand lower pe string

assert url_before_login.lower() in url_after_login.lower(), "Error, unexpected url after click on login button"
assert expected_error_text == actual_error_text, "Error, unexpected error message"


# Ex 4
#stergeti valoarea de pe campul email si introduceti o valoare invalida (adica fara caracterul @),fara sa introduceti si parola si verificati faptul ca butonul de login este dezactivat
#aici pe acest site daca nu punem @ apare mesajul cu wrong email dar care apare dupa ce dau un click in exterior
driver.find_element(By.ID, "Email").clear()   #stergem  mai intai din testul anterior
driver.find_element(By.ID, "Email").send_keys("pyta14")
driver.find_element(By.ID, "Password").click()    #fac click undeva in exterior de exemplu parola ca sa imi afiseze mesajul de eroare weong email, nu scriu nimic,doar ii dau click

email_error = driver.find_element(By.ID, "Email-error")
assert email_error.is_displayed(), "Error, email error message not displayed"
assert email_error.text == "Wrong email", "Unexpected error text"

# EX 5

# TC: Se face o cautare dupa care sortam rezultatee gasite in ordine crescatoare

search_box = driver.find_element(By.ID, "small-searchterms")
search_box.send_keys("phone")

button_search = driver.find_element(By.CLASS_NAME, "search-box-button")
button_search.click()
time.sleep(2)

#cand interactionam cu un dropdown ne folosim de libraria Select
dropdown_sort = Select(driver.find_element(By.ID, "products-orderby"))
dropdown_sort.select_by_visible_text("Price: Low to High")
time.sleep(3)

#am facut mai sus o lista care comtine toate preturile,daca am facut sortarea,lista contine elementele sortate crescator
price_list = driver.find_elements(By.CSS_SELECTOR, "span.actual-price")
price_value_list = []

#lista asta deja trebuie sa fie gata sortata,noi doar taiem dolarul si le facem float
for element in price_list:
    text = element.text
    # $300.00
    value = float(text.replace("$", ""))
    price_value_list.append(value)

#am luat lista am sortat-o si o compar cu lista initiala
price_value_list_initial = list.copy(price_value_list)
price_value_list.sort()

assert price_value_list_initial == price_value_list, "Error, sorting is not working properly"