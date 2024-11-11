from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    mobile_number_input = (By.XPATH("//input[@class = 'PhoneInputInput']"))
    generate_otp = (By.XPATH("//button[@class = 'BingeBtnBase-root css-1h228gw']"))
    facebook_button = (By.XPATH("//button[contains(@class, 'css-1usjl9m')]"), 'facebook')
    google_button = (By.XPATH("//button[@aria-label = 'Login with Google']"), 'google account')
    email_button = (By.XPATH("//button[@aria-label = 'Login with Email']"))

    def enter_mobile_number(self, mobile_number: str):
        self.mobile_number_input.send_keys(mobile_number)

