import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def driver():
  global driver
  driver=webdriver.Chrome()
  driver.maximize_window()
  driver.get("https://tutorialsninja.com/demo/")
  yield driver
  driver.quit()

