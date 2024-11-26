from yourstore.POM.home_page import Homepage


def test_buyproduct(driver):
    homepage=Homepage(driver)
    Loginpage=homepage.login_()
    Loginpage.login_into_application("reddyvinuth27@gmail.com","selenium")
    Search_page=homepage.send_product("iPod Touch")
    Search_page.product2()
    homepage.total_cart()
