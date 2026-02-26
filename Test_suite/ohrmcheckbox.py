import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 1. Initialize Driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Use Explicit Wait for dynamic loading
wait = WebDriverWait(driver, 15)

try:
    # 2. Login to OrangeHRM
    driver.get("https://opensource-demo.orangehrmlive.com/")

    # Wait for username field, then login
    wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print("Logged in successfully.")

    # 3. Navigate to PIM Module

    pim_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']")))
    pim_menu.click()
    print("Navigated to PIM module.")



    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-table-body")))
    time.sleep(2)



    checkboxes = driver.find_elements(By.XPATH,
                                      "//div[@class='oxd-table-body']//span[contains(@class, 'oxd-checkbox-input')]")

    print(f"Found {len(checkboxes)} employee records on the current page.")

    # 6. Scroll and click one by one
    for index, checkbox in enumerate(checkboxes, start=1):

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)


        time.sleep(0.5)


        driver.execute_script("arguments[0].click();", checkbox)
        print(f"Clicked employee checkbox {index}")

    print("Successfully clicked all individual checkboxes!")
    time.sleep(3)

finally:
    # 7. Teardown
    driver.quit()