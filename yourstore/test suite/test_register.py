
from yourstore.POM.home_page import Homepage

def test_register(driver):
    homepage=Homepage(driver)
    register_page=homepage.register()
    account_success=register_page.register_form("vinuth",
                                "reddy",
                                "reddyvinuth27@gmail.com",
                                "7676252914",
                                "framework",
                                "framework")

    assert account_success.msg__()

def test_register2(driver):
    homepage = Homepage(driver)
    register_page = homepage.register()
    register_page.register_with__no_fn()

    assert register_page.error_msg()
