from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_google_search():
    driver = webdriver.Chrome()  # Make sure ChromeDriver is in PATH
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium")
    search_box.submit()
    time.sleep(2)
    assert "Selenium" in driver.page_source
    driver.quit()
