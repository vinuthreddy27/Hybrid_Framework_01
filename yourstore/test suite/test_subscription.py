import pytest

from yourstore.POM.home_page import Homepage

@pytest.mark.skip
def test_subscription(driver):
    homepage=Homepage(driver)
    Loginpage=homepage.login_()
    Landing_page=Loginpage.login_into_application("reddyvinuth27@gmail.com","selenium")
    Subscription_page=Landing_page.newsletter_link()
    Subscription_page.Yes()

    assert Subscription_page.validate_yes()
@pytest.mark.skip
def test_subscription2(driver):
    homepage=Homepage(driver)
    Loginpage=homepage.login_()
    Landing_page=Loginpage.login_into_application("reddyvinuth27@gmail.com","selenium")
    Subscription_page=Landing_page.newsletter_link()
    Subscription_page.No()

    assert Subscription_page.validate()