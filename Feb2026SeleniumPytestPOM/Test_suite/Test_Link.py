from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time
import os

# Set the specified download directory
DOWNLOAD_DIR = r"C:\Users\KIIT01\Downloads"


class Test_download:
    def test_dw(self):
        # 1. Configure Firefox Options for automatic background download
        options = Options()

        # 0: desktop, 1: default download folder, 2: custom folder
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.dir", DOWNLOAD_DIR)

        # Bypass the "Save As" popup for specific file types
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "image/jpeg,application/octet-stream")

        # 2. Initialize Driver with the configured options
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

        try:
            # 3. Navigate to the target URL
            driver.get("https://the-internet.herokuapp.com/download")
            driver.maximize_window()
            time.sleep(2)

            # 4. Locate the specific 'alert.jpeg' link and click to download
            alert = driver.find_element(By.XPATH, "//a[normalize-space()='alert.jpeg']")
            alert.click()

            # 5. Wait for the file to finish downloading
            time.sleep(5)

            # 6. Verify the file actually exists in the local directory
            file_path = os.path.join(DOWNLOAD_DIR, "alert.jpeg")
            if os.path.exists(file_path):
                print(f"Success: alert.jpeg found in {DOWNLOAD_DIR}")
            else:
                print("Error: File not found after download.")

        finally:
            # 7. Close driver session
            time.sleep(2)
            driver.close()


if __name__ == "__main__":
    test = Test_download()
    test.test_dw()