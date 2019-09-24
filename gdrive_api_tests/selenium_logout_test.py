import unittest
import time
from handlers.gdrive_logout_page import GDriveLogoutUI


class GDriveTreeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.page_object = GDriveLogoutUI()
        cls.page_object.login()
        cls.page_object.screenshot()

    def test_1_logout(self):
        self.page_object.user_view.click()
        self.page_object.screenshot()
        self.page_object.user_logout.click()
        self.page_object.screenshot()
        self.assertTrue(self.page_object.user_logged_out.is_displayed(), "User not logged out")

    @classmethod
    def tearDownClass(cls):
        # comments left in case something needs to be debbuged
        cls.page_object.close()
        #pass
