import pytest

# Fixture for numbers
@pytest.fixture(params=[2, 4, 6, 8, 1, 3, 5, 7])
def num_data(request):
    
    return request.param

# Test case using the fixture
def test_even_odd(num_data):
    if num_data % 2 == 0:
        print(f"\nTesting Even: {num_data}")
        assert num_data % 2 == 0
    else:
        print(f"\nTesting Odd: {num_data}")
        assert num_data % 2 != 0