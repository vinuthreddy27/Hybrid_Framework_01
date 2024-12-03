
from yourstore.POM.home_page import Homepage

def test_register(get_browser):
    homepage=Homepage(get_browser)
    register_page=homepage.register()
    account_success_page=register_page.register_form("vinuth",
                                "reddy",
                                "reddyvinuth27@gmail.com",
                                "7676252914",
                                "framework",
                                "framework")

    assert account_success_page.msg_()

def test_register2(get_browser):
    homepage = Homepage(get_browser)
    register_page = homepage.register()
    register_page.register_with__no_fn()

    assert register_page.error_msg()
