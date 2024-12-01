
from yourstore.POM.home_page import Homepage


def test_logout(driver):
    homepage = Homepage(driver)
    login_page = homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    logout_page=homepage.logout()
    assert logout_page.account_logout()

