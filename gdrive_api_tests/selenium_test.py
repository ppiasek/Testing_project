from handlers.login_page import LoginPage
import unittest


class UITest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = LoginPage('chrome')
        with open('../credentials/login_credentials.txt') as credentials:
            content = credentials.readlines()
            cls.username = content[0]
            cls.password = content[1]
        credentials.close()
        print(f'{cls.username}{cls.password}')

    def test_login(self):
        self.driver.navigate_to_login_page.click()
        self.driver.login_field.clear()
        self.driver.login_field.send_keys(self.username)
        #self.driver.login_field_next_button.click()
        self.driver.password_field.clear()
        self.driver.password_field.send_keys(self.password)
        self.driver.password_field_next_button.click()

    @classmethod
    def tearDownClass(cls):
        #cls.driver.close()
        pass