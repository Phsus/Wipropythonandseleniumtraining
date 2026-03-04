import pytest

@pytest.mark.usefixtures("sessionsetup")
def test_one():
    print("Testcase1")

def test_two():
    print("testcase2")