# skip - if defects are there
# skip - if the testcases are absolute
# windows , mobile - OS dependency
# browsers - FF , IE , chrome

import pytest
def testcase1():
    print("Testcase1 is executed")

def testcase2():
    print("testcase2 is executed")

@pytest.mark.skip
def testcase3():
    print ("Testcase3 is executed")

def openbrowser():
    print("opening the browser")