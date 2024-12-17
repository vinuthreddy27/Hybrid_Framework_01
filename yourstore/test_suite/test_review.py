from time import sleep

from yourstore.POM.home_page import Homepage

def test_review(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    search_page=homepage.send_product("imac")
    review_page=search_page.product1()
    review_page.add_a_review("helloooo","good morning.................................................")
    sleep(5)


