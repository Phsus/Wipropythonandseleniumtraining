import pytest

@pytest.mark.usefixtures("openbrowser")
def test_login():
    print("enter the username")
    print("enter the password")
    print("click on the login button")

@pytest.mark.usefixtures("closebrowser")
def test_logout():
    print("User is logged out")