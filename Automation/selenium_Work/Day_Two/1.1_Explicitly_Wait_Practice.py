from selenium import webdriver # type: ignore
from selenium.webdriver.chrome.service import Service   # type: ignore
from webdriver_manager.chrome import ChromeDriverManager    # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
import time

# Installing Chrome Driver 
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

# Initializing wait
wait = WebDriverWait(driver, 10)

driver.get("https://practicetestautomation.com/practice-test-login/")

user_name = wait.until(EC.element_to_be_clickable((By.ID, "username"))).send_keys("student")

driver.implicitly_wait(5)

password = wait.until(EC.element_to_be_clickable((By.ID, "password")))
password.send_keys("Password123")

driver.implicitly_wait(5)

submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
submit_button.click()

driver.implicitly_wait(5)

show_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".post-title")))
print(f"Text displayed: {show_text.text}")

driver.implicitly_wait(5)

logout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Log out")))
logout_button.click()

driver.implicitly_wait(5)

driver.quit()

