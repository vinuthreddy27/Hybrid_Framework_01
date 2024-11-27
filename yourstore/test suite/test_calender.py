import pytest

from yourstore.POM.home_page import Homepage
@pytest.mark.skip
def test_calender(driver):
    homepage=Homepage(driver)
    Loginpage=homepage.login_()
    Loginpage.login_into_application("reddyvinuth27@gmail.com","selenium")
    Search_page=homepage.send_product("HP LP3065")
    Search_page.click_link()
    Search_page.select_date("April 2014")
    Search_page.previous_date("July 2013")