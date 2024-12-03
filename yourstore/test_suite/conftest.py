import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome"],scope="class")
def get_browser(request):
    global driver
    if request.param=="chrome":
        driver = webdriver.Chrome()
    elif request.param=="edge":
       driver = webdriver.Edge()
    elif request.param=="firefox":
        driver=webdriver.Firefox()
    else:
        print("invalid browser")

    driver.implicitly_wait(10)
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    yield driver
    driver.quit()