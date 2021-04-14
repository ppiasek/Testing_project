from handlers.ui_functions import UIFunctions
from handlers import ui_testbase
from pathlib import Path

CREDENTIALS_PATH = '../credentials/login_credentials.txt'


class LoginTest(ui_testbase.UITestBase):

    @classmethod
    def setUpClass(cls):
        cls.ui = UIFunctions(frame_depth=1)
        cls.username, cls.password = Path(CREDENTIALS_PATH).read_text().split('\n')
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
        super().tearDownClass()
