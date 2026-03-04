from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class DemoQAAutomation:

    def setup(self):
        # FIX: Correctly instantiate ChromeOptions
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 15)

    def handle_keyboard(self):
        # Navigating to a site to demonstrate keyboard actions
        self.driver.get("https://www.facebook.com/")
        actions = ActionChains(self.driver)

        # Locating the element and performing the SHIFT + keys action
        email = self.driver.find_element(By.XPATH, "//input[@name = 'email']")

        # move_to_element, key_down(SHIFT), and send_keys are chained
        seriesofactions = actions.move_to_element(email).key_down(Keys.SHIFT).send_keys("hello")
        seriesofactions.perform()

    def teardown(self):
        if hasattr(self, 'driver'):
            self.driver.quit()


if __name__ == "__main__":
    # FIX: Use the same instance for setup and teardown
    bot = DemoQAAutomation()
    try:
        bot.setup()
        bot.handle_keyboard()
    finally:
        bot.teardown()