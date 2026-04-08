from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Step 1: Navigate to login page
driver.get("https://practicetestautomation.com/practice-test-login/")

user_name = driver.find_element(By.ID, "username")
user_name.send_keys("student")

time.sleep(2)

password = driver.find_element(By.ID, "password")
password.send_keys("Password123")

time.sleep(2)

submit_button = driver.find_element(By.ID, "submit")
submit_button.click()

time.sleep(2)

success_message = driver.find_element(By.CSS_SELECTOR, ".post-title")
print(success_message.text)

time.sleep(2)

logout_button = driver.find_element(By.XPATH, "/html/body/div/div/section/div/div/article/div[2]/div/div/div/a")
logout_button.click()

time.sleep(2)



driver.quit()