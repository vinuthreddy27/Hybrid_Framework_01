from yourstore.POM.home_page import Homepage
from yourstore.POM.landing_page import Landing_page
import pytest

@pytest.mark.skip
def test_password_change(driver):
    homepage=Homepage(driver)
    Loginpage=homepage.login_()
    Landing_page=Loginpage.login_into_application("reddyvinuth27@gmail.com","selenium")
    Password_change_page=Landing_page.change_password()
    Password_change_page.change("selenium","selenium")

    assert Landing_page.password_changed()