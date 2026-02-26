import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()


driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)


checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(f"Found {len(checkboxes)} checkboxes on the page.")


for checkbox in checkboxes:

    if not checkbox.is_selected():
        checkbox.click()

print("Clicked all checkboxes.")

time.sleep(2)


for index, checkbox in enumerate(checkboxes, start=1):
    assert checkbox.is_selected() == True, f"Checkbox {index} was not selected!"

print("Validation passed: All checkboxes are successfully selected.")


driver.quit()