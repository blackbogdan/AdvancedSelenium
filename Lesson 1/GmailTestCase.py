#this import is for datetime.now()
from datetime import datetime
from time import gmtime, strftime
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class GMailTests(unittest.TestCase):

    def setUp(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        url = "https://mail.google.com"
        driver.get(url)

        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    def tearDown(self):
        self.driver.quit()

    def test_send_mail(self):
        my_email = '1bogdankapusta@gmail.com'

        driver = self.driver
        subject="selenium Class: {0}".format(str(datetime.now()))

        driver.find_element_by_id('Email').send_keys(my_email)
        # driver.find_element_by_css_selector('#Email')

        driver.find_element_by_name('signIn').click()

        self.wait.until(
                EC.visibility_of_element_located(
                        (By.ID, 'Passwd'))).send_keys('HUYpizda12')
        driver.find_element_by_id('signIn').click()

        driver.find_element_by_xpath("//div[text()='COMPOSE']").click()

        if not driver.find_element_by_css_selector('[name="to"]').is_displayed():
            driver.find_element_by_xpath('//*[text()="Recipients"]').click()

        driver.find_element_by_css_selector('[name="to"]').send_keys(my_email)

        driver.find_element_by_xpath('//*[@aria-label="Subject"]').send_keys(subject)
        #added "AO" to classname, because classname changes after mouseclick
        # driver.execute_script('document.getElementById(":e5").className += " Ao"')
        # driver.find_element_by_xpath('//*[@role="textbox"]').\
        #     send_keys("Come on you young sailor men listen to me,\n I'll sing you a song of the fish in the sea")
        textbox = driver.find_element_by_xpath('//*[@role="textbox"]')
        #another workaround for sending keys to body. args[0] because the first argument

        driver.execute_script('arguments[0].textContent="that is it"', textbox)

        driver.find_element_by_xpath('//*[contains(text(),"Send")]').click()
        #new webdriver, waits for 2 minst with encrement of 500ms
        # WebDriverWait(driver,120).until(EC.visibility_of_element_located((By.XPATH, "//b[text='{0}'".format(subject))))

        #need to use while loop, because, page should be refreshed
        start = int(strftime("%M", gmtime()))


        while int(strftime("%M", gmtime())) < start + 120:
            try:
                driver.find_element_by_xpath(".//b[text()='{0}'".format(subject))
                break
            except:
                driver.find_element_by_partial_link_text('Inbox').click()

        else:
            assert False, "The email did not arrive within expected 2 minutes"

        #verify that email came to the point
        print('Done')



