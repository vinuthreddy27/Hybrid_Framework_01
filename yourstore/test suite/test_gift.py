import pytest
from yourstore.POM.home_page import Homepage
from yourstore.utilities.excel_reader import get_data_from_excel


@pytest.mark.parametrize("email,password,name,mail,yn,email2,msg,amnt",get_data_from_excel())
def test_gift(driver,email,password,name,mail,yn,email2,msg,amnt):
    homepage=Homepage(driver)
    Loginpage=homepage.login_()
    Loginpage.login_into_application(email,password)
    Gift_page=homepage.gift_link()
    Gift_page.gift(name,mail,yn,email2,msg,amnt)
