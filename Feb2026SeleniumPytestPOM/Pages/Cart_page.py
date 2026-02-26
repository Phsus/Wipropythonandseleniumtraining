from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_item_name = (By.CLASS_NAME, "inventory_item_name")
        self.checkout_btn = (By.ID, "checkout")

    def verify_item_in_cart(self):
        return self.driver.find_element(*self.cart_item_name).text

    def click_checkout(self):
        self.driver.find_element(*self.checkout_btn).click()