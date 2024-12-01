import pytest
from selenium import webdriver
from yourstore.utilities import configReader


@pytest.fixture(autouse=True)
def driver_():
    global driver
    browser_name = configReader.read_configuration("basic_info", "browser")
    if browser_name.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser_name.__eq__("edge"):
       driver = webdriver.Edge()
    elif browser_name.__eq__("firefox"):
        driver = webdriver.Firefox()
    else:
        print("invalid browser")
    driver.implicitly_wait(10)
    driver.get(configReader.read_configuration("basic_info", "url"))
    driver.maximize_window()
    yield
    driver.quit()