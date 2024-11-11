import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)
        self._action = ActionChains(self.driver)
