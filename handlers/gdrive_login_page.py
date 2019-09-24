

class GDriveLoginUI:

    def __init__(self, driver):
        self._driver = driver

    @property
    def navigate_to_login_page(self):
        return self._driver.find_element_by_link_text('Go to Google Drive')

    @property
    def login_field(self):
        return self._driver.find_element_by_id('identifierId')

    @property
    def login_field_next_button(self):
        return self._driver.find_element_by_id('identifierNext')

    @property
    def password_field(self):
        return self._driver.find_element_by_name('password')

    @property
    def password_field_next_button(self):
        return self._driver.find_element_by_id('passwordNext')

    @property
    def user_logged_in(self):
        return self._driver.find_element_by_id('drive_main_page')
