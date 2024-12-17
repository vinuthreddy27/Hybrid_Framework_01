
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

    driver.implicitly_wait(3)
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    yield driver
    driver.quit()

# @pytest.hookimpl(hookwrapper=True,tryfirst=True)
# def report(item,call):
#     outcome=yield
#     rep=outcome.get_result()
#     setattr(item,"rep_" + rep.when,rep)
#     return rep
#
# @pytest.fixture()
# def log_on_failure(request):
#     yield
#     item=request.node
#     if item.rep_call.failed:
#         allure.attach(driver.get_screenshot_as_png(),name="failure",attachment_type=AttachmentType.PNG)


