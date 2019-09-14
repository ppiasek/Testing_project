from handlers.test_base import TestBase
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class LoginPage(TestBase):

    @property
    def navigate_to_login_page(self):
        return self._driver.find_element_by_link_text('Go to Google Drive')

    @property
    def login_field(self):
        return self._driver.find_element_by_id('identifierId')

    @property
    def login_field_next_button(self):
        return self._driver.find_element_by_id('identifierNext')

    @property
    def password_field(self):
        # pass_field = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
        # return pass_field
        return self._driver.find_element_by_name('password')

    @property
    def password_field_next_button(self):
        return self._driver.find_element_by_id('passwordNext')
        # next_button = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.ID, 'passwordNext')))
        # next_button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.ID, 'passwordNext')))
        # return next_button

    @property
    def user_logged_in(self):
        return self._driver.find_element_by_id('drive_main_page')
