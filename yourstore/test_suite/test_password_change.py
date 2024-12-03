from yourstore.POM.home_page import Homepage


def test_password_change(driver):
    homepage=Homepage(driver)
    login_page=homepage.login_()
    landing_page=login_page.login_into_application("reddyvinuth27@gmail.com","selenium")
    password_page=landing_page.change_password()
    password_page.change("selenium","selenium")

    assert landing_page.password_changed()


def test_password_change2(driver):
    homepage = Homepage(driver)
    login_page = homepage.login_()
    landing_page = login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    password_page = landing_page.change_password()
    password_page.change("selenium", "seleniu")

    assert password_page.display_error_msg()


def test_password_change3(driver):
    homepage = Homepage(driver)
    login_page = homepage.login_()
    landing_page = login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    password_page = landing_page.change_password()
    password_page.change("", "")

    assert password_page.display_error_msg2()