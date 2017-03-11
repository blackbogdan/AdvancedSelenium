import unittest
from datetime import datetime
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from lib.general import login, enter_text


class TwoSessionDemo(unittest.TestCase):

    def setUp(self):
        url = "http://hrm.seleniumminutes.com"

        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.get(url)

        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

        # -------- session 2
        driver2 = webdriver.Firefox()
        driver2.implicitly_wait(10)
        driver2.get(url)

        self.wait2 = WebDriverWait(driver2, 10)
        self.driver2 = driver2

    def tearDown(self):
        self.driver.quit()
        self.driver2.quit()

    def test_apply_leave(self):
        admin = self.driver
        bob = self.driver2

        login(admin)
        login(bob, 'bobsmith')

        assert admin.find_element_by_css_selector(
                '#task-list-group-panel-menu_holder td').text == 'No Records are Available'

        bob.find_element_by_link_text('Apply Leave').click()
        Select(bob.find_element_by_id(
                'applyleave_txtLeaveType')).select_by_visible_text('Vacation')

        enter_text(bob, By.ID, 'applyleave_txtFromDate', '2016-04-15')
        enter_text(bob, By.ID, 'applyleave_txtToDate', '2016-04-15')

        comment = str(datetime.now())
        bob.find_element_by_id('applyleave_txtComment').send_keys(comment)


        bob.find_element_by_id('applyBtn').click()

        admin.refresh()

        pending_leave_text = admin.find_element_by_css_selector(
                '#task-list-group-panel-menu_holder td').text

        assert 'Bob Smith' in pending_leave_text

        admin.find_element_by_css_selector('#task-list-group-panel-menu_holder a').click()

        Select(admin.find_element_by_class_name(
                'quotaSelect')).select_by_visible_text('Reject')
        admin.find_element_by_id('btnSave').click()


        bob.find_element_by_id('menu_leave_viewMyLeaveList').click()

        row = bob.find_element_by_xpath(
                '//span[contains(@id,"commentContainer") and text()="{0}"]'
                '/ancestor::tr'.format(comment))
        # bob.find_element_by_css_selector("resultTable tbody>tr:last-child")
        # bob.find_element_by_xpath("//table[@id='resultTable']/tbody/tr[last()]")

        status = row.find_element_by_xpath('.//td[6]/a').text
        self.assertTrue("Rejected" in status,
                        "Status '{0}' did not match expected value '{1}'".format(
                            status, 'Rejected'
                        ))


