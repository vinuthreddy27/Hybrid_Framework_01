import pytest
from yourstore.POM.home_page import Homepage

@pytest.mark.skip
def test_login(driver):
    homepage=Homepage(driver)
    login_page=homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com",
                    "selenium")
