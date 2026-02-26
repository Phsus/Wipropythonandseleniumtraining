import pytest

@pytest.mark.usefixtures("setup")
class TestLogin:
    

    def test_title(self):
        print(self.driver.title)
        assert "OrangeHRM" in self.driver.title

    def test_valid_login(self):


    def test_invalid_login(self):

