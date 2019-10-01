from handlers.ui_base import UIBase


class GDriveLogoutUI(UIBase):

    @property
    def user_view(self):
        return self._driver.find_element_by_css_selector('#gb > div:nth-of-type(2) > div:nth-of-type(3) > div > div:nth-of-type(2) > div > a')

    @property
    def user_logout(self):
        return self._driver.find_element_by_id('gb_71')

    @property
    def user_logged_out(self):
        return self._driver.find_element_by_id('yDmH0d')
