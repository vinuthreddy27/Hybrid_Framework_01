import pytest

from yourstore.POM.home_page import Homepage

def test_password_change(get_browser):
    homepage=Homepage(get_browser)
    login_page=homepage.login_()
    landing_page=login_page.login_into_application("reddyvinuth27@gmail.com","selenium")
    password_page=landing_page.change_password()
    password_page.change("selenium","selenium")

    landing_page.password_changed()

def test_password_change2(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    landing_page = login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    password_page = landing_page.change_password()
    password_page.change("selenium", "seleniu")

    password_page.display_error_msg()

def test_password_change3(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    landing_page = login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    password_page = landing_page.change_password()
    password_page.change("", "")

    password_page.display_error_msg2()

def test_password_change4(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    landing_page = login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    homepage.click_my_account()
    landing_page.change_password()
    driver=get_browser
    print(driver.title)

def test_password_change5(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    landing_page = login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    landing_page.click_password_link()
    driver = get_browser
    print(driver.title)

def test_password_change6(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    sitepage=homepage.click_on_sitemap()
    sitepage.click_on_password()
    driver = get_browser
    print(driver.title)