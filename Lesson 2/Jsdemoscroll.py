#this import is for datetime.now()
from datetime import datetime
from time import gmtime, strftime
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class DemoJSScroll(unittest.TestCase):

    def setUp(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        url = "https:/www.ajc.com"
        driver.get(url)

        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    def tearDown(self):
        self.driver.quit()

    def test_js_scroll(self):
        driver = self.driver
        while self.scroll():
            try:
                #need to change selector
                driver.find_element_by_css_selector('.cm-navbar-footer-bar.cm-navbar-internal')
                break
            except NoSuchElementException:
                continue
        self.assertTrue(driver.find_element_by_class_name('cm-sit-index'.is_displayed()))




    def scroll(self, ypixels=250):
        #defined webdriver, format sticks value inside {0}
        max = self.driver.execute_script("window.scrollMaxY")
        current = self.driver.execute_script("window.scrollY")

        if current == max:
            return False
        self.driver.execute_script("window.scrollBy(0,{0})".format(ypixels))
        return True