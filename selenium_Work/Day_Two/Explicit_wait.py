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

driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

start_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='start']/button")))

start_button.click()

driver.implicitly_wait(10)

driver.quit()

