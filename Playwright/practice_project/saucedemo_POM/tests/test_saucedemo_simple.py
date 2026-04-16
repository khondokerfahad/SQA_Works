from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import os
from datetime import datetime

def run_test():
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False, slow_mo=1000)
        page = browser.new()
        
        print("🚀 Starting Simple SauceDemo Test\n")
        
        try :
            page.goto("https://www.saucedemo.com/")
            login_page = LoginPage(page)
            inventory_page = InventoryPage(page)
            
            login_page.login("standard_user", "secret_sauce")
            print("✅ Step 1: Login successful")
            
            inventory_page.add_product_to_cart("Sauce Labs Bike Light")
            
            expect(page.locator(".shopping_cart_badge")).to_have_text("1")
            print("✅ Step 2: Cart badge shows 1 item")
            
            inventory_page.go_to_cart()
            
            page.wait_for_url("**/cart.html", timeout=10000)
            print("✅ Step 3: Cart page opened")
            
            expect(page.get_by_text("Sauce Labs Bike Light")).to_be_visible()
            print("✅ Step 4: Product verified in cart")

            print("\n🎉 Simple Test Completed Successfully!")
            
        except Exception as e:
            print(f"\n❌ Test Failed: {e}")
            page.screenshot(path=os.path.join(screenshot_dir, f"ERROR_{timestamp}.png"))

if __name__ == "__main__":
    run_test()