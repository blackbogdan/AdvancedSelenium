import unittest
from datetime import datetime
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class DemoJSScroll(unittest.TestCase):

    def setUp(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        url = "http://www.ajc.com/"
        driver.get(url)

        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    def tearDown(self):
        self.driver.quit()

    def test_js_scroll(self):
        driver = self.driver

        while self.scroll():
            try:
                driver.find_element_by_css_selector(
                        '.cm-navbar-footer-bar[style="display: block;"]')
                break
            except NoSuchElementException:
                continue

        self.assertTrue(driver.find_element_by_class_name('cm-site-index').is_displayed())


    def scroll(self, ypixels=250):
        max = self.driver.execute_script("return window.scrollMaxY;")
        current = self.driver.execute_script("return window.scrollY;")

        if current == max:
            return False
        self.driver.execute_script("window.scrollBy(0, {0})".format(ypixels))
        return True