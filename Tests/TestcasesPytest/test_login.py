import pytest
import time
from Pages.Login_pages import LoginPage
from utilities.logger import get_logger

# Import from your newly renamed file! (Notice the underscore)
from utilities.Write_Toexcel import get_excel_data

logger = get_logger()

# Loading test data using your absolute path from the Downloads folder
test_data = get_excel_data(r"C:\Users\KIIT01\Downloads\seltest.xlsx", "Sheet1")


class TestLogin:

    # The decorator loops the test for every row in seltest.xlsx
    @pytest.mark.parametrize("username, password", test_data)
    def test_login_excel(self, driver, username, password):
        logger.info(f"Opening application for user: {username}")
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)

        # Create the object of login_page
        lp = LoginPage(driver)

        logger.info(f"Entering credentials - Username: {username}, Password: {password}")
        lp.login(username, password)

        time.sleep(2)

        # Smart assertion checks the password to determine if it should expect success or failure
        if password == "admin123":
            logger.info("Validating successful login")
            assert "OrangeHRM" in driver.title
        else:
            logger.info("Validating invalid credentials error message")
            assert "Invalid credentials" in lp.get_error_message()
