from yourstore.POM.home_page import Homepage
from yourstore.configurations.config import TestData


def test_wishlist(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    login_page.login_page.login_into_application(TestData.email,TestData.password)
    search_page=homepage.send_product("ipod touch")
    search_page.added_to_wishlist()

def test_wishlist2(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    login_page.login_page.login_into_application(TestData.email,TestData.password)
    search_page=homepage.send_product("ipod touch")
    search_page.added_to_wishlist()
    wish_page=homepage.click_wishlist()
    wish_page.click_on_remove_btn()
    wish_page.dispaly_msg()



def test_wishlist_3(get_browser):
    homepage=Homepage(get_browser)
    login_page=homepage.login_()
    login_page.login_page.login_into_application(TestData.email,TestData.password)
    homepage.send_product("imac")
    wish_page=homepage.click_wishlist()
    wish_page.cart_btn_click()
    homepage.shopping_cart_click()