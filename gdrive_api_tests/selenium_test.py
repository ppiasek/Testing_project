import unittest
from handlers.login_page import LoginPage
from pathlib import Path


class UITest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = LoginPage('chrome')
        _credentials = Path('../credentials/login_credentials.txt').read_text()
        cls.username = _credentials[:_credentials.find('\n')]
        cls.password = _credentials[_credentials.find('\n') + 1:]

    def test_1_login(self):
        self.driver.navigate_to_login_page.click()
        self.driver.login_field.clear()
        self.driver.login_field.send_keys(self.username)
        self.driver.login_field_next_button.click()
        self.driver.wait_implictly(5)
        self.driver.password_field.clear()
        self.driver.password_field.send_keys(self.password)
        self.driver.wait_implictly(5)
        #self.driver.password_field_next_button.click()
        self.driver._driver.execute_script('arguments[0].click();', self.driver._driver.find_element_by_id('passwordNext'))
        #self.assertTrue(self.driver.user_logged_in, "User is not logged in")

    @classmethod
    def tearDownClass(cls):
        #cls.driver.close()
        pass
