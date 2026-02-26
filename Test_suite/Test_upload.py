from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time


class Test_Upload_Assignment:
    def test_up(self):
       
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


        driver.get("https://the-internet.herokuapp.com/upload")
        driver.maximize_window()
        time.sleep(2)


        browse = driver.find_element(By.XPATH, "//input[@id='file-upload']")


        file_path = r"C:\Users\KIIT01\Downloads\assignment2.docx"
        browse.send_keys(file_path)
        time.sleep(2)


        upload = driver.find_element(By.XPATH, "//input[@id='file-submit']")
        upload.click()
        time.sleep(2)


        fileupload_header = driver.find_element(By.XPATH, "//h3[normalize-space()='File Uploaded!']")
        assert fileupload_header.text == "File Uploaded!"

        print(f"Successfully uploaded: {file_path}")

        time.sleep(2)
        driver.close()


if __name__ == "__main__":
    test = Test_Upload_Assignment()
    test.test_up()