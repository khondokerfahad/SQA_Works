from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto('https://google.com')
    print(f"Page title : {page.title()}")
    browser.close()

