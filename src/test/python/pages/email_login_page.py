from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class EmailLoginPage(BasePage):
    __email = (By.XPATH("//input[@type = 'text']"))
    __password = (By.XPATH("//input[@type = 'password']"))
    __submit_button = (By.XPATH("//button[@fdprocessedid = 'pcz7lr']"))

    def enter_email(self, s:str):
        self.find(self.__email).send_keys(s)

    def enter_password(self, s:str):
        self.find(self.__password).send_keys(s)

    def click_submit(self):
        self.find(self.__submit_button).click()
