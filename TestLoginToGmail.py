from loginGmialPage import LoginGmailPage
from testTemplate import TestTemplate
from test_data.credentials import gmail_credentials


class TestLoginToGmial(TestTemplate):

    def log_in_to_gmail(self):
        login_page = LoginGmailPage(self.driver)
        login_page.login_to_gmail_account(**gmail_credentials)
        assert login_page.check_login()