from yourstore.POM.home_page import Homepage


def test_login(driver):
    homepage=Homepage(driver)
    Loginpage=homepage.login_()
    Loginpage.login_into_application("reddyvinuth27@gmail.com",
                    "selenium")
