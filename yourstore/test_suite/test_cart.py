import pytest

from yourstore.POM.home_page import Homepage

@pytest.mark.skip
def test_cart(get_browser):
    homepage=Homepage(get_browser)
    login_page=homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com","selenium")
    search_page=homepage.send_product("iphone")
    search_page.add_2_cart()
    cart_page=homepage.total_cart()
    cart_page.click_on_view_cart()

    cart_page.display_the_info()