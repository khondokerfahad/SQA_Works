from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By         #for select by type
import time

#blocking popupd
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

#chrome driver setup
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_options)

driver.get("https://demo.seleniumeasy.com/basic-radiobutton-demo.html")

# Not complete
