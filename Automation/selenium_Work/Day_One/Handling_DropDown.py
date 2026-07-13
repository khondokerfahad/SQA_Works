from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By         #for select which 
import time

#blocking popupd
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

#chrome driver setup
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_options)

driver.get("https://the-internet.herokuapp.com/dropdown")

#select option by ID
drop_down_elements = driver.find_element(By.ID, "dropdown")

drop_down = Select(drop_down_elements)

#grab all the options 
all_options = drop_down.options

print(f"Total possible options : {len(all_options)}")

for option in all_options:
    print(f"Options : {option.text}")
    drop_down.select_by_visible_text(option.text)
    time.sleep(2)

time.sleep(2)

driver.quit()
