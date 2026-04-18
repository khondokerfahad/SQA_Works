import pytest
from playwright.sync_api import Page, expect
import os
from datetime import datetime

# Fixture to setup browser and page
@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    # page.close()   # optional

# Test 1: Login Test
def test_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    print("✅ Login Test Passed")


# Test 2: Add Product to Cart
def test_add_to_cart(page: Page):
    page.goto("https://www.saucedemo.com/")
    
    # Login
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

    # Add product using simple CSS selector
    page.locator("#add-to-cart-sauce-labs-backpack").click()

    # Verify cart badge
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")
    print("✅ Product added to cart - Test Passed")


# Test 3: Full Flow - Login + Add to Cart + Go to Cart
def test_full_flow(page: Page):
    page.goto("https://www.saucedemo.com/")
    
    # Login
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

    # Add product
    page.locator("#add-to-cart-sauce-labs-backpack").click()

    # Go to cart
    page.locator(".shopping_cart_link").click()

    # Assertions
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()
    
    print("✅ Full Flow Test Passed")


# Run tests with nice reporting
if __name__ == "__main__":
    pytest.main(["-v", "--headed"])   # -v = verbose, --headed = show browser