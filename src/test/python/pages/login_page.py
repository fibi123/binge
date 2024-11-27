import json
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests.conftest import driver

class LoginPage(BasePage):
    __mobile_number_input = (By.XPATH, "//input[@class = 'PhoneInputInput']")
    __generate_otp = (By.XPATH, "//button[@fdprocessedid = 'rjwa1c']")
    __facebook_button = (By.XPATH, "//button[contains(@class, 'css-1usjl9m')]")
    __google_button = (By.XPATH, "//button[@aria-label = 'Login with Google']")
    __email_button = (By.XPATH, "//button[@aria-label = 'Login with Email']")
    __privacy_notice = (By.XPATH, "//u[text()='Privacy Notice']")
    __terms_and_conditions = (By.XPATH, "//u[text()='Terms & Condition']")

    def __init__(self, driver):
        super().__init__(driver)

    def login_page_displayed(self):
        return self.find(self.__generate_otp).is_displayed()

    def enter_mobile_number(self, mobile_number: str):
        return self.find(self.__mobile_number_input).send_keys(mobile_number)

    def click_google_login(self):
        self.find(self.__google_button).click()

    def click_generate_otp(self):
        self.find(self.__generate_otp).click()

