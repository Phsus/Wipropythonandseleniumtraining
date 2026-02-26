import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(2)

simple_button = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']")
simple_button.click()
time.sleep(1)
simple_alert = driver.switch_to.alert
print("Simple Alert Text:", simple_alert.text)
simple_alert.accept()

time.sleep(2)

confirm_button = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']")
confirm_button.click()
time.sleep(1)
confirm_alert = driver.switch_to.alert
print("Confirm Alert Text:", confirm_alert.text)
confirm_alert.dismiss()

time.sleep(2)

prompt_button = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']")
prompt_button.click()
time.sleep(1)
prompt_alert = driver.switch_to.alert
print("Prompt Alert Text:", prompt_alert.text)
prompt_alert.send_keys("Hello from Selenium")
prompt_alert.accept()

time.sleep(2)
driver.quit()