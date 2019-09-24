import platform
import os
import sys
from time import sleep
from datetime import datetime
from handlers.gdrive_login_page import GDriveLoginUI
from handlers.gdrive_logout_page import GDriveLogoutUI
from pathlib import Path
from selenium import webdriver


tested_url = 'https://www.google.com/drive/'
driver_location = '../drivers/'
browser_driver = {
    'Windows':
        {
            'chrome': 'chromedriver_77.exe',
            'firefox': 'geckodriver_0.25.0.exe'
        },
    'Linux':
        {
            'chrome': 'chromedriver_linux_77',
            'firefox': 'geckodriver_linux_0.25.0'
        }
}
credentials_path = '../credentials/login_credentials.txt'
evidence_path = '../evidence/'


class UIBase(object):

    def driver_setup(self):
        if os.environ['browser'] == 'chrome':
            self._driver = webdriver.Chrome(executable_path=str(Path(f'{driver_location}{browser_driver[platform.system()][os.environ["browser"]]}')))
        elif os.environ['browser'] == 'firefox':
            self._driver = webdriver.Firefox(executable_path=str(Path(f'{driver_location}{browser_driver[platform.system()][os.environ["browser"]]}')))
        else:
            raise Exception('Wrong browser selected')

        self.wait_implictly(15)
        self._driver.get(tested_url)
        self._driver.maximize_window()

        _execution_time = datetime.now().strftime('%d.%m.%Y_%H.%M.%S')
        self.evidence_location = Path(f'{evidence_path}{_execution_time}')
        os.makedirs(self.evidence_location)

    def close(self):
        self._driver.close()

    def wait_implictly(self, timeout):
        self._driver.implicitly_wait(timeout)

    def login(self):
        _username, _password = Path(credentials_path).read_text().split('\n')
        _login_page = GDriveLoginUI(self._driver)
        _login_page.navigate_to_login_page.click()
        sleep(1)
        _login_page.login_field.clear()
        _login_page.login_field.send_keys(_username)
        sleep(1)
        _login_page.login_field_next_button.click()
        sleep(1)
        _login_page.password_field.clear()
        _login_page.password_field.send_keys(_password)
        sleep(1)
        _login_page.password_field_next_button.click()
        sleep(1)

    def logout(self):
        _logout_page = GDriveLogoutUI(self._driver)
        _logout_page.user_view.click()
        sleep(1)
        _logout_page.user_logout.click()
        sleep(1)

    def screenshot(self):
        _execution_time = datetime.now().strftime('%H.%M.%S.%f')
        getframe_expr = 'sys._getframe({}).f_code.co_name'
        sleep(1)
        self._driver.save_screenshot(f"{Path(f'{self.evidence_location}/{eval(getframe_expr.format(2))}_{_execution_time}')}.png")
