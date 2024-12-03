import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome","edge"],scope="function")
def get_browser(request):
    if request.param=="chrome":
        driver = webdriver.Chrome()
    elif request.param=="edge":
       driver = webdriver.Edge()
    else:
        print("invalid browser")

    driver.implicitly_wait(10)
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    yield driver
    driver.quit()