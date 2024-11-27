import pytest
from pages.landing_page import LandingPage
from pages.login_page import LoginPage
from pages.google_password_page import GooglePasswordPage
from pages.google_signin_page import GoogleSigninPage
from utils.configurations import get_user_data
import time

def test_google_login(driver):
    landing_page  = LandingPage(driver)
    landing_page.close_ad()
    landing_page.click_login()
    login_page = LoginPage(driver)
    assert login_page.login_page_displayed(), 'Login page not displayed'

    login_page.click_google_login()

    time.sleep(3)

    all_handles = driver.window_handles
    original_window = driver.current_window_handle
    for handle in all_handles:
        if handle != original_window:
            driver.switch_to.window(handle)
            break

    time.sleep(3)
    google_signin_page = GoogleSigninPage(driver)

    google_signin_page.enter_email(get_user_data("email"))
    google_signin_page.click_next()

    time.sleep(3)
    google_password_page = GooglePasswordPage(driver)
    google_password_page.enter_password(get_user_data("password"))
    google_password_page.click_next()

    time.sleep(3)
    driver.switch_to.window(original_window)


