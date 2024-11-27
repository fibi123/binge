from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class GoogleSigninPage(BasePage):
    PAGE_IDENTIFIER = (By.XPATH, "//button[@jsname = 'Cuz2Ue'] ")
    __email_input = (By.XPATH, "//input[@type= 'email']")
    __next_button = (By.XPATH, "//div[@id='identifierNext']")

    def enter_email(self, s: str):
        self.find(self.__email_input).send_keys(s)

    def click_next(self):
        self.find(self.__next_button).click()

