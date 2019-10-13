import unittest
from handlers.ui_functions import UIFunctions
from pathlib import Path

credentials_path = '../credentials/login_credentials.txt'


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ui = UIFunctions()
        cls.username, cls.password = Path(credentials_path).read_text().split('\n')
        cls.ui.screenshot()

    def test_1_login(self):
        self.ui.login_page.navigate_to_login_page.click()
        self.ui.screenshot()
        self.ui.login_page.login_field.clear()
        self.ui.login_page.login_field.send_keys(self.username)
        self.ui.screenshot()
        self.ui.login_page.login_field_next_button.click()
        self.ui.screenshot()
        self.ui.login_page.password_field.clear()
        self.ui.login_page.password_field.send_keys(self.password)
        self.ui.screenshot()
        self.ui.login_page.password_field_next_button.click()
        self.ui.screenshot()
        self.assertTrue(self.ui.login_page.user_logged_in, "User is not logged in")

    @classmethod
    def tearDownClass(cls):
        # comments left in case something needs to be debbuged
        cls.ui.logout()
        cls.ui.screenshot()
        cls.ui.login_page.close()
        # pass
