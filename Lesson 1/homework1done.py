import re
import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from lib.general import login


class HW1_Tests(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        url = "http://hrm.seleniumminutes.com"
        driver.get(url)

        self.wait = WebDriverWait(driver, 10)
        login(driver)
        self.driver = driver

    def tearDown(self):
        self.driver.quit()

    def test_quick_launch_menu(self):
        expected_img_name = {
            'Assign Leave': 'ApplyLeave',
            'Leave List': 'MyLeave',
            'Timesheets': 'MyTimesheet',
            'Apply Leave': 'ApplyLeave',
            'My Leave': 'MyLeave',
            'My Timesheet': 'MyTimesheet',
        }

        driver = self.driver

        quick_launch_menu = driver.find_element_by_class_name('quickLaungeContainer')
        all_quick_links = quick_launch_menu.find_elements_by_class_name('quickLinkText')

        for link in all_quick_links:
            img_name = self.extract_img_name(
                    link.find_element_by_xpath('.//preceding-sibling::img').get_attribute(
                        'src'))
            assert expected_img_name[link.text] == img_name, \
                "Expected the image name above the {link_text}" \
                " link to be {expected_img_name}, but it was" \
                " {actual_img_name} instead".format(
                        link_text=link.text,
                        expected_img_name=expected_img_name[link.text],
                        actual_img_name=img_name)

    #second test case - comparing odd rows and even ones
    def test_pim_row_style(self):
        driver = self.driver
        driver.find_element_by_id('menu_pim_viewPimModule').click()
        # self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'odd')))
        all_rows = driver.find_elements_by_css_selector('tbody>tr')
        time.sleep(1)
        for i, row in enumerate(all_rows, 1):
            message = 'Expect the style of row #{0} to be {1}, but it was {2}'
            row_style = row.get_attribute('class')
            if i%2 == 1:
                assert row_style == 'odd', message.format(i, 'odd', row_style)
            else:
                assert row_style == 'even', message.format(i, 'even', row_style)


    def extract_img_name(self, src):
        return re.search('.*/(\w+?).png', src).group(1)


if __name__ == "__main__":
    unittest.main()