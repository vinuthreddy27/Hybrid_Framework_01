

from yourstore.POM.home_page import Homepage


def test_edit(driver):
    homepage = Homepage(driver)
    login_page = homepage.login_()
    landing_page=login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    modify_account=landing_page.edit_account_info()
    modify_account.modify("6969696969")

