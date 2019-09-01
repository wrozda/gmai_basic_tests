import unittest
from selenium import webdriver


class TestTemplate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('../Gmail/chromedriver')
        self.driver.get('https://gmail.com')

    def tearDown(self):
        self.driver.quit()