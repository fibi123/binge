import pytest

from pages.landing_page import LandingPage
from pages.login_page import LoginPage
from selenium import webdriver

def test_login(driver):
    landing_page  = LandingPage(driver)
    landing_page.click_login()
    login_page = LoginPage(driver)
    login_page.is_displayed()

