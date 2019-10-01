import os
import sys
from datetime import datetime
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

evidence_path = '../evidence/'


class UIBase(object):

    def __init__(self, driver):
        self._driver = driver
        _execution_time = datetime.now().strftime('%d.%m.%Y_%H.%M.%S')
        self.evidence_location = Path(f'{evidence_path}{sys._getframe(2).f_code.co_name}_{_execution_time}')
        os.makedirs(self.evidence_location)

    def close(self):
        self._driver.close()

    def wait_implictly(self, timeout):
        self._driver.implicitly_wait(timeout)

    def screenshot(self):
        _execution_time = datetime.now().strftime('%H.%M.%S.%f')
        self._driver.save_screenshot(
            f"{Path(f'{self.evidence_location}/{sys._getframe(2).f_code.co_name}_{_execution_time}')}.png"
        )

    def _wait_for_element(self, args):
        WebDriverWait(self._driver, 10).until(expected_conditions.presence_of_element_located(args))

    def _wait_for_element_to_be_clickable(self, args):
        WebDriverWait(self._driver, 20).until(expected_conditions.element_to_be_clickable(args))

    def _generic_id_element(self, object_id):
        self._wait_for_element((By.ID, object_id))
        self._wait_for_element_to_be_clickable((By.ID, object_id))
        return self._driver.find_element_by_id(object_id)

    def _generic_class_element(self, object_class_name):
        self._wait_for_element((By.CLASS_NAME, object_class_name))
        self._wait_for_element_to_be_clickable((By.CLASS_NAME, object_class_name))
        return self._driver.find_element_by_class_name(object_class_name)

    def _generic_css_element(self, object_css_selector):
        self._wait_for_element((By.CSS_SELECTOR, object_css_selector))
        self._wait_for_element_to_be_clickable((By.CSS_SELECTOR, object_css_selector))
        return self._driver.find_element_by_css_selector(object_css_selector)

    def _generic_name_element(self, object_name):
        self._wait_for_element((By.NAME, object_name))
        self._wait_for_element_to_be_clickable((By.NAME, object_name))
        return self._driver.find_element_by_name(object_name)

    def _generic_text_element(self, object_text):
        self._wait_for_element((By.LINK_TEXT, object_text))
        self._wait_for_element_to_be_clickable((By.LINK_TEXT, object_text))
        return self._driver.find_element_by_link_text(object_text)