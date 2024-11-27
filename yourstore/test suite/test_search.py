import pytest

from yourstore.POM.home_page import Homepage

@pytest.mark.skip
def test_search(driver):
    homepage=Homepage(driver)
    Loginpage=homepage.login_()
    Loginpage.login_into_application("reddyvinuth27@gmail.com","selenium")
    Search_page=homepage.send_product("Samsung Galaxy Tab 10.1")
    Search_page.product_info()
@pytest.mark.skip
def test_search2(driver):
        homepage = Homepage(driver)
        Loginpage = homepage.login_()
        Loginpage.login_into_application("reddyvinuth27@gmail.com", "selenium")
        Search_page = homepage.send_product("iPod Touch")
        Search_page.product2()

        assert Search_page.success_Msg()