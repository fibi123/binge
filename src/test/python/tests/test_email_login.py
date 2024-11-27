import pytest
from pages.email_login_page import EmailLoginPage
from pages.landing_page import LandingPage
from utils.configurations import get_user_data
import time

def test_email_login(driver):
    landing_page = LandingPage(driver)
    landing_page.click_login()

    email_login_page = EmailLoginPage(driver)
    email_login_page.enter_email(get_user_data("email"))
    email_login_page.enter_password(get_user_data("password"))
