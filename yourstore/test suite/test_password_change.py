from yourstore.POM.home_page import Homepage
from yourstore.POM.landing_page import Landing_page
import pytest
from yourstore.POM.search_page import Search_page



def test_password_change(driver):
    homepage=Homepage(driver)
    login_page=homepage.login_()
    landing_page=login_page.login_into_application("reddyvinuth27@gmail.com","selenium")
    password_page=landing_page.change_password()
    password_page.change("selenium","selenium")

    assert Landing_page.password_changed()


def test_password_change2(driver):
    homepage = Homepage(driver)
    login_page = homepage.login_()
    landing_page = login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    password_page = landing_page.change_password()
    Password_change_page.change("selenium", "seleniu")

    assert Password_change_page.display_error_msg()


def test_password_change2(driver):
    homepage = Homepage(driver)
    login_page = homepage.login_()
    landing_page = login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    password_page = landing_page.change_password()
    Password_change_page.change("", "")

    assert Password_change_page.display_error_msg2()