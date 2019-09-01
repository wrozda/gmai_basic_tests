from basePage import BasePage
from selenium.webdriver.common.by import By
from test_data.emails_data import emails_data


class HomePage(BasePage):
    COMPOSE_BUTTON = '//div[contains(text(), "Compose")]'
    TO = 'to'
    SUBJECT = 'subjectbox'
    SEND_BUTTON = '//div[text() = "Send"]'
    MENU_SENT = '//a[contains(text(), "Sent")]'

    def send_email(self, **data):
        self.click_element(By.XPATH, HomePage.COMPOSE_BUTTON)
        self.fill_element(By.NAME, HomePage.TO, data['1_email']['recipients'])
        self.fill_element(By.NAME, HomePage.SUBJECT, data['1_email']['subject'])
        self.click_element(By.XPATH, HomePage.SEND_BUTTON)
        self.click_element(By.XPATH, HomePage.MENU_SENT)

    def check_fist_sent_email(self):
        return self.element(By.XPATH, '//tr[1][contains(.,"%s")]' % emails_data['1_email']['subject'])


