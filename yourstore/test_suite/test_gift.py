import pytest
from yourstore.POM.home_page import Homepage
from yourstore.configurations.config import TestData
from yourstore.utilities.excel_reader import get_data_from_excel

# @pytest.mark.skip
# @pytest.mark.parametrize("email,password,name,mail,yn,email2,msg,amnt",get_data_from_excel())
# def test_gift(get_browser,email,password,name,mail,yn,email2,msg,amnt):
#     homepage=Homepage(get_browser)
#     login_page=homepage.login_()
#     login_page.login_page.login_into_application(TestData.email,TestData.password)
#     gift_page=homepage.gift_link()
#     gift_page.gift(name,mail,yn,email2,msg,amnt)
