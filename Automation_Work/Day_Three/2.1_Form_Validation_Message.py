from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 15)

print("========= TEST 1: Invalid Username =========")

driver.get("https://practicetestautomation.com/practice-test-login/")

user_name = wait.until(EC.presence_of_element_located((By.ID, "username")))
user_name.send_keys("incorrectUser")

password = wait.until(EC.presence_of_element_located((By.ID, "password")))
password.send_keys("Password123")

wait.until(EC.presence_of_element_located((By.ID, "submit"))).click()

wait.until(EC.invisibility_of_element((By.ID, "error")))

error_message = wait.until(EC.visibility_of_element_located((By.ID, "error")))
print(f"Error Message Contain : {error_message.text}")

driver.implicitly_wait(10)
# driver.close()

print("========= TEST 2: Invalid Password =========")

# driver.get("https://practicetestautomation.com/practice-test-login/")

user_name_2 = wait.until(EC.presence_of_element_located((By.ID, "username")))
user_name_2.send_keys("student")

password_2 = wait.until(EC.presence_of_element_located((By.ID, "password")))
password_2.send_keys("incorrectPassword")

wait.until(EC.presence_of_element_located((By.ID, "submit"))).click()

# wait.until(EC.invisibility_of_element((By.ID, "error")))

error_message_2 = wait.until(EC.visibility_of_element_located((By.ID, "error")))
print(f"Error Message Contain : {error_message_2.text}")

driver.implicitly_wait(10)

print("========= TEST 3: Valid Credentials =========")

user_name_3 = wait.until(EC.presence_of_element_located((By.ID, "username")))
user_name_3.send_keys("student")

password_3 = wait.until(EC.presence_of_element_located((By.ID, "password")))
password_3.send_keys("Password123")

wait.until(EC.presence_of_element_located((By.ID, "submit"))).click()

success_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "post-title")))
print(f"Success Message : {success_message.text}")


driver.quit()

