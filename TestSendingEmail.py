from homePage import HomePage
from testTemplate import TestTemplate
from loginGmialPage import LoginGmailPage
from test_data.emails_data import emails_data
from test_data.credentials import gmail_credentials


class TestSendingEmail(TestTemplate):

    def test_sending_email(self):
        home_page = HomePage(self.driver)
        login_page = LoginGmailPage(self.driver)

        login_page.login_to_gmail_account(**gmail_credentials)
        home_page.send_email(**emails_data)
        assert home_page.check_fist_sent_email()

