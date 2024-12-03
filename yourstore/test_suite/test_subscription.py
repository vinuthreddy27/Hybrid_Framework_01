from yourstore.POM.home_page import Homepage


def test_subscription(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    landing_page=login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    subscription_page=landing_page.newsletter_link()
    subscription_page.Yes()

    assert subscription_page.validate_yes()


def test_subscription2(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    landing_page=login_page.login_into_application("reddyvinuth27@gmail.com","selenium")
    subscription_page=landing_page.newsletter_link()
    subscription_page.No()

    assert subscription_page.validate()