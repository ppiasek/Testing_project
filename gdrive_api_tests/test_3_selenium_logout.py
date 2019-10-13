import unittest
from handlers.ui_functions import UIFunctions


class GDriveTreeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ui = UIFunctions()
        cls.ui.login()
        cls.ui.screenshot()

    def test_1_logout(self):
        self.ui.logout_page.user_view.click()
        self.ui.screenshot()
        self.ui.logout_page.user_logout.click()
        self.ui.screenshot()
        self.assertTrue(self.ui.logout_page.user_logged_out.is_displayed(), "User not logged out")

    @classmethod
    def tearDownClass(cls):
        # comments left in case something needs to be debbuged
        cls.ui.logout_page.close()
        # pass
