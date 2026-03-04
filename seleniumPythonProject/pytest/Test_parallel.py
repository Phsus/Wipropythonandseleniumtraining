import pytest
from Test_SimpleFixture import api_url

def testcase1():
    print("Testcase1 is executed")

def testcase2():
    print("testcase2 is executed")

def testcase3():
    print ("Testcase3 is executed")


def testcase4():
    print ("Testcase4 is executed")

def testcase5():
    print ("Testcase5 is executed")

def test_login():
    print ("login test is executed")

def test_api(api_url):
    assert "https" in api_url