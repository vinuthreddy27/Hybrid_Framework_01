from yourstore.POM.home_page import Homepage

def test_login(get_browser):
    homepage=Homepage(get_browser)
    login_page=homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com",
                    "selenium")
def test_login2(get_browser):
    homepage=Homepage(get_browser)
    login_page=homepage.login_()
    login_page.login_into_application("vinuth27@gmail.com",
                    "selenium")

def test_login3(get_browser):
    homepage=Homepage(get_browser)
    login_page=homepage.login_()
    login_page.login_into_application("reddyvinuth27@gmail.com",
                    "sele")

def test_login4(get_browser):
    homepage=Homepage(get_browser)
    login_page=homepage.login_()
    login_page.login_into_application("",
                    "")

def test_login5(get_browser):
    homepage=Homepage(get_browser)
    login_page=homepage.login_()
    login_page.login_into_application("vinuthgmail.com",
                    "$$$$")

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