from handlers import driver
from handlers.gdrive_login_page import GDriveLoginUI
from handlers.gdrive_logout_page import GDriveLogoutUI
from handlers.gdrive_page import GDriveUI
from pathlib import Path

credentials_path = '../credentials/login_credentials.txt'


class UIFunctions(object):

    def __init__(self):
        self.driver = driver.driver_setup()
        self.login_page = GDriveLoginUI(self.driver)
        self.logout_page = GDriveLogoutUI(self.driver)
        self.main_page = GDriveUI(self.driver)

    def login(self):
        _username, _password = Path(credentials_path).read_text().split('\n')
        self.login_page.navigate_to_login_page.click()
        self.login_page.login_field.clear()
        self.login_page.login_field.send_keys(_username)
        self.login_page.login_field_next_button.click()
        self.login_page.password_field.clear()
        self.login_page.password_field.send_keys(_password)
        self.login_page.password_field_next_button.click()

    def logout(self):
        self.logout_page.user_view.click()
        self.logout_page.user_logout.click()
