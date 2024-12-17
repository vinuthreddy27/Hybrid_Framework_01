from yourstore.POM.home_page import Homepage

def test_register(get_browser):
    homepage=Homepage(get_browser)
    register_page=homepage.register()
    account_success_page=register_page.register_form("vinuth",
                                "reddy",
                                "7676252914",
                                "framework",
                                "framework")

    account_success_page.msg_()


def test_register3(get_browser):
    homepage=Homepage(get_browser)
    register_page=homepage.register()
    account_success_page=register_page.register_form_mandator_Fields("chris",
                                                "gayle",
                                                "8888888888",
                                                "kkrr",
                                                "kkrr")
    account_success_page.msg_()

def test_register2(get_browser):
    homepage = Homepage(get_browser)
    register_page = homepage.register()
    register_page.register_with_no_fn()

    register_page.error_msg()


def test_register4(get_browser):
    homepage=Homepage(get_browser)
    register_Page=homepage.register()
    register_Page.register()

    register_Page.con_password_error_msg()


def test_register5(get_browser):
    homepage=Homepage(get_browser)
    register_Page=homepage.register()
    landing_Page=register_Page.register2("jason",
                                         "roy",
                                         "999999999",
                                         "selenium",
                                         "selenium")
    subscription_page =landing_Page.newsletter_link()
    subscription_page.validate()

def test_register6(get_browser):
    homepage=Homepage(get_browser)
    register_Page=homepage.register()
    landing_Page=register_Page.register2("jason",
                                         "roy",
                                         "999999999",
                                         "selenium",
                                         "selenium")
    subscription_page =landing_Page.newsletter_link()
    subscription_page.validate_yes()

def test_register7(get_browser):
    homepage=Homepage(get_browser)
    register_Page=homepage.register()
    register_Page.register_with_fn_32()

    register_Page.fn_error_msg()

def test_register8(get_browser):
    homepage=Homepage(get_browser)
    register_Page=homepage.register()
    register_Page.register_with_wrong_telephone_number()

    register_Page.fn_error_msg()

def test_register9(get_browser):
    homepage=Homepage(get_browser)
    register_Page=homepage.register()
    register_Page.register_with_wrong_telephone_number2()

    register_Page.phno_error_msg()

def test_register10(get_browser):
    homepage=Homepage(get_browser)
    register_Page=homepage.register()
    register_Page.register_with_wrong_telephone_number3()

    register_Page.phno_error_msg()