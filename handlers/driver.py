import os
import platform
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


def driver_setup():
    if os.environ['browser'] == 'chrome':
        driver = webdriver.Chrome(executable_path=str(
            Path(f'{driver_location}{browser_driver[platform.system()][os.environ["browser"]]}')))
    elif os.environ['browser'] == 'firefox':
        driver = webdriver.Firefox(
            executable_path=str(
                Path(f'{driver_location}{browser_driver[platform.system()][os.environ["browser"]]}')))
    else:
        raise Exception('Wrong browser selected')

    driver.get(tested_url)
    driver.maximize_window()
    return driver
