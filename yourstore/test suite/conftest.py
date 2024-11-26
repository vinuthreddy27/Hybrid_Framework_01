import pytest
from selenium import webdriver
from yourstore.utilities import config_reader

@pytest.fixture(autouse=True)
def driver():
  global driver
  browser_name=config_reader.read_configuration("basic info","browser2")
  if browser_name.__eq__("edge"):
    driver = webdriver.Edge()
  elif browser_name.__eq__("chrome"):
    driver = webdriver.Chrome()
  else:
    print("provide valid browser")
  driver.maximize_window()
  driver.get(config_reader.read_configuration("basic info","url"))
  yield driver
  driver.quit()

