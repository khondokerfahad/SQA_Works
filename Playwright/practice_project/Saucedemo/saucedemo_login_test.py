import os
from playwright.sync_api import sync_playwright, expect
from datetime import datetime

def main():
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok = True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = True, slow_mo=1000)
        page = browser.new_page()
        
        print("Starting SauceDemo Login Test")
        
        page.goto("https://www.saucedemo.com/")
        page.screenshot(path=os.path.join(screenshot_dir, f"01_saucedemo-loginpage_{timestamp}.png"))
        print("✅ Step 1: Opened SauceDemo login Page")
        
        
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.screenshot(path=os.path.join(screenshot_dir, f"02_saucedemo-credentials_{timestamp}.png"))
        page.get_by_role("button", name = "Login").click()
        print("✅ Step 2: Clicked Login")
        
        page.wait_for_url("**/inventory.html", timeout=30000)
        page.screenshot(path=os.path.join(screenshot_dir, f"03_saucedemo-inventory_{timestamp}.png"))
        
        try:
            expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
            print("✅ Assertion 1 Passed: Redirected to Inventory page")
        except Exception as e:
            print(f"❌ Assertion 1 FAILED: URL is incorrect. Error: {e}")
            page.screenshot(path=os.path.join(screenshot_dir, f"ERROR_url_failed_{timestamp}.png"))
            raise
        
        try:
            expect(page.get_by_text("Products")).to_be_visible(timeout=3000)
            print("✅ Assertion 2 PASSED: At least one product is displayed")
        except Exception as e:
            print(f"❌ Assertion 2 FAILED: No products found. Error: {e}")
            page.screenshot(path=os.path.join(screenshot_dir, f"ERROR_no_products_{timestamp}.png"))
            raise
        
if __name__ == "__main__":
    main()