import pytest
from selenium import webdriver

@pytest.fixture(scope = "class")
def driver():
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get('https://binge.buzz/')
    driver.implicitly_wait(10)
    yield driver
    driver.close()
