import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# 1. Configure Chrome Options
chrome_options = Options()


chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")

# Disable the Password Manager AND the specific Leak Detection feature
prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False,  
    "safebrowsing.enabled": False
}
chrome_options.add_experimental_option("prefs", prefs)

# Optional: Hides the "Chrome is being controlled by automated test software" info bar
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

# 2. Initialize Driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.maximize_window()
driver.implicitly_wait(10)

try:
    # 3. Navigate to SauceDemo
    driver.get("https://www.saucedemo.com/")
    time.sleep(1)

    # 4. Login
    print("Logging in...")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 5. Add Product to Cart
    print("Adding product to cart...")
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(1)

    # 6. Go to Cart
    print("Navigating to cart...")
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(1)

    # 7. Checkout
    print("Starting checkout process...")
    driver.find_element(By.ID, "checkout").click()
    time.sleep(1)

    # 8. Add Details
    print("Entering shipping details...")
    driver.find_element(By.ID, "first-name").send_keys("Sushant")
    driver.find_element(By.ID, "last-name").send_keys("QA")
    driver.find_element(By.ID, "postal-code").send_keys("110001")
    driver.find_element(By.ID, "continue").click()
    time.sleep(1)

    # 9. Finish Checkout
    print("Confirming order...")
    driver.find_element(By.ID, "finish").click()
    time.sleep(1)

    # 10. Validate Success Message
    success_message = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert success_message == "Thank you for your order!"
    print(f"Validation Passed: Found message '{success_message}'")

    # 11. Back Home
    print("Returning to inventory page...")
    driver.find_element(By.ID, "back-to-products").click()
    time.sleep(2)

    print("--- End-to-End Test Completed Successfully! ---")

finally:
    # 12. Teardown
    driver.quit()