from handlers.ui_base import UIBase


class GDriveLoginUI(UIBase):

    @property
    def navigate_to_login_page(self):
        return self._generic_text_element('Go to Google Drive')

    @property
    def login_field(self):
        return self._generic_id_element('identifierId')

    @property
    def login_field_next_button(self):
        return self._generic_id_element('identifierNext')

    @property
    def password_field(self):
        return self._generic_name_element('password')

    @property
    def password_field_next_button(self):
        return self._generic_id_element('passwordNext')

    @property
    def user_logged_in(self):
        return self._generic_id_element('drive_main_page')
