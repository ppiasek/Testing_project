import unittest
from handlers.ui_functions import UIFunctions
from handlers.gdrive_login_page import GDriveLoginUI
from pathlib import Path

credentials_path = '../credentials/login_credentials.txt'


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.page_object = GDriveLoginUI()
        cls.username, cls.password = Path(credentials_path).read_text().split('\n')
        cls.page_object.screenshot()

    def test_1_login(self):
        self.page_object.navigate_to_login_page
        self.page_object.screenshot()
        self.page_object.login_field.clear()
        self.page_object.login_field.send_keys(self.username)
        self.page_object.screenshot()
        self.page_object.login_field_next_button.click()
        self.page_object.screenshot()
        self.page_object.password_field.clear()
        self.page_object.password_field.send_keys(self.password)
        self.page_object.screenshot()
        self.page_object.password_field_next_button.click()
        self.page_object.screenshot()
        self.assertTrue(self.page_object.user_logged_in, "User is not logged in")

    @classmethod
    def tearDownClass(cls):
        # comments left in case something needs to be debbuged
        cls.page_object.logout()
        cls.page_object.screenshot()
        cls.page_object.close()
        #pass