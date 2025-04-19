from selenium import webdriver
from pytest import fixture
@fixture
def setup_teardown():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com")
    yield driver
    driver.quit()
