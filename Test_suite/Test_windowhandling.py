from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time


class Test_WindowHandle:
    def test_wh(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


        driver.get("https://the-internet.herokuapp.com/windows")
        driver.maximize_window()
        driver.implicitly_wait(10)


        parent_window = driver.current_window_handle


        clickhere = driver.find_element(By.XPATH, "//a[normalize-space()='Click Here']")
        clickhere.click()



        windows = driver.window_handles
        print(f"All Window Handles: {windows}")



        driver.switch_to.window(windows[1])


        child_text_element = driver.find_element(By.XPATH, "//h3[contains(text(),'New Window')]")
        print(f"Text in Child Window: {child_text_element.text}")


        driver.close()

        # 7. Return focus back to parent window
        driver.switch_to.window(parent_window)
        print(f"Returned to Parent Window: {driver.title}")

        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    test = Test_WindowHandle()
    test.test_wh()