from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time
import os


DOWNLOAD_DIR = r"C:\Users\KIIT01\Downloads"


class Test_Download:
    def test_dw(self):
       
        options = Options()
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.dir", DOWNLOAD_DIR)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "image/jpeg,application/octet-stream")

        # 2. Initialize Driver with options
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

        # 3. Navigate to the download page
        driver.get("https://the-internet.herokuapp.com/download")
        driver.maximize_window()
        time.sleep(2)

        # 4. Locate the specific file link and click to download
        alert = driver.find_element(By.XPATH, "//a[normalize-space()='alert.jpeg']")
        alert.click()


        time.sleep(5)

        # 6. Verify file exists in the directory
        file_path = os.path.join(DOWNLOAD_DIR, "alert.jpeg")
        assert os.path.exists(file_path)
        print(f"Success: alert.jpeg downloaded to {DOWNLOAD_DIR}")

        time.sleep(2)
        driver.close()


if __name__ == "__main__":
    test = Test_Download()
    test.test_dw()