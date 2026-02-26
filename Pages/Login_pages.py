from selenium.webdriver.common.by import By

class LoginPage:
    # Locators
    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    login_button = (By.XPATH, "//button[normalize-space()='Login']")
    # Ensure this locator is here for the invalid credentials test
    error_msg = (By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]")

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        """Unpacks tuples using * for element location"""
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        """Returns error text for validation assertions"""
        return self.driver.find_element(*self.error_msg).text