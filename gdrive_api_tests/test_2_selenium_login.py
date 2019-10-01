import unittest
from handlers.ui_functions import UIFunctions
from pathlib import Path

credentials_path = '../credentials/login_credentials.txt'


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ui = UIFunctions()
        cls.username, cls.password = Path(credentials_path).read_text().split('\n')
        cls.ui.login_page.screenshot()

    def test_1_login(self):
        self.ui.login_page.navigate_to_login_page.click()
        self.ui.login_page.screenshot()
        self.ui.login_page.login_field.clear()
        self.ui.login_page.login_field.send_keys(self.username)
        self.ui.login_page.screenshot()
        self.ui.login_page.login_field_next_button.click()
        self.ui.login_page.screenshot()
        self.ui.login_page.password_field.clear()
        self.ui.login_page.password_field.send_keys(self.password)
        self.ui.login_page.screenshot()
        self.ui.login_page.password_field_next_button.click()
        self.ui.login_page.screenshot()
        self.assertTrue(self.ui.login_page.user_logged_in, "User is not logged in")

    @classmethod
    def tearDownClass(cls):
        # comments left in case something needs to be debbuged
        cls.ui.login_page.logout()
        cls.ui.login_page.screenshot()
        cls.ui.login_page.close()
        # pass
