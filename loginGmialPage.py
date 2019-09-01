from basePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginGmailPage(BasePage):
    LOGIN = 'identifierId'
    PASSWORD = 'password'

    MENU_INDEX = '//a[contains(text(), "Index")]'

    def login_to_gmail_account(self, **credentials):
        self.fill_element_and_send_keys(
            By.ID, LoginGmailPage.LOGIN, credentials['login'], Keys.ENTER)
        self.fill_element_and_send_keys(
            By.NAME, LoginGmailPage.PASSWORD, credentials['password'], Keys.ENTER)

    def check_login(self):
        return self.element(By.XPATH, LoginGmailPage.MENU_INDEX)
