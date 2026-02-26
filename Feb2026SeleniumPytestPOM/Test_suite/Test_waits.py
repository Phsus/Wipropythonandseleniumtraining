from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time

class Test_waits:
    def test_waits(self):
        # Initialize Driver
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.get("https://www.facebook.com/")
        driver.maximize_window()

        # 1. Implicit Wait: A global setting for the entire session
        # Tells the driver to wait for a maximum of 2 seconds for every element location call
        driver.implicitly_wait(2)

        # 2. Explicit Wait: Targeted wait for a specific element condition
        radio_btn = driver.find_element(By.XPATH, "(//input[@value='radio2'])[1]")
        wait = WebDriverWait(driver, timeout=2)
        # Wait until the radio button is visible in the UI
        wait.until(lambda _: radio_btn.is_displayed())

        # 3. Custom/Fluent Wait: Flexible wait with custom polling and error ignoring
        errors = [NoSuchElementException, ElementNotInteractableException]
        # Checks for the condition every 0.2 seconds and ignores specified exceptions
        wait = WebDriverWait(driver, timeout=2, poll_frequency=0.2, ignored_exceptions=errors)
        wait.until(lambda _: radio_btn.send_keys("Displayed") or True)

        # Close the session
        driver.close()

if __name__ == "__main__":
    test = Test_waits()
    test.test_waits()