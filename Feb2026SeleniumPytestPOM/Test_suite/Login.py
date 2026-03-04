import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Initialize the Firefox driver
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

# Wait for the page elements to load
time.sleep(4)

# Enter username
name = driver.find_element(By.NAME, "username")
name.send_keys("Admin")

# Enter password
password = driver.find_element(By.NAME, "password")
password.send_keys("admin123")

time.sleep(4)

# Click on login button
Login = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
Login.click()

# Validate that the title contains "OrangeHRM"
assert "OrangeHRM" in driver.title
print("Login successful! Title validated.")

# Close the browser
time.sleep(2)
driver.quit()