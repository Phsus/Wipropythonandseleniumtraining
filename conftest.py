import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="class")
def setup(request):
    service = Service(ChromeDriverManager().install())
    # driver instance is created to use web driver globally in the test script
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://opensource-demo.orangehrmlive.com/")

    # FIX: Changed 'clas' to 'cls'
    request.cls.driver = driver
    yield
    driver.quit()