import pytest

from yourstore.POM.home_page import Homepage

@pytest.mark.skip
def test_edit(driver):
    homepage=Homepage(driver)
    Loginpage=homepage.login_()
    Landing_page=Loginpage.login_into_application("reddyvinuth27@gmail.com",
                                          "selenium")
    Modify_account=Landing_page.edit_account_info()
    Modify_account.modify("6969696969")

