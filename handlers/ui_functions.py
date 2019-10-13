import os
import sys
from datetime import datetime
from handlers import driver
from handlers.gdrive_login_page import GDriveLoginUI
from handlers.gdrive_logout_page import GDriveLogoutUI
from handlers.gdrive_page import GDriveUI
from pathlib import Path
from time import sleep

credentials_path = '../credentials/login_credentials.txt'
evidence_path = '../evidence/'


class UIFunctions(object):

    def __init__(self):
        self.driver = driver.driver_setup()
        self.login_page = GDriveLoginUI(self.driver)
        self.logout_page = GDriveLogoutUI(self.driver)
        self.main_page = GDriveUI(self.driver)

        _execution_time = datetime.now().strftime('%d.%m.%Y_%H.%M.%S')
        self.evidence_location = Path(f'{evidence_path}{sys._getframe(1).f_globals["__name__"]}_{_execution_time}')
        os.makedirs(self.evidence_location)

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

    def screenshot(self, wait=0):
        if wait:
            sleep(wait)

        _execution_time = datetime.now().strftime('%H.%M.%S.%f')
        self.driver.save_screenshot(
            f"{Path(f'{self.evidence_location}/{sys._getframe(1).f_code.co_name}_{_execution_time}')}.png"
        )
