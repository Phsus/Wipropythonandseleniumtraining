import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()


driver.get("https://testautomationpractice.blogspot.com/")


time.sleep(3)


male_radio = driver.find_element(By.ID, "male")
male_radio.click()
print("Selected Gender: Male")



monday_checkbox = driver.find_element(By.ID, "monday")
monday_checkbox.click()
print("Selected Day: Monday")


time.sleep(2)

# Validate that both elements are actually selected
assert male_radio.is_selected() == True, "Male radio button was not selected!"
assert monday_checkbox.is_selected() == True, "Monday checkbox was not checked!"
print("Validation passed: Both elements were successfully selected.")


driver.quit()