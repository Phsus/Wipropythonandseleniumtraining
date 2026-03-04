import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Implicit wait
driver.implicitly_wait(10)

# 1. Navigate to the GreenKart practice site
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
time.sleep(2)

# 2. Add the first product (Brocolli) to the cart
driver.find_elements(By.XPATH, "//div[@class='product-action']/button")[0].click()
print("Added first item to cart.")
time.sleep(1)

# 3. Click the Cart bag icon
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
print("Clicked on Cart icon.")
time.sleep(1)

# 4. Click Proceed to Checkout
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
print("Proceeding to checkout.")
time.sleep(2)

# 5. Click Place Order on the Cart page
driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
print("Clicked Place Order.")
time.sleep(2)

# 6. Select Country as India from the dropdown
country_dropdown = driver.find_element(By.TAG_NAME, "select")
select = Select(country_dropdown)
select.select_by_visible_text("India")
print("Selected Country: India.")
time.sleep(1)

# 7. Check the 'Agree to Terms & Conditions'
driver.find_element(By.CLASS_NAME, "chkAgree").click()
print("Agreed to terms and conditions.")
time.sleep(1)

# 8. Click Final Proceed Button
driver.find_element(By.XPATH, "//button[text()='Proceed']").click()
print("Clicked Proceed to finish the order. End-to-End Test Passed!")
time.sleep(3)

# Close the browser
driver.quit()