import pytest
from yourstore.POM.home_page import Homepage


@pytest.mark.smoke
def test_wishlist(driver):
    homepage = Homepage(driver)
    login_page = homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    search_page=homepage.send_product("ipod touch")
    search_page.add_wishlist()

    assert search_page.added_to_wishlist()


def test_wishlist2(driver):
    homepage = Homepage(driver)
    login_page = homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    search_page=homepage.send_product("ipod touch")
    search_page.add_wishlist()

    assert search_page.added_to_wishlist()
