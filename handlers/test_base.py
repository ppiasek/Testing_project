import platform
import pytest
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


class TestBase(object):

    def __init__(self, browser):
        if browser == 'chrome':
            self._driver = webdriver.Chrome(executable_path=str(Path(f'{driver_location}{browser_driver[platform.system()][browser]}')))
        elif browser == 'firefox':
            self._driver = webdriver.Firefox(executable_path=str(Path(f'{driver_location}{browser_driver[platform.system()][browser]}')))
        else:
            raise Exception('Wrong browser selected')

        self.wait_implictly(15)
        self._driver.get(tested_url)
        self._driver.maximize_window()

    def close(self):
        self._driver.close()

    def wait_implictly(self, timeout):
        self._driver.implicitly_wait(timeout)
