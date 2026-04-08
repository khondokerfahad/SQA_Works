from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 15)

print("=" * 60)
print("Exercise 2.3: Alert Handling")
print("=" * 60 + "\n")

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# ========================================
# PART 1: Simple Alert (OK button only)
# ========================================
print("===== PART 1: Simple Alert (OK button only) =====")

js_alert = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[onclick='jsAlert()']"))).click()

wait.until(EC.alert_is_present())

alert_1 = driver.switch_to.alert

print(f"Alert Message Contain : {alert_1.text}")

time.sleep(2)

alert_1.accept()

result_message = wait.until(EC.visibility_of_element_located((By.ID, "result")))
print(f"Result Message Contain : {result_message.text}")

# ========================================
# TEST 2: Confirmation Alert - Dismiss
# ========================================
print("\n===== TEST 2: Confirmation Alert - Dismiss =====")

js_confirm = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[onclick='jsConfirm()']"))).click()

wait.until(EC.alert_is_present())

alert_2 = driver.switch_to.alert

print(f"Alert Message Contain : {alert_2.text}")

time.sleep(2)

alert_2.dismiss()

result_message = wait.until(EC.visibility_of_element_located((By.ID, "result")))
print(f"Result Message Contain : {result_message.text}")

# ========================================
# TEST 3: Confirmation Alert - Accept
# ========================================
print("\n===== TEST 3: Confirmation Alert - Accept =====")

js_prompt = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[onclick='jsPrompt()']"))).click()

wait.until(EC.alert_is_present())

alert_3 = driver.switch_to.alert

print(f"Alert Message Contain : {alert_3.text}")

time.sleep(2)

alert_3.send_keys("Selenium Automation")
time.sleep(2)
alert_3.accept()

result_message = wait.until(EC.visibility_of_element_located((By.ID, "result")))
print(f"Result Message Contain : {result_message.text}")

driver.quit()