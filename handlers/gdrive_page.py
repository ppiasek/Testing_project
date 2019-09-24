from handlers.ui_base import UIBase


class GDriveUI:

    def __init__(self, driver):
        self._driver = driver

    @property
    def my_drive_button(self):
        return self._driver.find_element_by_id('nt:D')

    @property
    def shared_with_me_button(self):
        return self._driver.find_element_by_id('nt:Driv')

    @property
    def recent_button(self):
        return self._driver.find_element_by_id('nt:Drive')

    @property
    def starred_button(self):
        return self._driver.find_element_by_id('nt:DriveD')

    @property
    def trash_button(self):
        return self._driver.find_element_by_id('nt:DriveDo')
