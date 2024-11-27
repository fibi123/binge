import pytest
from pages.email_login_page import EmailLoginPage
from pages.landing_page import LandingPage
from pages.login_page import LoginPage
from utils.configurations import get_user_data
import time

def test_email_login(driver):
    landing_page = LandingPage(driver)
    landing_page.click_login()

    login_page = LoginPage(driver)
    login_page.enter_mobile_number(get_user_data("phone"))
    login_page.click_generate_otp()
    

    email_login_page.enter_email(get_user_data("email"))
    email_login_page.enter_password(get_user_data("password"))