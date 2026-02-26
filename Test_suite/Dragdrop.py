from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class DemoQAAutomation:

    def setup(self):
        """Initializes the Chrome WebDriver with optimized settings."""
        # Correctly instantiating ChromeOptions
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        # Ensure driver is initialized for this instance
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 15)
        print("Setup: Browser launched and maximized.")

    def open_site(self):
        """Navigates to the DemoQA homepage and validates page load."""
        self.driver.get("https://demoqa.com/")
        # Explicit wait to ensure site is ready
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "home-banner")))
        print("Open Site: Navigated to DemoQA successfully.")

    def handle_frame(self):
        """Switches context to an iframe and validates internal text."""
        self.driver.get("https://demoqa.com/frames")
        # Switch context to the targeted frame
        self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1")))

        frame_text = self.driver.find_element(By.ID, "sampleHeading").text
        print(f"Handle Frame: Found text '{frame_text}' inside iframe.")

        # Always switch back to the main document context
        self.driver.switch_to.default_content()

    def handle_windows(self):
        """Handles multiple browser tabs/windows and switches back to parent."""
        self.driver.get("https://demoqa.com/browser-windows")
        parent_handle = self.driver.current_window_handle

        self.driver.find_element(By.ID, "tabButton").click()
        self.wait.until(EC.number_of_windows_to_be(2))

        # Iterating through handles using the correct parent variable
        for handle in self.driver.window_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                break

        child_text = self.driver.find_element(By.ID, "sampleHeading").text
        print(f"Handle Windows: Child tab text validated as '{child_text}'.")

        self.driver.close()
        # Switching context back to ensure further steps work
        self.driver.switch_to.window(parent_handle)

    def handle_alert(self):
        """Triggers a JS alert and performs the accept action."""
        self.driver.get("https://demoqa.com/alerts")
        self.driver.find_element(By.ID, "alertButton").click()

        # Wait for the JS alert to appear
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        print(f"Handle Alert: Alert text reads '{alert.text}'.")
        alert.accept()

    def handle_elements(self):
        """Demonstrates interaction with Text Box and Checkbox."""
        # Text Box workflow
        self.driver.get("https://demoqa.com/text-box")
        self.driver.find_element(By.ID, "userName").send_keys("John Doe")

        # Using JS scroll to ensure elements are viewable before interaction
        submit_btn = self.driver.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
        submit_btn.click()

        # Checkbox workflow
        self.driver.get("https://demoqa.com/checkbox")
        self.driver.find_element(By.CLASS_NAME, "rct-checkbox").click()
        print("Handle Elements: Completed text entry and checkbox selection.")

    def teardown(self):
        """Safely terminates the browser session."""
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()
            print("Teardown: Browser resources released.")


# Main flow execution using a single consistent instance
if __name__ == "__main__":
    bot = DemoQAAutomation()
    try:
        bot.setup()
        bot.open_site()
        bot.handle_frame()
        bot.handle_windows()
        bot.handle_alert()
        bot.handle_elements()
    except Exception as e:
        print(f"Execution Error: {e}")
    finally:
        # Closing the instance that performed setup
        bot.teardown()