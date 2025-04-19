from time import sleep

from lib import SeleniumWrapper
class Loginpage:
    _lnk_login=("id","login")
    email=("id","email")
    password=("id","password")
    lnk_loginsubmit=("id","loginsubmit")
    def __init__(self,driver):
        self.driver=driver
    def login(self,email,password):
        sw=SeleniumWrapper(self.driver)
        sw.click_element(Loginpage._lnk_login)
        sw.enter_text(Loginpage.email,value=email)
        sw.enter_text(Loginpage.password)
        sw.click_element(Loginpage.lnk_loginsubmit,value=password)
    def is_user_loggedin(self,email):
        _xpath = f"//a[text()='{email}']"
        for _ in range(5):
            try:
                return self.driver.find_element("xpath",_xpath).isdisplayed()
            except Exception:
                sleep(1)
                continue
        return False



