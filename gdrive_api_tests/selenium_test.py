import pytest
import unittest
from handlers.gdrive_page import GDrivePage
from pathlib import Path


class UITest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = GDrivePage('chrome')
        _credentials = Path('../credentials/login_credentials.txt').read_text()
        cls.username = _credentials[:_credentials.find('\n')]
        cls.password = _credentials[_credentials.find('\n') + 1:]

    def test_1_login(self):
        self.driver.navigate_to_login_page.click()
        self.driver.login_field.clear()
        self.driver.login_field.send_keys(self.username)
        self.driver.login_field_next_button.click()
        self.driver.password_field.clear()
        self.driver.password_field.send_keys(self.password)
        self.driver.password_field_next_button.click()
        #self.driver._driver.execute_script('arguments[0].click();', self.driver._driver.find_element_by_id('passwordNext'))
        self.assertTrue(self.driver.user_logged_in, "User is not logged in")

    def test_2_go_through_tree(self):
        self.driver.shared_with_me_button.click()
        self.assertTrue(self.driver.shared_with_me_text.is_displayed(), 'Shared with me not displayed')
        self.driver.recent_button.click()
        #self.assertTrue(self.driver.recent_text.is_displayed(), 'Recent not displayed')
        self.driver.starred_button.click()
        self.assertTrue(self.driver.starred_text.is_displayed(), 'Starred not displayed')
        self.driver.trash_button.click()
        self.assertTrue(self.driver.trash_text.is_displayed(), 'Trash not displayed')
        self.driver.my_drive_button.click()
        #self.assertTrue(self.driver.my_drive_text.is_displayed(), 'My Drive not displayed')

    def test_3_logout(self):
        self.driver.user_view.click()
        self.driver.user_logout.click()
        self.assertTrue(self.driver.user_logged_out.is_displayed(), "User not logged out")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
