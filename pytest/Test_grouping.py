import pytest

def testcase1():
    print("Testcase1 is executed")
@pytest.mark.sanity
def testcase2():
    print("testcase2 is executed")
@pytest.mark.regression
def testcase3():
    print ("Testcase3 is executed")

def openbrowser():
    print("opening the browser")