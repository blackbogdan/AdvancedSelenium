from selenium.webdriver.common.by import By


def enter_text(driver, by, locator, text):
    element = driver.find_element(by, locator)
    element.clear()
    element.send_keys(text)


def login(driver, username="admin", password="Password"):
    enter_text(driver, By.ID, "txtUsername", username)
    enter_text(driver, By.ID, "txtPassword", password)
    driver.find_element_by_id("btnLogin").click()


def logout(driver):
    driver.find_element_by_id("welcome").click()
    driver.find_element_by_link_text("Logout").click()