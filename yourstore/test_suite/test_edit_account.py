

from yourstore.POM.home_page import Homepage
from yourstore.configurations.config import TestData


def test_edit(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    landing_page=login_page.login_page.login_into_application(TestData.email,TestData.password)
    modify_account_page=landing_page.edit_account_info()
    modify_account_page.modify("9988776655")


