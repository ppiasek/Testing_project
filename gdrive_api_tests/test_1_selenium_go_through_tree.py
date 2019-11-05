from handlers import ui_testbase


class GDriveTreeTest(ui_testbase.UITestBase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_1_shared(self):
        self.ui.main_page.shared_with_me_button.click()
        self.ui.screenshot(wait=0.5)
        self.assertTrue(self.ui.main_page._driver.current_url == 'https://drive.google.com/drive/shared-with-me',
                        f'Current URL: {self.ui.main_page._driver.current_url}')

    def test_2_recent(self):
        self.ui.main_page.recent_button.click()
        self.assertTrue(self.ui.main_page._driver.current_url == 'https://drive.google.com/drive/recent',
                        "Recent not selected")
        self.ui.screenshot()

    def test_3_starred(self):
        self.ui.main_page.starred_button.click()
        self.assertTrue(self.ui.main_page._driver.current_url == 'https://drive.google.com/drive/starred',
                        "Starred not selected")
        self.ui.screenshot()

    def test_4_trash(self):
        self.ui.main_page.trash_button.click()
        self.assertTrue(self.ui.main_page._driver.current_url == 'https://drive.google.com/drive/trash',
                        "Trash not selected")
        self.ui.screenshot()

    def test_5_my_drive(self):
        self.ui.main_page.my_drive_button.click()
        self.assertTrue(self.ui.main_page._driver.current_url == 'https://drive.google.com/drive/my-drive',
                        "My Drive not selected")
        self.ui.screenshot()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
