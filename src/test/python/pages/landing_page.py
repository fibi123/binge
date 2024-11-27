from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LandingPage(BasePage):
    __login_button = (By.XPATH,'//*[@id="root"]//button[text()="Login"]')
    __close_ad_button = (By.XPATH, '//button[@aria-label = "close"]')

    def click_login(self):
        self.find(self.__login_button).click()

    def close_ad(self):
        self.find(self.__close_ad_button).click()

