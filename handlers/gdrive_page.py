from handlers.ui_base import UIBase


class GDriveUI(UIBase):

    @property
    def my_drive_button(self):
        return self._generic_id_element('nt:D')

    @property
    def shared_with_me_button(self):
        return self._generic_id_element('nt:Driv')

    @property
    def recent_button(self):
        return self._generic_id_element('nt:Drive')

    @property
    def starred_button(self):
        return self._generic_id_element('nt:DriveD')

    @property
    def trash_button(self):
        return self._generic_id_element('nt:DriveDo')
