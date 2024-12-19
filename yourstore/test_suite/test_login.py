from yourstore.POM.home_page import Homepage



def test_login(get_browser):
    homepage=Homepage(get_browser)
    login_page=homepage.login_()
    landing_page=login_page.login_into_application("reddyvinuth27@gmail.com",
                    "selenium")
    landing_page.proper_msg()


def test_login2(get_browser):
    homepage=Homepage(get_browser)
    login_page=homepage.login_()
    login_page.login_into_application("vinuth27@gmail.com",
                    "selenium")
    login_page.display_error_msg()


def test_login3(get_browser):
    homepage=Homepage(get_browser)
    login_page=homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com",
                    "sele")
    login_page.display_error_msg()

def test_login4(get_browser):
    homepage=Homepage(get_browser)
    login_page=homepage.login_()
    login_page.login_into_application("",
                    "")
    login_page.display_error_msg()

def test_login5(get_browser):
    homepage=Homepage(get_browser)
    login_page=homepage.login_()
    login_page.login_into_application("vinuthgmail.com",
                    "$$$$")
    login_page.display_error_msg()

def test_login_6(get_browser):
    homepage=Homepage(get_browser)
    login_page=homepage.login_()
    forgot_page=login_page.click_forgot_password()
    forgot_page.me_ssage()


def test_login_7(get_browser):
    homepage=Homepage(get_browser)
    register_page=homepage.register()
    register_page.click_on_login()
    driver=get_browser
    if driver.title == "Account Login":
        print("yes")
    print(driver.title)


def test_login_8(get_browser):
    homepage=Homepage(get_browser)
    login_page=homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com","selenium")
    logout_page=homepage.logout()

    logout_page.account_logout()
