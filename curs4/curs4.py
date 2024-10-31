#libraria unitTest ajuta ca sa putem crea test case separate in acelasi fisier,sa le rulam unul dupa altul, fara ca sa se opreasca daca unul din teste pica
#Metoda setUp o sa contina bucati de cod care trebuiesc rulate inainte de fiecare test
#Metoda tearDown cod pentru a inchide sesiunea curenta ca sa avem browser nou pentru fiecare test
#Metoda de test care au prefixul test


import unittest

#mostenim din libraria unitTest clasa TestCase
class TestDemo(unittest.TestCase):

    def setUp(self):
        print("Se ruleaza metoda setUp()")

    def tearDown(self):
        print("Se ruleaza metoda tearDown()")

    @unittest.skip # va sari peste acest test
    def test_1(self):
        print("Test 1")
        print("Pas 1")
        print("Pas 2")
        print("Pas 3")
        self.metoda_auxiliara()

        assert 1 + 1 == 2, "Eroare, expresia nu este adevarata"

    def test_2(self):
        print("Test 2")
        print("Pas 1")
        print("Pas 2")
        print("Pas 3")

        # assert 1 + 1 == 3, "Eroare, expresia nu este adevarata"
        self.assertEqual(1+1, 3, "Eroare, expresia nu este adevarata")  #noi mostenim si alte functii din aceasta clasa pe care le putem folosi

    def test_3(self):
        print("Test 3")
        print("Pas 1")
        print("Pas 2")
        print("Pas 3")
        self.metoda_auxiliara()

        self.assertTrue(3+5==10, "Text eroare")


    def test_4(self):
        print("Test 4")
        print("Pas 1")
        print("Pas 2")
        print("Pas 3")

        lista = [1, 2, 3, 4]

        self.assertIn(8, lista, "Text eroare")

    def metoda_auxiliara(self):
        print("Se ruleaza metoda auxiliara...")

#testele mai pot fi rulate din terminal daca accesam:  python -m unittest

