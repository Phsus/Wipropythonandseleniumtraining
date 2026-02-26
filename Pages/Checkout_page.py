from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.zip_code = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")
        self.finish_btn = (By.ID, "finish")
        self.success_msg = (By.CLASS_NAME, "complete-header")

    def input_info_and_finish(self, fname, lname, zip_code):
        self.driver.find_element(*self.first_name).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.zip_code).send_keys(zip_code)
        self.driver.find_element(*self.continue_btn).click()
        self.driver.find_element(*self.finish_btn).click()

    def get_confirmation(self):
        return self.driver.find_element(*self.success_msg).text