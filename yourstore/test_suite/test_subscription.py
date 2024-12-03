from yourstore.POM.home_page import Homepage


def test_subscription(driver):
    homepage = Homepage(driver)
    login_page = homepage.login_()
    landing_page=login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    subscription_page=landing_page.newsletter_link()
    subscription_page.Yes()

    assert subscription_page.validate_yes()


def test_subscription2(driver):
    homepage = Homepage(driver)
    login_page = homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    landing_page=login_page.login_into_application("reddyvinuth27@gmail.com","selenium")
    subscription_page=landing_page.newsletter_link()
    subscription_page.No()

    assert subscription_page.validate()