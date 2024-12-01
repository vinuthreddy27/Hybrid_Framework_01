from yourstore.POM.home_page import Homepage
from yourstore.POM.review_page import Review_page



def test_review(driver):
    homepage = Homepage(driver)
    login_page = homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    search_page=homepage.send_product("imac")
    review_page=search_page.product1()
    review_page.add_a_review("helloooo","good morning")


