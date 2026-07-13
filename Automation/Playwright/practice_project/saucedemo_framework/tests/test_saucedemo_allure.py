import pytest 
import allure 
from playwright.sync_api import Page, expect
from datetime import datetime

# ====================== PAGE CLASSES ======================

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Login to SauceDemo")
    def login(self):
        self.page.goto("https://www.saucedemo.com/")
        self.page.locator("[data-test='username']").fill("standard_user")
        self.page.locator("[data-test='password']").fill("secret_sauce")
        self.page.locator("[data-test='login-button']").click()
        allure.attach(self.page.screenshot(), name="After_Login", attachment_type=allure.attachment_type.PNG)


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Add product to cart: {product_name}")
    def add_to_cart(self, product_name="Sauce Labs Backpack"):
        locators = {
            "Sauce Labs Backpack": "#add-to-cart-sauce-labs-backpack",
            "Sauce Labs Bike Light": "#add-to-cart-sauce-labs-bike-light",
            "Sauce Labs Bolt T-Shirt": "#add-to-cart-sauce-labs-bolt-t-shirt",
            "Sauce Labs Fleece Jacket": "#add-to-cart-sauce-labs-fleece-jacket",
            "Sauce Labs Onesie": "#add-to-cart-sauce-labs-onesie"
        }
        self.page.locator(locators[product_name]).click()
        allure.attach(self.page.screenshot(), name=f"After_Adding_{product_name}", attachment_type=allure.attachment_type.PNG)

    @allure.step("Go to Shopping Cart")
    def go_to_cart(self):
        self.page.locator(".shopping_cart_link").click()


# ====================== TESTS ======================

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=600)
    yield browser
    browser.close()


@allure.title("SauceDemo - Full E2E Flow")
@allure.severity(allure.severity_level.CRITICAL)
def test_full_e2e_flow(page: Page):
    """End-to-End test with Allure reporting"""
    
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    with allure.step("Step 1: Perform Login"):
        login_page.login()

    with allure.step("Step 2: Add product to cart"):
        inventory_page.add_to_cart("Sauce Labs Backpack")

    with allure.step("Step 3: Verify Cart Badge"):
        expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    with allure.step("Step 4: Go to Cart"):
        inventory_page.go_to_cart()

    with allure.step("Step 5: Verify Product in Cart"):
        expect(page).to_have_url("https://www.saucedemo.com/cart.html")
        expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()

    allure.attach(page.screenshot(), name="Final_Cart_Page", attachment_type=allure.attachment_type.PNG)
    print("\n🎉 Allure Test Completed Successfully!")


# Run with Allure
if __name__ == "__main__":
    pytest.main([
        "-v",
        "--headed",
        "--alluredir=allure-results",   # Store results
        "--clean-alluredir"             # Clean old results
    ])