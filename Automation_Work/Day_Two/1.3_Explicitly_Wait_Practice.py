from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 15)

# TODO: Complete this exercise
driver.get("https://www.saucedemo.com/")

# Login
username_field = wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
password_field = wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
login_button.click()

# Wait for products page

wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_img")))


# Get all products

inventory_items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name")))

# Print product names

for items in inventory_items:
    print(f"Product name: {items.text}")

# Click first add to cart

add_cart = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
add_cart.click()
driver.implicitly_wait(5)

# Verify cart badge
cart_badge = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
print(f"Cart badge value: {cart_badge.text}")

cart = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_link")))
cart.click()
driver.implicitly_wait(5)

# burger_menu_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "react-burger-menu-btn")))
# burger_menu_button.click()

# logout_button = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
# logout_button.click()

driver.implicitly_wait(5)


driver.quit()