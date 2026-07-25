import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

products_name = [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Fleece Jacket",
    "Sauce Labs Onesie",
    "Test.allTheThings() T-Shirt (Red)",
]

@pytest.fixture

def inventory_page(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    page.wait_for_url("**/inventory.html")
    return InventoryPage(page)

def test_all_products_visible(inventory_page):
    assert inventory_page.inventory_items.count() == 6
    
def test_add_single_item_to_cart(inventory_page):
    inventory_page.add_item_to_cart_by_name("Sauce Labs Backpack")
    assert inventory_page.get_cart_count() == 1
    
def test_add_multiple_items_to_cart(inventory_page):
    inventory_page.add_item_to_cart_by_name("Sauce Labs Bike Light")
    inventory_page.add_item_to_cart_by_name("Sauce Labs Bolt T-Shirt")
    inventory_page.add_item_to_cart_by_name("Sauce Labs Fleece Jacket")
    assert inventory_page.get_cart_count() == 3
    
def test_remove_items_from_cart(inventory_page):
    inventory_page.add_item_to_cart_by_name("Sauce Labs Fleece Jacket")
    assert inventory_page.get_cart_count() == 1
    inventory_page.remove_item_from_cart_by_name("Sauce Labs Fleece Jacket")
    expect(inventory_page.cart_badge).to_have_count(0)

def test_sort_by_name_za(inventory_page):
    inventory_page.sort_by("za")
    displayed_names = inventory_page.page.locator(".inventory_item_name").all_inner_texts()
    assert displayed_names == sorted(products_name, reverse=True)


def test_sort_by_price_low_high(inventory_page):
    inventory_page.sort_by("lohi")
    displayed_prices = inventory_page.page.locator(".inventory_item_price").all_inner_texts()
    prices = [float(p.replace("$", "")) for p in displayed_prices]
    assert prices == sorted(prices)


def test_sort_by_price_high_low(inventory_page):
    inventory_page.sort_by("hilo")
    displayed_prices = inventory_page.page.locator(".inventory_item_price").all_inner_texts()
    prices = [float(p.replace("$", "")) for p in displayed_prices]
    assert prices == sorted(prices, reverse=True)


def test_cart_icon_navigates_to_cart_page(inventory_page):
    inventory_page.go_to_cart()
    assert "cart.html" in inventory_page.page.url