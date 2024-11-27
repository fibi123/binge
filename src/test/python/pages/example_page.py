from aquality.selenium.elements import ElementType
from aquality.selenium.forms import Form
from aquality.selenium.elements.interfaces import ITextBox
from selenium.webdriver.common.by import By

class MainPage(Form):
    def __init__(self):
        super().__init__(By.ID, "main_page", "Main Page")  # Specify locator and name of the page
        self.search_box: ITextBox = self.element_factory.get_text_box(By.ID, "searchBox", "Search Box")

    def enter_search_query(self, query):
        self.search_box.clear_and_type(query)
