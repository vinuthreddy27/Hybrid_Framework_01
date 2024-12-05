from yourstore.POM.home_page import Homepage


def test_search(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    search_page=homepage.send_product("Samsung Galaxy Tab 10.1")
    search_page.product_info()

def test_search2(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    search_page = homepage.send_product("iPod Touch")
    search_page.product2()

    assert search_page.success_Msg()

def test_search3(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    search_page = homepage.send_product("")
    assert search_page.product_Msg()