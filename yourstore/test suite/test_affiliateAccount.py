from yourstore.POM.home_page import Homepage


def test_affiliate(driver):
    homepage=Homepage(driver)
    Loginpage=homepage.login_()
    Landing_page=Loginpage.login_into_application("reddyvinuth27@gmail.com","selenium")
    Edit_affiliate=Landing_page.edit_affiliate_account()
    Edit_affiliate.edit_affiliate("xyz","sssss","dddd","ssss")
