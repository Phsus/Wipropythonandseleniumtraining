from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize driver
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()


wait = WebDriverWait(driver, 20)

try:

    email_field = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
    pass_field = driver.find_element(By.NAME, "pass")

    actions = ActionChains(driver)


    actions.move_to_element(email_field).click().send_keys("hello").perform()


    actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()


    actions.move_to_element(pass_field).click().key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

    print("Success: 'hello' was copied and pasted successfully.")

except Exception as e:

    print(f"Detailed Error: {e}")

finally:
    time.sleep(5)  
    driver.quit()