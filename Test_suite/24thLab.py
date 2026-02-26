from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 10)

try:

    driver.get("https://demowebshop.tricentis.com/register")
    print(f"Navigated to: {driver.title}")


    driver.find_element(By.ID, "gender-male").click()
    driver.find_element(By.ID, "FirstName").send_keys("Sushant")
    driver.find_element(By.ID, "LastName").send_keys("choudhary")

    # Use a unique email to avoid "Email already exists" errors
    unique_email = f"Sush{int(time.time())}@example.com"
    driver.find_element(By.ID, "Email").send_keys(unique_email)

    driver.find_element(By.ID, "Password").send_keys("Password123")
    driver.find_element(By.ID, "ConfirmPassword").send_keys("Password123")

    # Submit Registration
    driver.find_element(By.ID, "register-button").click()

    # Validate Registration Success
    result = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
    print(f"Registration Status: {result.text}")

    # --- STEP 2: LOGIN ---
    # Navigate to Login page
    driver.get("https://demowebshop.tricentis.com/login")

    driver.find_element(By.ID, "Email").send_keys(unique_email)
    driver.find_element(By.ID, "Password").send_keys("Password123")

    # Click Login
    driver.find_element(By.CLASS_NAME, "login-button").click()

    # Verify Login by checking the presence of the logout link
    logout_link = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ico-logout")))
    print("Login successful: Logout link is visible.")

finally:
    time.sleep(3)
    driver.quit()