from pages.base_page import BasePage
from playwright.sync_api import expect

class InventoryPage(BasePage):
    def add_to_cart(self, product_name):
        locators = {
            "Sauce Labs Backpack" : "#add-to-cart-sauce-labs-backpack",
            "Sauce Labs Bike Light" : "#add-to-cart-sauce-labs-bike-light",
            "Sauce Labs Bolt T-Shirt" : "#add-to-cart-sauce-labs-bolt-t-shirt",
            "Sauce Labs Fleece Jacket" : "#add-to-cart-sauce-labs-fleece-jacket",
            "Sauce Labs Onesie" : "#add-to-cart-sauce-labs-onesie",
            "Test.allTheThings() T-Shirt (Red)" : "button[id='add-to-cart-test.allthethings()-t-shirt-(red)']"
        }
        
        locator = locators.get(product_name)
        if locator:
            self.page.locator(locator).click()
            print(f"✅ Added '{product_name}' to cart")
        else:
            print(f"❌ Product '{product_name}' not found")
        
    def got_to_cart(self):
        self.page.locator(".shopping_cart_link").click()
        print("✅ Navigated to Cart page")