from yourstore.POM.home_page import Homepage



def test_wishlist(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    search_page=homepage.send_product("ipod touch")
    search_page.add_wishlist()

    assert search_page.added_to_wishlist()


def test_wishlist2(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    search_page=homepage.send_product("ipod touch")
    search_page.add_wishlist()

    assert search_page.added_to_wishlist()
