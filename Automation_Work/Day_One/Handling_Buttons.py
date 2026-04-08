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

time.sleep(2)

user_name = driver.find_element(By.ID, "user-name")
user_name.send_keys("standard_user")

password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

time.sleep(2)

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

time.sleep(2)

# alert = driver.switch_to.alert
# print(f"Alert Text : {alert}")
# alert.accept()

# time.sleep(2)

bike_light_add_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
bike_light_add_cart.click()

time.sleep(5)

driver.quit()