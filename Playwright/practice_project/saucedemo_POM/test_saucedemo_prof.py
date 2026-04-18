import pytest
from playwright.sync_api import Page, expect

# ====================== FIXTURES ======================

@pytest.fixture(scope="function")
def page(browser):
    """Create a new page for each test"""
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="session")
def browser(playwright):
    """Launch browser once for all tests"""
    # You can change browser here: chromium, firefox, webkit
    browser = playwright.chromium.launch(headless=False, slow_mo=600)
    yield browser
    browser.close()


# ====================== TESTS ======================

def test_successful_login(page: Page):
    """Test Case 1: Verify successful login"""
    page.goto("https://www.saucedemo.com/")
    
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.get_by_text("Products")).to_be_visible()
    
    print("✅ TC01 - Login Test Passed")


def test_add_product_to_cart(page: Page):
    """Test Case 2: Add product to cart"""
    page.goto("https://www.saucedemo.com/")
    
    # Login
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

    # Add product
    page.locator("#add-to-cart-sauce-labs-backpack").click()

    # Verify cart badge
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")
    
    print("✅ TC02 - Add to Cart Test Passed")


def test_full_checkout_flow(page: Page):
    """Test Case 3: Full flow - Login + Add to cart + Go to cart"""
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
    
    print("✅ TC03 - Full Flow Test Passed")


# ====================== Run Configuration ======================
if __name__ == "__main__":
    pytest.main([
        "-v",                    # Verbose output
        "--headed",              # Show browser
        "--html=report.html",    # Generate HTML report
        "--self-contained-html", # Make report self-contained
        "--browser=chromium"     # You can also try: firefox, webkit
    ])