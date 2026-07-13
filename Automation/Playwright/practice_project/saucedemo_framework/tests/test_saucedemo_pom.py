import pytest
from playwright.sync_api import Page, expect

# ====================== POM CLASSES (Inside same file) ======================

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def login(self):
        self.page.goto("https://www.saucedemo.com/")
        self.page.locator("[data-test='username']").fill("standard_user")
        self.page.locator("[data-test='password']").fill("secret_sauce")
        self.page.locator("[data-test='login-button']").click()
        print("✅ Login successful")


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

    def add_to_cart(self, product_name="Sauce Labs Backpack"):
        locators = {
            "Sauce Labs Backpack": "#add-to-cart-sauce-labs-backpack",
            "Sauce Labs Bike Light": "#add-to-cart-sauce-labs-bike-light",
            "Sauce Labs Bolt T-Shirt": "#add-to-cart-sauce-labs-bolt-t-shirt",
            "Sauce Labs Fleece Jacket": "#add-to-cart-sauce-labs-fleece-jacket",
            "Sauce Labs Onesie": "#add-to-cart-sauce-labs-onesie"
        }
        locator = locators.get(product_name)
        if locator:
            self.page.locator(locator).click()
            print(f"✅ Added '{product_name}' to cart")
        else:
            print("Product not found")

    def go_to_cart(self):
        self.page.locator(".shopping_cart_link").click()
        print("✅ Opened Cart page")


# ====================== TESTS ======================

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=700)
    yield browser
    browser.close()


def test_full_flow(page: Page):
    """Complete test using simple POM classes"""
    
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.login()
    inventory_page.add_to_cart("Sauce Labs Backpack")
    
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")
    
    inventory_page.go_to_cart()
    
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()

    print("\n🎉 Full Flow Test Passed Successfully!")


# Run the test
if __name__ == "__main__":
    pytest.main(["-v", "--headed", "--html=final_report.html", "--self-contained-html"])