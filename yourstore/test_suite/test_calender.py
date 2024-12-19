from yourstore.POM.home_page import Homepage
from yourstore.configurations.config import TestData


def test_calender(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    login_page.login_page.login_into_application(TestData.email,TestData.password)
    search_page=homepage.send_product("HP LP3065")
    search_page.click_link()
    search_page.select_date("April 2014")
    search_page.previous_date("July 2013")