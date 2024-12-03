import pytest
from yourstore.POM.home_page import Homepage
from yourstore.utilities.excel_reader import get_data_from_excel2


@pytest.mark.parametrize("fn,ln,company,address,address2,city,postcode,option,state",get_data_from_excel2())
def test_address(get_browser,fn,ln,company,address,address2,city,postcode,option,state):
    homepage=Homepage(get_browser)
    login_page=homepage.login_()
    landing_page=login_page.login_into_application("reddyvinuth27@gmail.com","selenium")
    address_page=landing_page.click_address()
    address_page.default_Address(fn,ln,company,address,address2,city,postcode,option,state)
    