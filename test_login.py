from pytest import mark
from loginpage import Loginpage
headers="email,password"
# data=data
data=[
    ("hello.world@company.com", "Password123"),
    ("steve.jobs@company.com", "Password123"),

]
@mark.parametrize(headers,data)
def test_login_positive(setupteardown,email,password):
    loginobj=Loginpage(setupteardown)
    loginobj.login(email,password)
    assert True==loginobj.is_user_loggedin(email)
