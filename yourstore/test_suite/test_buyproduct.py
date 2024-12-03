from yourstore.POM.home_page import Homepage


def test_buyproduct(get_browser):
    driver = get_browser
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    search_page=homepage.send_product("iPod Touch")
    search_page.product2()
    homepage.total_cart()
