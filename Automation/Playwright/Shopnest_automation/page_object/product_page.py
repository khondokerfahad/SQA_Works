from page_object.base_page import BasePage

class ProductPage(BasePage):
    
    def __init__(self, page):
        super().__init__(page)
        
        # ============================================
        # LOCATORS - MORE SPECIFIC
        # ============================================
        
        self.product_name = ".product-name"
        self.product_price = ".price"
        self.product_availability = ".availability"
        
        # ✅ SPECIFIC: Only matches the add to cart button on product page
        self.add_to_cart_button = ".product-details-page .add-to-cart-button"
        
        # ✅ Alternative: Using the ID pattern
        self.add_to_cart_by_id = "input[id^='add-to-cart-button-']"
        
        self.add_to_wishlist_button = "input[value='Add to wishlist']"
        self.success_message = ".bar-notification.success"
        self.success_message_text = "#bar-notification .content"
        self.close_notification = ".bar-notification .close"
        self.reviews_tab = "a:has-text('Reviews')"
        self.write_review_button = "input[value='Write product review']"
    
    def get_product_name(self) -> str:
        """Get the product name"""
        return self.get_text(self.product_name).strip()
    
    def get_product_price(self) -> str:
        """Get the product price"""
        return self.get_text(self.product_price).strip()
    
    def add_to_cart(self, quantity: int = 1):
        """Add product to cart with proper verification"""
        print(f"🛒 Adding to cart (Quantity: {quantity})")
        
        # ============================================
        # STEP 1: Find and set quantity
        # ============================================
        
        # Try to find quantity field
        quantity_input = self.page.locator("input[name*='EnteredQuantity']")
        if quantity_input.count() > 0:
            quantity_input.fill(str(quantity))
            print("✅ Quantity set")
        
        # ============================================
        # STEP 2: Click Add to Cart
        # ============================================
        
        # Try multiple strategies
        try:
            # Strategy 1: Product detail page button
            button = self.page.locator(".product-details-page .add-to-cart-button")
            if button.count() > 0:
                button.click()
                print("✅ Clicked Add to Cart (Strategy 1)")
            else:
                # Strategy 2: ID pattern
                button = self.page.locator("input[id^='add-to-cart-button-']")
                if button.count() > 0:
                    button.click()
                    print("✅ Clicked Add to Cart (Strategy 2)")
                else:
                    # Strategy 3: By value
                    self.page.locator("input[value='Add to cart']").first.click()
                    print("✅ Clicked Add to Cart (Strategy 3)")
        except Exception as e:
            print(f"❌ Error clicking Add to Cart: {e}")
            raise
        
        # ============================================
        # STEP 3: Verify success
        # ============================================
        
        # Wait for update
        self.page.wait_for_timeout(2000)
        
        # Check success message
        success = self.page.locator(".bar-notification.success")
        if success.count() > 0:
            success_text = success.text_content()
            print(f"✅ Success: {success_text.strip()}")
        else:
            # Check for error
            error = self.page.locator(".bar-notification.error")
            if error.count() > 0:
                error_text = error.text_content()
                print(f"❌ Error: {error_text.strip()}")
                raise AssertionError(f"Add to cart failed: {error_text}")
            else:
                print("⚠️ No success/error message found, but click was attempted")
        
        # Check cart count in header
        cart_qty = self.page.text_content(".cart-qty")
        print(f"📊 Cart count: {cart_qty}")
        
        return self
    
    def go_to_cart(self):
        """
        Go to cart page with proper waiting and debugging
        """
        print("🛒 Attempting to go to cart...")
        
        # Take a screenshot before clicking cart
        self.page.screenshot(path="reports/before_cart_click.png")
        print("📸 Screenshot saved: reports/before_cart_click.png")
        
        # Find the cart link/icon
        # Different possible selectors for cart
        cart_selectors = [
            "a[href='/cart']",
            ".cart-label",
            ".cart-icon",
            "a:has-text('Shopping cart')",
            "a:has-text('Cart')",
            "#topcartlink"
        ]
        
        cart_found = False
        for selector in cart_selectors:
            if self.page.locator(selector).count() > 0:
                print(f"📍 Found cart with selector: {selector}")
                self.page.locator(selector).click()
                cart_found = True
                break
        
        if not cart_found:
            print("❌ No cart link found on page!")
            # Print all links to see what's available
            links = self.page.locator("a").all()
            for link in links:
                text = link.text_content()
                if text and "cart" in text.lower():
                    print(f"🔗 Found link: '{text}'")
            raise AssertionError("Could not find cart link")
        
        # Wait for cart page to load
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)
        
        print(f"📍 Cart page URL: {self.page.url}")
        
        # Take a screenshot after clicking cart
        self.page.screenshot(path="reports/after_cart_click.png")
        print("📸 Screenshot saved: reports/after_cart_click.png")
        
        # Import here to avoid circular imports
        from page_object.cart_page import CartPage
        return CartPage(self.page)
    
    def add_to_wishlist(self):
        """Add product to wishlist"""
        print("💝 Adding to wishlist")
        self.click(self.add_to_wishlist_button)
        self.wait_for_element(self.success_message)
        return self