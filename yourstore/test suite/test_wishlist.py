import pytest
from yourstore.POM.home_page import Homepage


@pytest.mark.smoke
def test_wishlist(driver):
    homepage=Homepage(driver)
    Loginpage=homepage.login_()
    Loginpage.login_into_application("reddyvinuth27@gmail.com","selenium")
    Search_page=homepage.send_product("ipod touch")
    Search_page.add_wishlist()

    assert Search_page.added_to_wishlist()


