
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from yourstore.configurations.config import TestData

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
    driver.implicitly_wait(3)
    driver.get(TestData.base_url)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True,tryfirst=True)
def report(item,call):
    outcome=yield
    rep=outcome.get_result()
    setattr(item,"rep_" + rep.when,rep)
    return rep

@pytest.fixture()
def log_on_failure(request,get_browser):
    yield
    item=request.node
    driver=get_browser
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(),name="failure",attachment_type=AttachmentType.PNG)
