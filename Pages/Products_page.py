from selenium.webdriver.common.by import By

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_item_and_go_to_cart(self):
        self.driver.find_element(*self.add_backpack).click()
        self.driver.find_element(*self.cart_icon).click()