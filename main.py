import unittest
from selenium import webdriver
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

first_name = "Kris"
last_name = "Krisowy"

class TestRoweria(unittest.TestCase):
    def setUp(self):
        """
        Warunki wstepne
        """
        #przegladarka wlaczona
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://roweria.pl")


    def testDoProjektu(self):

        """
        TC = 01: testowanie strony roweria.pl - zalogowanie
        """

        driver = self.driver

        znajdz_zaloguj = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="account_link link hidden-phone"]'))).click()

        #znajdz_zaloguj_sie = driver.find_element_by_xpath('//a[@class="account_link link hidden-phone"]').click()


        znajdz_buton = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="btn signin-form_register2"]'))).click()

        #znajdz_nowe_k = driver.find_element_by_xpath('//a[@class="btn signin-form_register2"]').click()

        wybierz_firma = driver.find_element_by_xpath('//input[@id="client_type1"]').click()

        firstName = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'client_firm'))).send_keys(first_name)








        #ceke debagowe
        time.sleep(8)

    def tearDown(self):
        """
        sprzatanie po tescie
        """
        self.driver.quit()




if __name__=='__main__':
    unittest.main(verbosity=2)
