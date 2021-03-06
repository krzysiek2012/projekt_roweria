#!/usr/bin/python3
import unittest
from selenium import webdriver
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

firma = "Kris"
nip_code = "Krisowy"
ulica = "Krisowa"
kod = "xx"
miasto = "Olesnica"
imie = "Krisek"
nazwisko = "Olo"
i_majl = "kiko@gmail.com"
fon = "123456789"
logyn = "okimoki"
haslo = "123kokoK456"

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

        Firma = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'client_firm'))).send_keys(firma)

        NIP = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'client_nip'))).send_keys(nip_code)

        Street = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'client_street'))).send_keys(ulica)

        Postal = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'client_zipcode'))).send_keys(kod)

        City = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'client_city'))).send_keys(miasto)

        #przewijam stronę na dół
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3.5);window.scrollTo(0, document.body.scrollHeight/3.7);")

        Firsname = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'client_firstname'))).send_keys(imie)

        Surname = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'client_lastname'))).send_keys(nazwisko)

        Wrong_mail = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'client_email'))).send_keys(i_majl)

        newsletter = driver.find_element_by_xpath('//input[@id="client_mailing"]').click()

        tele = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'client_phone'))).send_keys(fon)

        login = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'client_login'))).send_keys(logyn)

        haslo_1 = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'client_password'))).send_keys(haslo)

        haslo_2 = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'repeat_password'))).send_keys(haslo)

        akceptacja = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="terms_agree"]')))

        driver.execute_script("arguments[0].click();", akceptacja)

        zarejestruj = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="submit_clientnew_form"]'))).click()

        #akcept_warunki = driver.find_element_by_xpath('//input[@id="terms_agree"]')

        #drive.execute_script("arguments[0].click();", akcept_warunki)
        bledy = driver.find_elements_by_xpath('//div[@class="menu_messages_warning_sub"]/p[text()="Niepoprawny kod pocztowy."]')

        visible_error_noticed = []

        for error in bledy:
            if error.is_displayed():
                visible_error_noticed.append(error)

        assert len(visible_error_noticed) == 1

        error_text = visible_error_noticed[0].get_attribute("innerText")
        assert error_text == "Niepoprawny kod pocztowy."

        #ceke debagowe
        time.sleep(5)

    def tearDown(self):
        """
        sprzatanie po tescie
        """
        self.driver.quit()




if __name__=='__main__':
    unittest.main(verbosity=2)
