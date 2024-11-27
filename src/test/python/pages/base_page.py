from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)
        self._action = ActionChains(self._driver)

    def find(self, locator):
        return self._driver.find_element(*locator)

    def switch_to_new_window(self, target_window_handle):
        WebDriverWait(self._driver, 10).until(
            ec.new_window_is_opened(self._driver.window_handles)
        )
        self._driver.switch_to.window(target_window_handle)

    def close_and_switch_to_window(self, original_window):
        self._driver.close()
        self._driver.switch_to.window(original_window)

