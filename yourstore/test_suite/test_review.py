from yourstore.POM.home_page import Homepage

def test_review(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    search_page=homepage.send_product("imac")
    review_page=search_page.product1()
    review_page.add_a_review("helloooo","good morning.................................................")
    review_page.success_msg()


def test_review2(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    search_page=homepage.send_product("imac")
    review_page=search_page.product1()
    review_page.add_review_2()
    review_page.error_msg()

def test_review3(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    search_page=homepage.send_product("imac")
    review_page=search_page.product1()
    review_page.add_review_3()
    review_page.error_msg()

def test_review4(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    search_page=homepage.send_product("imac")
    review_page=search_page.product1()
    review_page.add_review_4()
    review_page.rating_error_msg()

def test_review5(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    search_page=homepage.send_product("imac")
    review_page=search_page.product1()
    review_page.add_review_5()
    review_page.error_review_text()

def test_review6(get_browser):
    homepage = Homepage(get_browser)
    login_page = homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com", "selenium")
    search_page=homepage.send_product("imac")
    review_page=search_page.product1()
    review_page.add_review_6()
    review_page.rating_error_msg()