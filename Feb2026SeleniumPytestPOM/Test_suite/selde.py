import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://trytestingthis.netlify.app/")
time.sleep(2)

single_dropdown = driver.find_element(By.ID, "option")
single_select = Select(single_dropdown)

single_select.select_by_visible_text("Option 2")
print("Selected Option 2 from single dropdown")
time.sleep(2)

multi_dropdown = driver.find_element(By.ID, "owc")
multi_select = Select(multi_dropdown)

if multi_select.is_multiple:
    multi_select.select_by_value("option 2")
    multi_select.select_by_visible_text("Option 3")
    print("Selected Option 2 and Option 3 from multi dropdown")
    time.sleep(3)

    multi_select.deselect_all()
    print("Deselected all options")
    time.sleep(2)

driver.quit()