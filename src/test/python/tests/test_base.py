import pytest
from selenium import webdriver

class BaseTest:
    def __init__(self):
        self.driver = None

    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://binge.buzz/')

        yield self.driver

        if self.driver:
            self.driver.quit()
