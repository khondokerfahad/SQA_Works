from playwright.sync_api import sync_playwright, expect
import os
from datetime import datetime

def run_test():
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        print("🚀 Starting SauceDemo Add to Cart Test\n")

        try:
            # Login
            page.goto("https://www.saucedemo.com/")
            page.locator("[data-test='username']").fill("standard_user")
            page.locator("[data-test='password']").fill("secret_sauce")
            page.locator("[data-test='login-button']").click()

            page.wait_for_url("**/inventory.html", timeout=15000)
            print("✅ Step 1: Login successful")

            # Add product
            page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
            print("✅ Step 2: Added Sauce Labs Backpack to cart")

            # Verify badge
            expect(page.locator("[data-test='shopping-cart-badge']")).to_have_text("1", timeout=10000)
            print("✅ Step 3: Cart badge shows 1 item")

            # === CORRECT CART CLICK (from your Codegen) ===
            print("Clicking shopping cart icon using data-test locator...")
            page.locator(".shopping_cart_link").click()

            # Wait for cart page
            page.wait_for_url("**/cart.html", timeout=15000)
            page.screenshot(path=os.path.join(screenshot_dir, f"03_cart_page_{timestamp}.png"))
            print("✅ Step 4: Cart page opened successfully!")

            # Verify product in cart
            expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible(timeout=10000)
            print("✅ Step 5: Product is visible in cart")

            print("\n🎉 SUCCESS! Test completed without errors.")

        except Exception as e:
            print(f"\n❌ Test Failed: {e}")
            page.screenshot(path=os.path.join(screenshot_dir, f"ERROR_{timestamp}.png"))
            page.screenshot(path=os.path.join(screenshot_dir, f"debug_failure_{timestamp}.png"))
        
        finally:
            print("\nTest execution finished.")

if __name__ == "__main__":
    run_test()