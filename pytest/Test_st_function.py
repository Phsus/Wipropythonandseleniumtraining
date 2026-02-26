# function level set up and tear down
# these run before and after each test function
import pytest


# set up at function level

def setup_function(function):
    print("opening the browser")

def teardown_function(function):
    print("closing the browser")

def testcase1():
    print("Testcase1 is executed")

@pytest.mark.regression
@pytest.mark.sanity
def testcase2():
    print("Testcase2 is executed")

@pytest.mark.regression
def testcase3():
    print("Testcase3 is executed")
