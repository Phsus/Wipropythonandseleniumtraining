# basic assertion
from operator import truediv


# hard assertion  - this will stop the execution of the test case / test suite
#soft assertion will continue to run even if the assertion fails

import pytest_check as check


# basic assertion
def test_add():
    result = 2 + 3
    assert result == 5


# checking true or false
def test_boolean():
    assert True
    assert not False

# none value
def test_none():
    value = None
    assert value is None

# list assertion
def test_list():
    fruits = ["apple","banana", "oranges"]
    assert "banana" in fruits


#Dict assertion
def test_dict():
    creds = {"username" : "admin" ,"password": "admin123"}
    assert creds["password"] == 'admin123'


#comparing list
def test_comparelist():
    assert [1,2,3] == [1,2,3]


def test_customsg():
    result = 10
    assert result == 10 , "Result should be 5"


#soft assertion
def test_multiple():
    check.equal(1,5)
    check.equal(3,3)
