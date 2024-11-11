from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LandingPage(BasePage):
    loginButton = (By.XPATH,'//*[@id="root"]//button[text()="Login"]')

    def click_login(self):
        self.driver.find_element(*self.loginButton).click()


