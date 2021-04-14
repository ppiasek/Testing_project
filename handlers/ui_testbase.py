import unittest
from handlers.ui_functions import UIFunctions


class UITestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ui = UIFunctions()
        cls.ui.login()
        cls.ui.screenshot(wait=1)

    @classmethod
    def tearDownClass(cls):
        cls.ui.logout()
        cls.ui.screenshot(wait=1)
        cls.ui.main_page.close()
