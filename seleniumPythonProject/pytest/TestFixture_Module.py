#scope = module , runs per file(module)

import pytest
@pytest.mark.usefixtures("setupapi")
def test_one():
    print("Testcas1")

def test_two():
    print("Testcase2")