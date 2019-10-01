import unittest
from handlers.ui_functions import UIFunctions


class GDriveTreeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ui = UIFunctions()
        cls.ui.login()
        cls.ui.login_page.screenshot()

    def test_1_shared(self):
        self.ui.main_page.shared_with_me_button.click()
        self.assertTrue(self.ui.main_page._driver.current_url == 'https://drive.google.com/drive/shared-with-me',
                        "Shared with me not selected")
        self.ui.main_page.screenshot()

    def test_2_recent(self):
        self.ui.main_page.recent_button.click()
        self.assertTrue(self.ui.main_page._driver.current_url == 'https://drive.google.com/drive/recent',
                        "Recent not selected")
        self.ui.main_page.screenshot()

    def test_3_starred(self):
        self.ui.main_page.starred_button.click()
        self.assertTrue(self.ui.main_page._driver.current_url == 'https://drive.google.com/drive/starred',
                        "Starred not selected")
        self.ui.main_page.screenshot()

    def test_4_trash(self):
        self.ui.main_page.trash_button.click()
        self.assertTrue(self.ui.main_page._driver.current_url == 'https://drive.google.com/drive/trash',
                        "Trash not selected")
        self.ui.main_page.screenshot()

    def test_5_my_drive(self):
        self.ui.main_page.my_drive_button.click()
        self.assertTrue(self.ui.main_page._driver.current_url == 'https://drive.google.com/drive/my-drive',
                        "My Drive not selected")
        self.ui.main_page.screenshot()

    @classmethod
    def tearDownClass(cls):
        # comments left in case something needs to be debbuged
        cls.ui.main_page.logout()
        cls.ui.main_page.screenshot()
        cls.ui.main_page.close()
        # pass
