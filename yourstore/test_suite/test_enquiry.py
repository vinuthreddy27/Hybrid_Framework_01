from yourstore.POM.home_page import Homepage



def test_enquiry(driver):
    homepage = Homepage(driver)
    login_page = homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    enquiry_page=homepage.contact_us()
    enquiry_page.enquiry("vinuthreddy","reddyvinuth27@gmail.com","i just need additional info about ipod")