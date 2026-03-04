from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time


class Test_frame:
    def test_frame(self):
        # Initialize Firefox Driver
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        # Navigate to the JQuery UI Datepicker page
        driver.get("https://jqueryui.com/datepicker/")
        driver.maximize_window()
        time.sleep(2)

        # Set implicit wait for element stability
        driver.implicitly_wait(10)

        # 1. Switch to the frame using its index or element
        # In this specific page, the demo is the first iframe (index 0)
        driver.switch_to.frame(0)

        # 2. Locate and click the date picker input inside the frame
        datepicker = driver.find_element(By.XPATH, "//input[@id='datepicker']")
        datepicker.click()
        print("Successfully clicked the datepicker inside the iframe.")

        # 3. Optional: Switch back to the main content
        # Use this if you need to interact with elements outside the frame
        driver.switch_to.default_content()

        time.sleep(2)
        driver.close()


if __name__ == "__main__":
    test = Test_frame()
    test.test_frame()