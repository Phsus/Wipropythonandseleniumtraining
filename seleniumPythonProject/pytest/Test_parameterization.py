#parameterization testing multiple set of test data with the same function
#@pytest.mark.parameterize()

import pytest

@pytest.mark.parametrize("a , b , result" ,[
    (2 ,  3 , 5),
    (4 , 5 , 9),
    (10 , 2, 12)
])

def test_add(a,b,result):
    assert a + b == result

@pytest.mark.parametrize("number", [1,2,3,4,5])
def test_even(number):
    assert number%2 == 0

@pytest.mark.parametrize("payload",[
    {"name": "John" , "age": 25},
    {"name" : "Alice" , "age": 17}
])

def test_create_user(payload):
    assert payload["age"] > 18