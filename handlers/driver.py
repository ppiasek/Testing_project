import os
import platform
from pathlib import Path
from selenium import webdriver


TESTED_URL = 'https://www.google.com/drive/'
DRIVER_LOCATION = '../drivers/'
BROWSER_DRIVER = {
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


def driver_setup():
    if os.environ['browser'] == 'chrome':
        driver = webdriver.Chrome(executable_path=str(
            Path(f'{DRIVER_LOCATION}{BROWSER_DRIVER[platform.system()][os.environ["browser"]]}')))
    elif os.environ['browser'] == 'firefox':
        driver = webdriver.Firefox(
            executable_path=str(
                Path(f'{DRIVER_LOCATION}{BROWSER_DRIVER[platform.system()][os.environ["browser"]]}')))
    else:
        raise Exception('Wrong browser selected')

    driver.get(TESTED_URL)
    driver.maximize_window()
    return driver
