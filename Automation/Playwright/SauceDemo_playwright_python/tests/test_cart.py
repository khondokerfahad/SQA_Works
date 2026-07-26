import pytest

from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.fixture

def cart_page_with_items(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    page.wait_for_url("**/inventory.html")
    
    inventory_page = InventoryPage(page)
    inventory_page.add_item_to_cart_by_name("Sauce Labs Backpack")
    inventory_page.add_item_to_cart_by_name("Sauce Labs Bike Light")
    inventory_page.go_to_cart()
    page.wait_for_url("**/cart.html")
    
    return CartPage(page)

def test_cart_shows_added_items(cart_page_with_items):
    item_names = cart_page_with_items.get_item_names()
    assert "Sauce Labs Backpack" in item_names
    assert "Sauce Labs Bike Light" in item_names
    assert cart_page_with_items.get_cart_item_count() == 2
    
def test_remove_item_from_cart_page(cart_page_with_items):
    cart_page_with_items.remove_item_by_name("Sauce Labs Backpack")
    expect(cart_page_with_items.cart_items).to_have_count(1)
    item_names = cart_page_with_items.get_item_names()
    assert "Sauce Labs Backpack" not in item_names
    
def test_continue_shopping_returns_to_inventory(cart_page_with_items):
    cart_page_with_items.continue_shopping()
    assert "inventory.html" in cart_page_with_items.page.url
    
def test_checkout_button_navigates_to_checkout(cart_page_with_items):
    cart_page_with_items.got_to_checkout()
    assert "checkout-step-one.html" in cart_page_with_items.page.url