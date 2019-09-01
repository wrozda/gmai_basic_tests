from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def element(self, locator, selector):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((locator, selector)))
        element = self.driver.find_element(locator, selector)
        return element

    def fill_element(self, locator, selector, value):
        element = self.element(locator, selector)
        element.send_keys(value)

    def fill_element_and_send_keys(self, locator, selector, value, keys):
        element = self.element(locator, selector)
        element.send_keys(value)
        element.send_keys(keys)

    def click_element(self, locator, selector):
        element = self.element(locator, selector)
        element.click()




