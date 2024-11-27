import pytest

from yourstore.POM.home_page import Homepage


@pytest.mark.skip
def test_enquiry(driver):
    homepage=Homepage(driver)
    Loginpage=homepage.login_()
    Loginpage.login_into_application("reddyvinuth27@gmail.com","selenium")
    Enquiry_page=homepage.contact_us()
    Enquiry_page.enquiry("vinuthreddy","reddyvinuth27@gmail.com","i just need additional info about ipod")