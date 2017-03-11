import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class GMailTests(unittest.TestCase):

    def setUp(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        url = "http://hrm.seleniumminutes.com/class"
        driver.get(url)

        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    def tearDown(self):
        self.driver.quit()

    def test_send_mail(self):
        login = 'admin'
        password = 'Password'

        driver = self.driver

        driver.find_element_by_id('txtUsername').send_keys(login)
        driver.find_element_by_id('txtPassword').send_keys(password)

        driver.find_element_by_id('btnLogin').click()

        self.wait.until(
                EC.visibility_of_element_located(
                        (By.ID, 'branding')))
        driver.find_element_by_id('menu_dashboard_index').click()

        # first_image_xpath = (//div[@class="quickLaunge"]//descendant::img)[1]
        for i in range(1,4):
            print "Verifying footer of image nubmer %s" %(i)
            # image_xpath = (//div[@class="quickLaunge"]//descendant::img)[i]
            footer_xpath = ('(//div[@class="quickLaunge"]//descendant::img)[%s]/following-sibling::span' %(i))
            or lin(.//preceding-sibling::img)[1]
            if i==1:
                expected_label= "Assign Leave"
                # how to get value of attribute  "quickLinkText" in <span class="quickLinkText">Leave List</span>
                y = driver.find_element_by_xpath(footer_xpath).get_attribute("class")
                # how to find "Assign Leave" in <span class="quickLinkText">Assign Leave</span>
                actual_label = driver.find_element_by_xpath(footer_xpath).text
                self.assertTrue(expected_label in actual_label)
                print y
                print actual_label
                print "______________________\n"

            elif i==2:
                print
                expected_label= "Leave List"
                actual_label = driver.find_element_by_xpath(footer_xpath).text
                self.assertTrue(expected_label in actual_label)
                print actual_label
                print "______________________\n"

            elif i==3:
                expected_label= "Timesheets"
                actual_label = driver.find_element_by_xpath(footer_xpath).text
                self.assertTrue(expected_label in actual_label)
                print actual_label
                print "______________________\n"