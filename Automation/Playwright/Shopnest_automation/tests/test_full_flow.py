# tests/test_full_flow.py

import pytest
from playwright.sync_api import Page, Browser
from page_object.login_page import LoginPage
from page_object.home_page import HomePage
from page_object.search_results_page import SearchResultsPage
from page_object.product_page import ProductPage
from page_object.cart_page import CartPage
from page_object.checkout_page import CheckoutPage
from data.test_data import TestData

class TestFullFlow:
    """
    Test class for complete e-commerce flow
    """
    
    @pytest.fixture(scope="function")
    def page(self, browser: Browser):
        """Setup fixture for each test"""
        page = browser.new_page()
        page.goto(TestData.login_url)
        yield page
        page.close()
    
    def test_complete_purchase_flow(self, page: Page):
        """
        TC_FULL_001: Complete purchase flow
        
        Steps:
        1. Login
        2. Search for a product
        3. Select product
        4. Add to cart
        5. Go to cart
        6. Proceed to checkout
        7. Fill address
        8. Select shipping
        9. Select payment
        10. Enter card details
        11. Confirm order
        12. Verify success
        """
        print("\nTEST: Complete Purchase Flow")
        
        # ============================================
        # STEP 1: Login
        # ============================================
        print("1️⃣ Logging in...")
        login_page = LoginPage(page)
        home_page = login_page.login(
            TestData.valid_user["email"],
            TestData.valid_user["password"]
        )
        
        # ✅ ADD DEBUGGING
        print(f"Current URL: {page.url}")
        print(f"Page title: {page.title()}")
        
        # Check if search field exists
        search_field_visible = page.is_visible("#small-searchterms")
        print(f"Search field visible: {search_field_visible}")
        
        # Check if account link exists
        account_visible = page.is_visible(".account")
        print(f"Account link visible: {account_visible}")
        
        # Check if we're on login page
        email_field_visible = page.is_visible("#Email")
        print(f"Email field visible: {email_field_visible}")
        
        # Now assert
        assert home_page.is_home_page(), "Should be on home page"
        
        
        # ============================================
        # STEP 2: Search for a product
        # ============================================
        print("============================================ 2 Searching for product...")
        search_results = home_page.search("book")
        assert search_results.has_results(), "Search should return results"
        print(f"Found {search_results.get_product_count()} results")
        
        # ============================================
        # STEP 3: Select first product
        # ============================================
        print("============================================ 3 Selecting first product...")
        product_page = search_results.select_product_by_index(0)
        product_name = product_page.get_product_name()
        print(f"Selected: {product_name}")
        
        # ============================================
        # STEP 4: Add to cart
        # ============================================
        print("============================================ 4 Adding to cart...")
        product_page.add_to_cart(1)
        print("Added to cart")

        # ✅ ADD THESE CHECKS:
        # Check if cart count increased
        cart_count_after = page.text_content(".cart-qty")
        print(f"📊 Cart count after add: {cart_count_after}")

        # Check if cart icon shows items
        cart_items_text = page.text_content(".cart-label")
        print(f"📊 Cart label: {cart_items_text}")

        # Take a screenshot to see what happened
        page.screenshot(path="reports/after_add_to_cart.png")
        print("📸 Screenshot saved: reports/after_add_to_cart.png")
        
        # ============================================
        # STEP 5: Go to cart using direct URL
        # ============================================
        print("============================================ 5 Going to cart...")

        # ✅ Direct navigation to cart page
        page.goto("https://demowebshop.tricentis.com/cart")
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(2000)

        print(f"📍 Cart page URL: {page.url}")

        # Create cart page object
        from page_object.cart_page import CartPage
        cart_page = CartPage(page)

        item_count = cart_page.get_cart_item_count()
        print(f"📊 Items in cart: {item_count}")

        assert item_count > 0, "Cart should have items"
        print(f"✅ Cart has {item_count} items")

        # ============================================
        # STEP 6: Proceed to checkout
        # ============================================
        print("============================================ 6 Proceeding to checkout...")
        checkout_page = cart_page.proceed_to_checkout()
        print(f"📍 After checkout URL: {page.url}")
        
        # ============================================
        # STEP 7: Fill billing address
        # ============================================
        print("============================================ 7 Filling billing address...")
        checkout_page.fill_billing_address({
            "first_name": "Test",
            "last_name": "User",
            "email": "test@example.com",
            "country": "1",
            "city": "New York",
            "address": "123 Main St",
            "zip": "10001",
            "phone": "1234567890"
        })
        checkout_page.click_billing_continue()
        print("Address filled")
        
        # ============================================
        # STEP 8: Select shipping method
        # ============================================
        print("============================================ 8 Selecting shipping method...")
        checkout_page.select_shipping_method(0)
        checkout_page.click_shipping_continue()
        print("Shipping selected")
        
        # ============================================
        # STEP 9: Select payment method
        # ============================================
        print("============================================ 9 Selecting payment method...")
        checkout_page.select_payment_method(0)
        checkout_page.click_payment_continue()
        print("Payment method selected")
        
        # ============================================
        # STEP 10: Enter card details
        # ============================================
        print("============================================ 10 Entering card details...")
        checkout_page.enter_card_details({
            "type": "1",
            "number": "4111111111111111",
            "expiry_month": "12",
            "expiry_year": "2026",
            "cvv": "123"
        })
        checkout_page.click_payment_info_continue()
        print("Card details entered")
        
        # ============================================
        # STEP 11: Confirm order
        # ============================================
        print("============================================ 11 Confirming order...")
        checkout_page.confirm_order()
        print("Order confirmed")
        
        # ============================================
        # STEP 12: Verify success
        # ============================================
        print("============================================ 12 Verifying order...")
        assert checkout_page.is_order_completed(), "Order should be completed"
        order_number = checkout_page.get_order_number()
        print(f"Order #{order_number} placed successfully!")
        
        print("\nCOMPLETE FLOW PASSED!")