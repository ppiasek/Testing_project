from handlers import ui_testbase


class LogoutTest(ui_testbase.UITestBase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_1_logout(self):
        self.ui.logout_page.user_view.click()
        self.ui.screenshot()
        self.ui.logout_page.user_logout.click()
        self.ui.screenshot()
        self.assertTrue(self.ui.logout_page.user_logged_out.is_displayed(), "User not logged out")

    @classmethod
    def tearDownClass(cls):
        cls.ui.main_page.close()
