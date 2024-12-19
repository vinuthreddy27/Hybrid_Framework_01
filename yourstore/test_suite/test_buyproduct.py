from yourstore.POM.home_page import Homepage
from yourstore.configurations.config import TestData


def test_buyproduct(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    login_page.login_page.login_into_application(TestData.email,TestData.password)
    search_page=homepage.send_product("iPod Touch")
    search_page.product2()
    search_page.success_Msg()
