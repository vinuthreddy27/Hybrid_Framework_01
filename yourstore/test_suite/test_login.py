from yourstore.POM.home_page import Homepage
from yourstore.configurations.config import TestData
from yourstore.test_suite.base_test import BaseTest


class Test_login(BaseTest):


    def test_login11(self,get_browser):
      homepage = Homepage(get_browser)
      login_page = homepage.login_()
      landing_page = login_page.login_into_application(TestData.email, TestData.password)
      landing_page.proper_msg()

    def test_login21(self, get_browser):
        homepage = Homepage(get_browser)
        login_page = homepage.login_()
        login_page.login_into_application("vinuth27@gmail.com",
                                          "selenium")
        login_page.display_error_msg()

    def test_login31(self, get_browser):
        homepage = Homepage(get_browser)
        login_page = homepage.login_()
        login_page.login_into_application("reddyvinuth27@gmail.com",
                                          "sele")
        login_page.display_error_msg()

    def test_login41(self, get_browser):
        homepage = Homepage(get_browser)
        login_page = homepage.login_()
        login_page.login_into_application("",
                                          "")
        login_page.display_error_msg()

    def test_login51(self, get_browser):
        homepage = Homepage(get_browser)
        login_page = homepage.login_()
        login_page.login_into_application("vinuthgmail.com",
                                          "$$$$")
        login_page.display_error_msg()

    def test_login61(self, get_browser):
        homepage = Homepage(get_browser)
        login_page = homepage.login_()
        forgot_page = login_page.click_forgot_password()
        forgot_page.me_ssage()

    def test_login71(self, get_browser):
        homepage = Homepage(get_browser)
        register_page = homepage.register()
        register_page.click_on_login()
        driver = get_browser
        if driver.title == "Account Login":
            print("yes")
        print(driver.title)

    def test_login81(self, get_browser):
        homepage = Homepage(get_browser)
        login_page = homepage.login_()
        login_page.login_into_application(TestData.email, TestData.password)
        logout_page = homepage.logout()

        logout_page.account_logout()




