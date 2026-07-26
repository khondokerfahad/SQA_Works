import pytest

from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

@pytest.fixture

def checkout_page_with_items(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    page.wait_for_url("**/inventory.html")
    
    inventory_page = InventoryPage(page)
    inventory_page.add_item_to_cart_by_name("Sauce Labs Backpack")
    inventory_page.go_to_cart()
    page.wait_for_url("**/cart.html")
    
    page.locator("#checkout").click()
    page.wait_for_url("**/checkout-step-one.html")
    
    return CheckoutPage(page)

def test_checkout_valid_information(checkout_page_with_items):
    checkout_page_with_items.fill_information("Fahad", "Ahmed", "2500")
    checkout_page_with_items.page.wait_for_url("**/checkout-step-two.html")
    assert "checkout-step-two.html" in checkout_page_with_items.page.url
    
def test_checkout_missing_first_name(checkout_page_with_items):
    checkout_page_with_items.fill_information("", "Ahmed", "2500")
    assert checkout_page_with_items.error_message.is_visible()
    assert "First Name is required" in checkout_page_with_items.error_message.inner_text()
    
def test_checkout_missing_last_name(checkout_page_with_items):
    checkout_page_with_items.fill_information("Fahad", "", "2500")
    assert checkout_page_with_items.error_message.is_visible()
    assert "Last Name is required" in checkout_page_with_items.error_message.inner_text()
    
def test_checkout_missing_postal_code(checkout_page_with_items):
    checkout_page_with_items.fill_information("Fahad", "Ahmed", "")
    assert checkout_page_with_items.error_message.is_visible()
    assert "Postal Code is required" in checkout_page_with_items.error_message.inner_text()
    
def test_complete_checkout_flow(checkout_page_with_items):
    checkout_page_with_items.fill_information("Fahad", "Ahmed", "2500")
    checkout_page_with_items.page.wait_for_url("**/checkout-step-two.html")
    
    checkout_page_with_items.finish_checkout()
    checkout_page_with_items.page.wait_for_url("**/checkout-complete.html")
    
    expect(checkout_page_with_items.complete_header).to_have_text("Thank you for your order!")
    
def test_back_to_products_from_complete_page(checkout_page_with_items):
    checkout_page_with_items.fill_information("Fahad", "Ahmed", "2500")
    checkout_page_with_items.page.wait_for_url("**/checkout-step-two.html")
    
    checkout_page_with_items.finish_checkout()
    checkout_page_with_items.page.wait_for_url("**/checkout-complete.html")
    
    checkout_page_with_items.go_back_to_products()
    assert "inventory.html" in checkout_page_with_items.page.url