from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class GooglePasswordPage(BasePage):
    PAGE_IDENTIFIER = (By.ID, "forgotPassword")
    __password_input = (By.XPATH, "//input[@type='password']")
    __next_button = (By.ID, "passwordNext")

    def __init__(self, driver):
        super().__init__(driver, By.XPATH, "//body[@id='www-wikipedia-org']")


    def enter_password(self, s: str):
        password_field = WebDriverWait(self._driver, 10).until(
            ec.element_to_be_clickable(self.__password_input)
        )
        password_field.send_keys(s)

    def click_next(self):
        self.find(self.__next_button).click()
