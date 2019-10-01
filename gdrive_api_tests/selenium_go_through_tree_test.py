import unittest
import time
from handlers.gdrive_page import GDriveUI
from handlers.ui_base import UIBase
from handlers.gdrive_page import GDriveUI


class GDriveTreeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        login_object = UIBase()
        login_object.login()
        cls.page_object = GDriveUI().login()
        cls.page_object.login()
        cls.page_object.screenshot()

    def test_1_shared(self):
        self.page_object._drive.click()
        time.sleep(1)
        self.assertTrue(self.page_object._driver.current_url == 'https://drive.google.com/drive/shared-with-me', "Shared with me not selected")
        self.page_object.screenshot()

    def test_2_recent(self):
        self.page_object.recent_button.click()
        time.sleep(1)
        self.assertTrue(self.page_object._driver.current_url == 'https://drive.google.com/drive/recent', "Recent not selected")
        self.page_object.screenshot()

    def test_3_starred(self):
        self.page_object.starred_button.click()
        time.sleep(1)
        self.assertTrue(self.page_object._driver.current_url == 'https://drive.google.com/drive/starred', "Starred not selected")
        self.page_object.screenshot()

    def test_4_trash(self):
        self.page_object.trash_button.click()
        time.sleep(1)
        self.assertTrue(self.page_object._driver.current_url == 'https://drive.google.com/drive/trash', "Trash not selected")
        self.page_object.screenshot()

    def test_5_my_drive(self):
        self.page_object.my_drive_button.click()
        time.sleep(1)
        self.assertTrue(self.page_object._driver.current_url == 'https://drive.google.com/drive/my-drive', "My Drive not selected")
        self.page_object.screenshot()

    @classmethod
    def tearDownClass(cls):
        # comments left in case something needs to be debbuged
        cls.page_object.logout()
        cls.page_object.screenshot()
        cls.page_object.close()
        #pass