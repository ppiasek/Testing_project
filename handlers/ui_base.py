import platform
import os
import sys
import time
from datetime import datetime
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

    def __init__(self):
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
        self._driver.find_element_by_link_text('Go to Google Drive').click()
        self._driver.find_element_by_id('identifierId').clear()
        self._driver.find_element_by_id('identifierId').send_keys(_username)
        self._driver.find_element_by_id('identifierNext').click()
        self._driver.find_element_by_name('password').clear()
        self._driver.find_element_by_name('password').send_keys(_password)
        self._driver.find_element_by_id('passwordNext').click()

    def logout(self):
        self._driver.find_element_by_css_selector('#gb > div:nth-of-type(2) > div:nth-of-type(3) > div > div:nth-of-type(2) > div > a').click()
        self._driver.find_element_by_id('gb_71').click()

    def screenshot(self):
        _execution_time = datetime.now().strftime('%H.%M.%S.%f')
        getframe_expr = 'sys._getframe({}).f_code.co_name'
        time.sleep(1)
        self._driver.save_screenshot(f"{Path(f'{self.evidence_location}/{eval(getframe_expr.format(2))}_{_execution_time}')}.png")
