import pytest
import time
import os

from Pages.Login_page import LoginPage
from Pages.Products_page import ProductsPage
from Pages.Cart_page import CartPage
from Pages.Checkout_page import CheckoutPage
from utilities.logger import get_logger
from utilities.Write_Toexcel import get_excel_data

logger = get_logger()

current_dir = os.path.dirname(__file__)
project_root = os.path.dirname(os.path.dirname(current_dir))

excel_path = os.path.join(project_root, "testdata", "secret_sauce.xlsx")
test_data = get_excel_data(excel_path, "Sheet1")


class TestSauceDemo:

    @pytest.mark.parametrize("username, password", test_data)
    def test_sauce_flow(self, driver, username, password):
        user_clean = str(username).strip().lower()

        logger.info(f" Running Test for User: {user_clean} ")
        driver.get("https://www.saucedemo.com/")

        lp = LoginPage(driver)
        lp.login(username, password)
        time.sleep(2)


        if user_clean == "standard_user":
            logger.info("Proceeding with full purchase flow")

            pp = ProductsPage(driver)
            pp.add_item_and_go_to_cart()

            cp_cart = CartPage(driver)
            cp_cart.click_checkout()

            cp_check = CheckoutPage(driver)
            cp_check.input_info_and_finish("Sushant", "kkk", "12345")

            assert "Thank you" in cp_check.get_confirmation()
            logger.info("End-to-End Test Passed!")


        elif user_clean == "locked_out_user":
            logger.info("Checking locked out user gets an error")
            assert "Epic sadface" in driver.page_source


        elif user_clean == "problem_user":
            logger.info("Checking problem user reached inventory but has issues")
            assert "inventory" in driver.current_url

        logger.info(f" Test Finished for {user_clean} ")