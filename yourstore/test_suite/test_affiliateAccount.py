from yourstore.POM.home_page import Homepage


def test_affiliate(get_browser):
    homepage=Homepage(get_browser)
    login_page = homepage.login_()
    landing_page = login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")

    affiliate_page=landing_page.edit_affiliate_account()
    affiliate_page.edit_affiliate("xyz","sssss","dddd","ssss")
