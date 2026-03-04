import pytest
@pytest.fixture(params=["chrome","Firefox"])
#request - pytest object that contains information about who is calling and with what data.
def browser(request):
         print("Current browser:", request.param)
         return request.param

def testbrowser(browser):
    assert browser in ["chrome" , "firefox"]
