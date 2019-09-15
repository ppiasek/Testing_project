from handlers.test_base import TestBase
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By


class GDrivePage(TestBase):

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
        # pass_field = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
        # return pass_field
        return self._driver.find_element_by_name('password')

    @property
    def password_field_next_button(self):
        return self._driver.find_element_by_id('passwordNext')
        # next_button = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.ID, 'passwordNext')))
        # next_button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.ID, 'passwordNext')))
        # return next_button

    @property
    def user_logged_in(self):
        return self._driver.find_element_by_id('drive_main_page')

    @property
    def user_view(self):
        return self._driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[3]/div/div[2]/div/a')

    @property
    def user_logout(self):
        return self._driver.find_element_by_id('gb_71')

    @property
    def user_logged_out(self):
        return self._driver.find_element_by_id('yDmH0d')

    @property
    def my_drive_button(self):
        return self._driver.find_element_by_id('nt:D')

    @property
    def my_drive_text(self):
        return self._driver.find_element_by_class_name('h-sb-Ic h-R-w-d-ff')

    @property
    def shared_with_me_button(self):
        return self._driver.find_element_by_id('nt:Driv')

    @property
    def shared_with_me_text(self):
        return self._driver.find_element_by_xpath('//*[@id="drive_main_page"]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div/div/div[1]')

    @property
    def recent_button(self):
        return self._driver.find_element_by_id('nt:Drive')

    @property
    def recent_text(self):
        return self._driver.find_element_by_xpath('//*[@id="drive_main_page"]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div/div/div[1]')

    @property
    def starred_button(self):
        return self._driver.find_element_by_id('nt:DriveD')

    @property
    def starred_text(self):
        return self._driver.find_element_by_xpath('//*[@id="drive_main_page"]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div/div[5]/div/div[1]/div/div/div[1]')

    @property
    def trash_button(self):
        return self._driver.find_element_by_id('nt:DriveDo')

    @property
    def trash_text(self):
        return self._driver.find_element_by_xpath('//*[@id="drive_main_page"]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div/div[5]/div/div[1]/div/div/div[1]')
