import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://binge.buzz/')
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
