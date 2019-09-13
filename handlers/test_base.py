import platform
from selenium import webdriver

browser_driver = {
    'Windows':
        {
            'chrome': '..\\drivers\\chromedriver_77.exe',
            'firefox': '..\\drivers\\geckodriver_0.25.0.exe'
        },
    'Linux':
        {
            'chrome': '../drivers/chromedriver_linux_77',
            'firefox': '../drivers/geckodriver_linux_0.25.0'
        }
}


class TestBase(object):

    def __init__(self, browser):
        if browser == 'chrome':
            self._driver = webdriver.Chrome(executable_path=browser_driver[platform.system()]['chrome'])
        elif browser == 'firefox':
            self._driver = webdriver.Firefox(executable_path=browser_driver[platform.system()]['firefox'])
        else:
            raise Exception('Wrong browser selected')

        self.wait_implictly(15)
        self._driver.get('https://www.google.com/drive/')

    def close(self):
        self._driver.close()

    def wait_implictly(self, timeout):
        self._driver.implicitly_wait(timeout)
