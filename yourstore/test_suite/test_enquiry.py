from yourstore.POM.home_page import Homepage



def test_enquiry(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    enquiry_page=homepage.contact_us()
    enquiry_page.enquiry("i just need additional info about ipod")