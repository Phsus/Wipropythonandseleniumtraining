import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Initialize the Firefox driver
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.maximize_window()

# Navigate to Rahul Shetty Automation Practice Page
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# Wait for the page elements to load
time.sleep(3)

# Locate the Radio1 button using its 'value' attribute
radio_button_1 = driver.find_element(By.XPATH, "//input[@value='radio1']")

# Click the radio button
radio_button_1.click()
print("Clicked on Radio1.")

time.sleep(2) # Brief pause so you can visually see it clicked

# Validate that the radio button is actually selected
assert radio_button_1.is_selected() == True
print("Validation passed: Radio1 is successfully selected.")

# Close the browser
driver.quit()