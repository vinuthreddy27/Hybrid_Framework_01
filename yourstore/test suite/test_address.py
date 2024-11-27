import pytest
from yourstore.POM.home_page import Homepage
from yourstore.utilities.excel_reader import get_data_from_excel2

@pytest.mark.skip
@pytest.mark.parametrize("fn,ln,company,address,address2,city,postcode,option,state",get_data_from_excel2())
def test_address(driver,fn,ln,company,address,address2,city,postcode,option,state):
    homepage=Homepage(driver)
    Loginpage=homepage.login_()
    Landing_page=Loginpage.login_into_application("reddyvinuth27@gmail.com","selenium")
    Address_page_locators=Landing_page.click_address()
    Address_page_locators.default_Address(fn,ln,company,address,address2,city,postcode,option,state)
    