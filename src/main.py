import unittest
from test.python.tests.TestBase import BaseTest

import time

service = Service(executable_path = 'chromedriver.exe')
driver = webdriver.Chrome(service=service)

class TestExample(BaseTest, unittest.TestCase):

    def test_open_page(self):
        self.driver.get("https://binge.buzz/")
        title = self.driver.title
        self.assertIn("Example Domain", title)

    def tearDown(self):
        self.teardown()
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://binge.buzz/")
time.sleep(10)

input_element = driver.find_element(By.XPATH, "//button[contains(@class, 'css-8xcdnj')]")
input_element.click()

driver.close()