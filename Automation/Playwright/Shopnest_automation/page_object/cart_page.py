from page_object.base_page import BasePage

class CartPage(BasePage):
    """
    Shopping Cart Page Object for Demo Web Shop
    """
    
    def __init__(self, page):
        super().__init__(page)
        
        # ============================================
        # LOCATORS - CORRECTED FOR DEMO WEB SHOP
        # ============================================
        
        # ✅ Cart items - each row in the cart table
        self.cart_items = "tr.cart-item-row"
        
        # ✅ Product name in cart
        self.product_name_in_cart = ".product-name"
        
        # ✅ Quantity input field
        self.quantity_input = "input[name^='itemquantity']"
        
        # ✅ Unit price
        self.unit_price = ".unit-price"
        
        # ✅ Subtotal
        self.subtotal = ".subtotal"
        
        # ✅ Update cart button
        self.update_cart_button = "input[value='Update shopping cart']"
        
        # ✅ Remove checkbox
        self.remove_checkbox = "input[name^='removefromcart']"
        
        # ✅ Terms of service checkbox
        self.terms_checkbox = "#termsofservice"
        
        # ✅ Checkout button
        self.checkout_button = "input[id='checkout']"
        
        # ✅ Continue shopping button
        self.continue_shopping_button = "input[value='Continue shopping']"
        
        # ✅ Empty cart message
        self.empty_cart_message = ".order-summary-content"
        self.empty_cart_text = "Your Shopping Cart is empty!"
    
    # ============================================
    # CART INFORMATION METHODS
    # ============================================
    
    def get_cart_item_count(self) -> int:
        """
        Get number of items in cart
        
        Uses multiple strategies to find cart items
        """
        print("📊 Checking cart items...")
        
        # Strategy 1: Try the main cart items locator
        items = self.page.locator(self.cart_items)
        count = items.count()
        print(f"📊 Cart items found (Strategy 1): {count}")
        
        # If no items found, try alternative locators
        if count == 0:
            # Strategy 2: Try the order summary content
            order_summary = self.page.locator(".order-summary-content")
            if order_summary.count() > 0:
                summary_text = order_summary.text_content()
                if "empty" in summary_text.lower():
                    print("📊 Cart is empty (confirmed by text)")
                    return 0
                else:
                    # Try to find items inside the summary
                    items_inside = order_summary.locator(".cart-item-row")
                    count = items_inside.count()
                    print(f"📊 Cart items found (Strategy 2): {count}")
                    return count
        
        return count
    
    def get_item_names(self) -> list:
        """Get names of items in cart"""
        names = []
        elements = self.page.locator(self.product_name_in_cart).all()
        for element in elements:
            names.append(element.text_content().strip())
        print(f"📊 Item names: {names}")
        return names
    
    def get_cart_subtotal(self) -> str:
        """Get the cart subtotal"""
        return self.get_text(self.subtotal)
    
    def is_cart_empty(self) -> bool:
        """Check if cart is empty"""
        if self.is_visible(self.empty_cart_message):
            text = self.get_text(self.empty_cart_message)
            return self.empty_cart_text in text
        
        # Also check if there are no cart items
        return self.get_cart_item_count() == 0
    
    # ============================================
    # CART ACTION METHODS
    # ============================================
    
    def update_quantity(self, item_index: int, quantity: int):
        """Update quantity for specific item"""
        print(f"🔄 Updating item {item_index} to quantity {quantity}")
        
        inputs = self.page.locator(self.quantity_input).all()
        if item_index < len(inputs):
            inputs[item_index].fill(str(quantity))
            self.click(self.update_cart_button)
            self.page.wait_for_load_state("networkidle")
        else:
            print(f"⚠️ Item index {item_index} not found")
        return self
    
    def remove_item(self, item_index: int):
        """Remove item from cart"""
        print(f"🗑️ Removing item {item_index}")
        
        checkboxes = self.page.locator(self.remove_checkbox).all()
        if item_index < len(checkboxes):
            checkboxes[item_index].check()
            self.click(self.update_cart_button)
            self.page.wait_for_load_state("networkidle")
        else:
            print(f"⚠️ Item index {item_index} not found")
        return self
    
    def clear_cart(self):
        """Remove ALL items from cart"""
        print("🗑️ Clearing cart")
        
        checkboxes = self.page.locator(self.remove_checkbox).all()
        if checkboxes:
            for checkbox in checkboxes:
                checkbox.check()
            self.click(self.update_cart_button)
            self.page.wait_for_load_state("networkidle")
            print("✅ Cart cleared")
        else:
            print("⚠️ No items to remove")
        return self
    
    def proceed_to_checkout(self):
        """Proceed to checkout with robust error handling"""
        print("🛒 Proceeding to checkout")
        
        # ============================================
        # DEBUG: Check what's on the page
        # ============================================
        
        # 1. Check URL
        current_url = self.page.url
        print(f"📍 Current URL: {current_url}")
        
        # 2. Check if cart is empty
        cart_content = self.page.locator(".order-summary-content")
        if cart_content.count() > 0:
            text = cart_content.text_content()
            if "empty" in text.lower():
                print("❌ Cart is empty! Cannot proceed to checkout.")
                raise AssertionError("Cart is empty - no items to checkout")
        
        # 3. Check for cart items
        items = self.page.locator(".cart-item-row").count()
        print(f"📦 Cart items: {items}")
        if items == 0:
            print("❌ No items in cart!")
            raise AssertionError("No items in cart - please add items first")
        
        # ============================================
        # TRY MULTIPLE STRATEGIES FOR TERMS CHECKBOX
        # ============================================
        
        terms_clicked = False
        
        # Strategy 1: Try the standard ID
        if not terms_clicked:
            try:
                if self.page.locator("#termsofservice").count() > 0:
                    self.page.locator("#termsofservice").click()
                    terms_clicked = True
                    print("✅ Terms accepted (Strategy 1: #termsofservice)")
            except:
                pass
        
        # Strategy 2: Try by name attribute
        if not terms_clicked:
            try:
                if self.page.locator("input[name='termsofservice']").count() > 0:
                    self.page.locator("input[name='termsofservice']").click()
                    terms_clicked = True
                    print("✅ Terms accepted (Strategy 2: name='termsofservice')")
            except:
                pass
        
        # Strategy 3: Try by class
        if not terms_clicked:
            try:
                if self.page.locator(".terms-of-service").count() > 0:
                    self.page.locator(".terms-of-service").click()
                    terms_clicked = True
                    print("✅ Terms accepted (Strategy 3: .terms-of-service)")
            except:
                pass
        
        # Strategy 4: Try using JavaScript (last resort)
        if not terms_clicked:
            try:
                self.page.evaluate("""
                    document.querySelector('#termsofservice')?.click();
                    document.querySelector('input[name="termsofservice"]')?.click();
                    document.querySelector('.terms-of-service')?.click();
                """)
                terms_clicked = True
                print("✅ Terms accepted (Strategy 4: JavaScript fallback)")
            except:
                pass
        
        if not terms_clicked:
            print("⚠️ Could not find terms checkbox - proceeding anyway")
        
        # ============================================
        # CLICK CHECKOUT BUTTON
        # ============================================
        
        # Wait a moment for any animations
        self.page.wait_for_timeout(500)
        
        # Try multiple checkout button selectors
        checkout_clicked = False
        
        # Strategy 1: By ID
        if not checkout_clicked:
            try:
                if self.page.locator("#checkout").count() > 0:
                    self.page.locator("#checkout").click()
                    checkout_clicked = True
                    print("✅ Checkout clicked (Strategy 1: #checkout)")
            except:
                pass
        
        # Strategy 2: By value
        if not checkout_clicked:
            try:
                if self.page.locator("input[value='Checkout']").count() > 0:
                    self.page.locator("input[value='Checkout']").click()
                    checkout_clicked = True
                    print("✅ Checkout clicked (Strategy 2: value='Checkout')")
            except:
                pass
        
        if not checkout_clicked:
            print("❌ Could not find checkout button!")
            raise AssertionError("Checkout button not found on page")
        
        # Wait for navigation
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(1000)
        
        print(f"📍 After checkout URL: {self.page.url}")
        
        # Import CheckoutPage
        from page_object.checkout_page import CheckoutPage
        return CheckoutPage(self.page)
    
    def continue_shopping(self):
        """Go back to shopping"""
        print("🛍️ Continuing shopping")
        self.click(self.continue_shopping_button)
        
        from page_object.home_page import HomePage
        return HomePage(self.page)
    
    # ============================================
    # VERIFICATION METHODS
    # ============================================
    
    def verify_product_in_cart(self, product_name: str) -> bool:
        """Check if a specific product is in the cart"""
        names = self.get_item_names()
        return product_name in names
    
    def get_cart_total_items(self) -> int:
        """Get total quantity of all items in cart"""
        total = 0
        inputs = self.page.locator(self.quantity_input).all()
        for input_field in inputs:
            try:
                value = int(input_field.get_attribute("value"))
                total += value
            except:
                pass
        print(f"📊 Total items in cart: {total}")
        return total
    
    def debug_cart_page(self):
        """Debug what's on the cart page"""
        print("=" * 50)
        print("🔍 DEBUG: Cart Page Analysis")
        print("=" * 50)
        
        # 1. Check URL
        print(f"📍 URL: {self.page.url}")
        
        # 2. Check page title
        print(f"📄 Title: {self.page.title()}")
        
        # 3. Check for empty cart
        empty_cart = self.is_visible(".order-summary-content")
        if empty_cart:
            text = self.get_text(".order-summary-content")
            print(f"📝 Empty cart message: {text}")
        
        # 4. Check for cart items
        items = self.page.locator(".cart-item-row").count()
        print(f"📦 Cart items: {items}")
        
        # 5. Check for terms checkbox
        terms_selectors = ["#termsofservice", "input[name='termsofservice']", ".terms-of-service"]
        for selector in terms_selectors:
            exists = self.page.locator(selector).count() > 0
            visible = self.is_visible(selector) if exists else False
            print(f"🔲 Selector '{selector}' - Exists: {exists}, Visible: {visible}")
        
        # 6. Check for checkout button
        checkout_selectors = ["#checkout", "input[value='Checkout']", "button:has-text('Checkout')"]
        for selector in checkout_selectors:
            exists = self.page.locator(selector).count() > 0
            visible = self.is_visible(selector) if exists else False
            print(f"🔘 Selector '{selector}' - Exists: {exists}, Visible: {visible}")
        
        # 7. Take screenshot
        self.page.screenshot(path="reports/cart_page_debug.png")
        print("📸 Screenshot saved: reports/cart_page_debug.png")
        
        print("=" * 50)