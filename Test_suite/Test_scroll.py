from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class DemoQAAutomation:

    def setup(self):
        """Initialize Chrome WebDriver and basic configuration."""
        # FIX: Correctly instantiate options
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 15)
        print("Setup: Browser launched and maximized.")

    def open_site(self):
        """Navigate to the DemoQA homepage and validate load."""
        self.driver.get("https://demoqa.com/")
        # Validate page load using explicit wait
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "home-banner")))
        print("Open Site: Navigated to DemoQA successfully.")

    def handle_frame(self):
        """Navigate to Frames and interact with iframe content."""
        self.driver.get("https://demoqa.com/frames")
        # Switch context to iframe
        self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1")))

        frame_text = self.driver.find_element(By.ID, "sampleHeading").text
        print(f"Handle Frame: Content is '{frame_text}'.")

        self.driver.switch_to.default_content()
        print("Handle Frame: Switched back to main content.")

    def handle_windows(self):
        """Handle multiple browser tabs and windows."""
        self.driver.get("https://demoqa.com/browser-windows")
        parent_handle = self.driver.current_window_handle

        self.driver.find_element(By.ID, "tabButton").click()
        self.wait.until(EC.number_of_windows_to_be(2))

        # FIX: Correct variable name for handle matching
        for handle in self.driver.window_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                break

        child_text = self.driver.find_element(By.ID, "sampleHeading").text
        print(f"Handle Windows: New tab text is '{child_text}'.")

        self.driver.close()
        self.driver.switch_to.window(parent_handle)

    def handle_alert(self):
        """Trigger and accept a JavaScript alert."""
        self.driver.get("https://demoqa.com/alerts")
        self.driver.find_element(By.ID, "alertButton").click()

        # Wait for alert presence
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        print(f"Handle Alert: Alert text is '{alert.text}'.")
        alert.accept()

    def handle_elements(self):
        """Interact with Text Boxes and Checkboxes."""
        # Text Box Interaction
        self.driver.get("https://demoqa.com/text-box")
        self.driver.find_element(By.ID, "userName").send_keys("John Doe")

        # JavaScript Scroll to ensure element is clickable
        submit_btn = self.driver.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
        submit_btn.click()

        # Checkbox Interaction
        self.driver.get("https://demoqa.com/checkbox")
        self.driver.find_element(By.CLASS_NAME, "rct-checkbox").click()
        print("Handle Elements: Interacted with text box and checkbox.")

    def teardown(self):
        """Close browser and release resources."""
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()
            print("Teardown: Resources released.")


# FIX: Ensure main block uses the single instance consistently
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
        print(f"An error occurred: {e}")
    finally:
        # Proper cleanup
        bot.teardown()