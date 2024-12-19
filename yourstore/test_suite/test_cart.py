from time import sleep

from yourstore.POM.home_page import Homepage

def test_cart(get_browser):
    homepage=Homepage(get_browser)
    login_page=homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com","selenium")
    search_page=homepage.send_product("ipod touch")
    search_page.add_2_cart()
    cart_page=homepage.total_cart()
    cart_page.click_on_view_cart()
    cart_page.display_the_info()



def test_cart2(get_browser):
    homepage=Homepage(get_browser)
    login_page=homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com","selenium")
    search_page=homepage.send_product("imac")
    search_page.add_2_cart()
    cart_page=homepage.total_cart()
    view_page=cart_page.click_on_view_cart()
    cart_page.display_the_info()
    view_page.change_quantity()
