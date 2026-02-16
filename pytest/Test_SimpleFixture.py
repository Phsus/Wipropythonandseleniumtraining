import pytest
@pytest.fixture
def simple_data():
    return 45

def testcase1(simple_data):
    assert simple_data == 45


@pytest.fixture
def api_url():
    return "https://api.example.com"

def test_api(api_url):
    assert "https" in api_url
