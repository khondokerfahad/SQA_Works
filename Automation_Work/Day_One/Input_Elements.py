from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By         #for select which 
import time

#blocking popupd
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

#chrome driver setup
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_options)

driver.get("https://www.saucedemo.com")

username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")
# time.sleep(5)
username.clear()
username.send_keys("problem_user")

password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# alert = driver.switch_to.alert
# # print("Alert Text : ", alert.text)
# alert.accept()

time.sleep(2)

add_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
print("Button enabled?", add_cart.is_enabled())
add_cart.click()
time.sleep(10)

driver.quit()
