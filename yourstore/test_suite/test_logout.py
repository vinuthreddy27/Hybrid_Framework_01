from yourstore.POM.home_page import Homepage
from yourstore.configurations.config import TestData


def test_logout(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    login_page.login_page.login_into_application(TestData.email,TestData.password)
    logout_page=homepage.logout()
    assert logout_page.account_logout()

def test_logout2(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    landing_page=login_page.login_into_application(TestData.email,TestData.password)
    logout_page=landing_page.click_on_logout()
    assert logout_page.account_logout()
