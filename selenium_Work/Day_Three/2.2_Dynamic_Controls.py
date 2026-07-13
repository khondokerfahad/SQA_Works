from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 15)

print("=" * 60)
print("Exercise 2.2: Dynamic Controls")
print("=" * 60 + "\n")

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

# ========================================
# PART 1: Remove Checkbox
# ========================================
print("=== PART 1: Remove Checkbox ===")

# Click Remove button - FIXED: Using text-based XPath
remove_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Remove']")))
remove_button.click()
print("✓ Clicked Remove button")

# Wait for loading to appear
wait.until(EC.visibility_of_element_located((By.ID, "loading")))
print("✓ Loading started")

# Wait for loading to disappear
wait.until(EC.invisibility_of_element_located((By.ID, "loading")))
print("✓ Loading finished")

# Get message
message = wait.until(EC.visibility_of_element_located((By.ID, "message")))
print("✓ Message appeared")

# NEW: Verify message text
wait.until(EC.text_to_be_present_in_element((By.ID, "message"), "It's gone!"))
print("✓ Verified message text")

# NEW: Verify checkbox is no longer visible
wait.until(EC.invisibility_of_element_located((By.ID, "checkbox")))
print("✓ Checkbox is no longer visible")

print(f"Message: {message.text}\n")

# ========================================
# PART 2: Add Checkbox
# ========================================
print("=== PART 2: Add Checkbox ===")

# Click Add button - FIXED: Using text-based XPath
add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add']")))
add_button.click()
print("✓ Clicked Add button")

# Wait for loading to appear
wait.until(EC.visibility_of_element_located((By.ID, "loading")))
print("✓ Loading started")

# Wait for loading to disappear
wait.until(EC.invisibility_of_element_located((By.ID, "loading")))
print("✓ Loading finished")

# Get message
message = wait.until(EC.visibility_of_element_located((By.ID, "message")))
print("✓ Message appeared")

# NEW: Verify message text
wait.until(EC.text_to_be_present_in_element((By.ID, "message"), "It's back!"))
print("✓ Verified message text")

# NEW: Verify checkbox is visible again
checkbox = wait.until(EC.visibility_of_element_located((By.ID, "checkbox")))
print("✓ Checkbox is visible again")

print(f"Message: {message.text}\n")

# ========================================
# PART 3: Enable Input Field
# ========================================
print("=== PART 3: Enable Input Field ===")

# Click Enable button - Already good!
enable_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[onclick='swapInput()']")))
enable_button.click()
print("✓ Clicked Enable button")
print("✓ Loading started")

# Get message
message = wait.until(EC.visibility_of_element_located((By.ID, "message")))
print("✓ Message appeared")

# NEW: Verify message text (FIXED TYPO!)
wait.until(EC.text_to_be_present_in_element((By.ID, "message"), "It's enabled!"))
print("✓ Verified message text")

# NEW: Wait for input to be enabled and type in it
input_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']")))
print("✓ Input field is now enabled")

input_field.send_keys("Now I'm enabled!")
print("✓ Typed in input field")

# NEW: Verify text was entered
entered_text = input_field.get_attribute("value")
assert entered_text == "Now I'm enabled!", f"Expected 'Now I'm enabled!' but got '{entered_text}'"
print(f"✓ Verified entered text: '{entered_text}'")

print(f"Message: {message.text}\n")

# ========================================
# BONUS PART 4: Disable Input Field
# ========================================
print("\n======= PART 4: Disable Input Field =======")

# Click Disable button
disable_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Disable']")))
disable_button.click()
print("✓ Clicked Disable button")

# Get message
message = wait.until(EC.visibility_of_element_located((By.ID, "message")))
print("✓ Message appeared")

# Verify message text
wait.until(EC.text_to_be_present_in_element((By.ID, "message"), "It's disabled!"))
print("✓ Verified message text")

# Verify input is disabled
input_field = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
is_disabled = input_field.get_attribute("disabled")
assert is_disabled == "true", "Input should be disabled"
print("✓ Input field is now disabled")

print(f"Message: {message.text}\n")

print("=" * 60)
print("✓ Exercise 2.2 Completed Successfully!")
print("=" * 60)

driver.quit()