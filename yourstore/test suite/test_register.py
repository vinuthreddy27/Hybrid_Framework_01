from yourstore.POM.home_page import Homepage


def test_register(driver):
    homepage=Homepage(driver)
    Register_page=homepage.register()
    Account_success=Register_page.register_form("vinuth",
                                "reddy",
                                "reddyvinuth27@gmail.com",
                                "7676252914",
                                "framework",
                                "framework")

    assert Account_success.msg__()

def test_register2(driver):
    homepage = Homepage(driver)
    Register_page = homepage.register()
    Register_page.register_with__no_fn()

    assert Register_page.error_msg()
