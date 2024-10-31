lista = [1, "a", True, "2"]
print(lista)

print(*lista)  #vreau lista despachetata, fara paranteze, fara virgule, fara ghilimele


def suma(a, b):
    return a+b

print(suma(5,5))
#vreau nr indefinit de parametri si ma pot folosi de despachetare
def suma_numere(*numere):
    suma = 0
    for numar in numere:
        # suma = suma + numar
        suma += numar
    return suma


lista_2 = [1, 2, 3, 4, 5, 6, 45, 35, 435, 345, 345, 34, 345]

print(suma_numere(*lista_2))   #despachetez lista

lista_3 = [1, 2, 3]

print(suma_numere(*lista_3))