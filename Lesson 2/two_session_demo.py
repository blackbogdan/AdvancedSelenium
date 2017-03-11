#this import is for datetime.now()
from datetime import datetime
from time import gmtime, strftime
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from twisted.spread.ui.gtk2util import login
from lib.general import enter_text


class TwoSessionDemo(unittest.TestCase):

    def setUp(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        url = "https://hrm.seleniumminutes.com"
        driver.get(url)

        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

        #------------session#2
        driver2 = webdriver.Firefox()
        driver2.implicitly_wait(10)
        driver2.get(url)

        self.wait = WebDriverWait(driver2, 10)
        self.driver2 = driver2

    def tearDown(self):
        self.driver.quit()
        self.driver2.quit()

    def test_apply_leave(self):
        admin = self.driver
        bob = self.driver2
        login(admin)
        login(bob,"bobsmith")

        #first verify that no records are available
        assert admin.find_elements_by_css_selector(
            '#task-list-group-panel-menu_holder').text == 'No records are Available'

        bob.find_element_by_link_text("Apply Leave").click()
        Select(bob.find_element_by_id('applyleave_txtLeaveType')).select_by_visible_text("Vacation")
        enter_text(bob, By.ID, 'applyleave_txtFromDate', 2016-12-02)
        enter_text(bob, By.ID, 'applyleave_txtFromDate', 2016-12-02)

        bob.find_element_by_id('applyBtn').click()


        admin.refresh()
        #gets text from css selector
        assert 'Bob Smith' in admin.find_elements_by_css_selector(
            '#task-list-group-panel-menu_holder').text()

        admin.find_elements_by_css_selector(
            '#task-list-group-panel-menu_holder a')
        Select(admin.find_element_by_class_name(
            "select_action quotaSelect")).select_by_visible_text("Reject")

        bob.find_element_by_id('menu_leave_viewMyLeaveList').click()
        bob.find_elements_by_css_selector('tbody>tr::last_child')
        #or  bob.find_elements_by_xpaht('//table[@id='smth']/tbody/tr[last()]')

        row= bob.find_element_by_css_selector('#resultTable tbody>tr:last_child')
        row.fin


