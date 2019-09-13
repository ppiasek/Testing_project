from handlers.test_base import TestBase
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class LoginPage(TestBase):

    @property
    def navigate_to_login_page(self):
        return self._driver.find_element_by_link_text('Go to Google Drive')

    @property
    def login_field(self):
        return self._driver.find_element_by_id('identifierId')

    @property
    def login_field_next_button(self):
        return self._driver.find_element_by_class_name('U26fgb O0WRkf zZhnYe e3Duub C0oVfc nDKKZc DL0QTb')

    @property
    def password_field(self):
        #return self._driver.find_element_by_xpath('//input[@name="password"]')
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
        return self._driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')


    @property
    def password_field_next_button(self):
        return self._driver.find_element_by_class_name('ZFr60d CeoRYc')
