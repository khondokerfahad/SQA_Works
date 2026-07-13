from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 15)

start_time = time.time()

# TODO: Complete this exercise
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

start_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='start'] button")))
start_button.click()
print(f"Start button clicked at: {time.time() - start_time:.2f} seconds")

# wait.until(EC.invisibility_of_element_located((By.ID, "loading")))
# print(f"Loading element is invisible at: {time.time() - start_time:.2f} seconds")

wait.until(EC.visibility_of_element_located((By.ID, "loading")))
print(f"Loading element is visible at: {time.time() - start_time:.2f} seconds")

wait.until(EC.invisibility_of_element_located((By.ID, "loading")))
print(f"Loading element is invisible at: {time.time() - start_time:.2f} seconds")

result = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='finish'] h4")))
print(f"Result : {result.text} - element is visible at: {time.time() - start_time:.2f} seconds")

driver.quit()