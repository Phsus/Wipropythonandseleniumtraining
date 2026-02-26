from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time


class Test_WebTable:
    def test_table_data(self):
        # Initialize the Firefox Driver
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        # Navigate to the target URL
        driver.get("https://the-internet.herokuapp.com/tables")
        driver.maximize_window()
        time.sleep(2)

        # 1. Fetch and print all rows in 'table1'
        print("--- Rows Data ---")
        rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr")
        for i in rows:
            print(i.text)

        time.sleep(2)

        # 2. Fetch and print all columns from the first row
        print("\n--- Columns in First Row ---")
        cols = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr[1]/td")
        for i in cols:
            print(i.text)

        time.sleep(2)

        # 3. Fetch and validate specific cell data
        # Targeting Row 3, Column 4
        celldata = driver.find_element(By.XPATH, "//table[@id='table1']/tbody/tr[3]/td[4]")
        print(f"\nFetched Cell Data: {celldata.text}")

        # Assert the expected value is present in the cell text
        assert "$100.00" in celldata.text

        # Close the browser session
        driver.quit()


if __name__ == "__main__":
    test = Test_WebTable()
    test.test_table_data()