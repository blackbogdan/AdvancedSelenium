import unittest
from selenium import webdriver
import time
class Send_myself_an_email(unittest.TestCase):


    def setUp(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        url = 'https://www.google.com/gmail/about'
        driver.get(url)
        self.driver = driver


    def tearDown(self):
        self.driver.quit()


    def test_itself(self):
        driver = self.driver
        login = "1bogdankapusta@gmail.com"
        password = "Huypizda12"
        subject = "My test MIUKAAAA"
        body_text = "come on you young sailormen listen to me"
        sign_in_xpath = '//a[@data-g-label="Sign in"]'
        email_xpath = '//input[@id="Email"]'
        next_button_xpath = '//input[@id="next"]'
        pwd_field_xpath = '//input[@id="Passwd"]'
        sign_in_button_xpath = '//input[@id="signIn"]'
        compose_button_xpath = '//div[text()="COMPOSE"]'
        recepients_xpath = '//*[text()="Recipients"]'
        to_field_xpath ='//*[@name="to"]'
        subject_xpath = '//*[@aria-label="Subject"]'
        body_xpath = '//*[@aria-label="Message Body" and @role="textbox"]'
        send_xpath = '//*[text()="Send"]'

        driver.find_element_by_xpath(sign_in_xpath).click()
        driver.find_element_by_xpath(email_xpath).send_keys(login)
        driver.find_element_by_xpath(next_button_xpath).click()
        driver.find_element_by_xpath(pwd_field_xpath).send_keys(password)
        driver.find_element_by_xpath(sign_in_button_xpath).click()
        driver.find_element_by_xpath(compose_button_xpath).click()

        # sometimes "To" field is displayed and you don't have to click "Recepients"
        if not driver.find_element_by_xpath(to_field_xpath).is_displayed():
            # in order to make "To" field available, we need to click on "Recipients"
            driver.find_element_by_xpath(recepients_xpath).click()

        # now we can input data and send the message
        driver.find_element_by_xpath(to_field_xpath).send_keys(login)
        driver.find_element_by_xpath(subject_xpath).send_keys(subject)
        driver.find_element_by_xpath(body_xpath).send_keys(body_text)
        driver.find_element_by_xpath(send_xpath).click()

        # at the end of the test we neet to make sure that message arrived:
        # this is to be done

        inbox_xpath = '//*[contains(@title, "Inbox")]'
        subject_xpath = "//span/b[text()='{0}']".format(subject)
        for i in range(1, 121):
            try:
                print "Looking for email, attempt number {0}".format(i)
                assert assdriver.find_element_by_xpath(subject_xpath)
            except:
                print "Have not found element, sleeping 1s"
                time.sleep(1)
                driver.find_element_by_xpath(inbox_xpath).click()

        print "Done "









