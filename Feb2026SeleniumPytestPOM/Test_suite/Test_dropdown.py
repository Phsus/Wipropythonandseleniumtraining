import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# You MUST import the Select class to handle dropdowns
from selenium.webdriver.support.ui import Select

# Initialize the Firefox driver
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.maximize_window()

# Navigate to the practice website
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

time.sleep(2)

# 1. Locate the dropdown element using its ID
dropdown = driver.find_element(By.ID, "dropdown-class-example")

# 2. Pass the located element into the Select class
sel = Select(dropdown)

# 3. Select by visible text (What the user actually sees on the screen)
sel.select_by_visible_text("Option1")
print("Selected Option1 by visible text")
time.sleep(2)

# 4. Select by value (The 'value' attribute inside the HTML <option> tag)
sel.select_by_value("option2")
print("Selected Option2 by value")
time.sleep(2)

# 5. Select by index (0-based index of the options in the list)
# Index 3 is the 4th item in the list (usually Option3 if the first is 'Select')
sel.select_by_index(3)
print("Selected 4th item by index")
time.sleep(2)

# Close the browser
driver.quit()