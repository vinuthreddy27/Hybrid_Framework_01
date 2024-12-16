

from yourstore.POM.home_page import Homepage

def test_edit(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    landing_page=login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    modify_account_page=landing_page.edit_account_info()
    modify_account_page.modify("9988776655")


