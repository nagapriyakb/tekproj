from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located


def wait_for_element(func):
    def wrapper(*args,**kwargs):
        instance=args[0]
        locator=args[1]
        wait=WebDriverWait(instance.driver,10)
        v=visibility_of_element_located(locator)
        wait.until(v)
        func(*args,**kwargs)
    return wrapper
class SeleniumWrapper:
    _lnk=("id","Login")
    _email=()
    def __init__(self,driver):
        self.driver=driver
    @wait_for_element
    def enter_text(self,locator,/,*,value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)
    @wait_for_element
    def click_element(self,locator):
        self.driver.find_element(locator).click()
    


