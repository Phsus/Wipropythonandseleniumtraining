import pytest

# This mark applies the 'class_setup' fixture to every test inside
@pytest.mark.usefixtures("class_setup")
class TestFixturesClass:

    # IMPORTANT: 'self' is required for methods inside a class
    def test_login(self):
        print("Executing: Step 1 - Login")
        assert True

    def test_search(self):
        print("Executing: Step 2 - Search")
        assert True

    def test_payment(self):
        print("Executing: Step 3 - Payment")
        assert True

    # Using a data fixture from conftest
    def test_data_validation(self, simple_data):
        print(f"Executing: Step 4 - Data value is {simple_data}")
        assert simple_data == 45

    # Using a parameterized fixture
    def test_browser_check(self, browser):
        print(f"Executing: Step 5 - Checking on {browser}")
        assert browser in ["chrome", "firefox"]