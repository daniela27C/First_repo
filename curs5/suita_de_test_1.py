"""Suitele de teste sunt utile din doua puncte de vedere:

Sa putem sa rulam mai multe clase in acelasi timp
Sa specificam configuratia pentru raportul de executie

n interiorul acestei clase vom avea o metoda numita test_suite care sa contina un obiect instantiat din clasa TestSuite:

test_de_rulat = unittest.TestSuite()"""

import unittest

import HtmlTestRunner

from HtmlTestRunner.result import HtmlTestResult

from curs5.js_alerts import TestAlerts
from curs5.test_register_page import TestRegisterPage
from curs5.test_wait_for_presence import TestElementIsPresent
from curs5.test_wait_for_visibility import TestElementIsVisible
from main import TestKeys


class TestSuite(unittest.TestCase):

    def test_suite(self):

        teste_de_rulat = unittest.TestSuite()

        #teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts))
        # teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestKeys))
        # teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestRegisterPage))
        # teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestElementIsPresent))
        # teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestElementIsVisible))

        # Adaugam in suita <teste_de_rulat> toate clasele de test
        # create in aceasta sesiune
        teste_de_rulat.addTests(
            [
                # intre paranteze vine exact numele clasei de test
                #unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts),
                #unittest.defaultTestLoader.loadTestsFromTestCase(TestKeys),
                #unittest.defaultTestLoader.loadTestsFromTestCase(TestRegisterPage),
                unittest.defaultTestLoader.loadTestsFromTestCase(TestElementIsPresent),
                unittest.defaultTestLoader.loadTestsFromTestCase(TestElementIsVisible)
            ]
        )

        # instalam pip install html-testRunner
        runner = HtmlTestRunner.HTMLTestRunner(
            #output="reports/",  # Specifică directorul pentru raport
            combine_reports=True,
            report_title="Test Report PYTA14",
            report_name="Smoke test result"
        )

        runner.run(teste_de_rulat)

#Smoke test result_2024-04-21_18-01-53.html