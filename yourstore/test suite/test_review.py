from yourstore.POM.home_page import Homepage
from yourstore.POM.review_page import Review_page


def test_review(driver):
    homepage=Homepage(driver)
    Login_page=homepage.login_()
    Login_page.login_into_application("reddyvinuth27@gmail.com","selenium")
    Search_page=homepage.send_product("imac")
    Review_page=Search_page.product1()
    Review_page.add_a_review("helloooo","good morning")


