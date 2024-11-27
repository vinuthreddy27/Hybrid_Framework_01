import pytest

from yourstore.POM.home_page import Homepage

@pytest.mark.skip
def test_logout(driver):
    homepage=Homepage(driver)
    Loginpage=homepage.login_()
    Loginpage.login_into_application("reddyvinuth27@gmail.com","selenium")
    Logout_page=homepage.logout()
    assert Logout_page.account_logout()

