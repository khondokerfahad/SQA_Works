# page_objects/checkout_page.py

from page_object.base_page import BasePage

class CheckoutPage(BasePage):
    """
    Checkout Page Object
    
    Handles shipping address, payment, and order confirmation
    """
    
    def __init__(self, page):
        super().__init__(page)
        
        # ============================================
        # BILLING ADDRESS (Step 1)
        # ============================================
        
        self.billing_first_name = "#BillingNewAddress_FirstName"
        self.billing_last_name = "#BillingNewAddress_LastName"
        self.billing_email = "#BillingNewAddress_Email"
        self.billing_country = "#BillingNewAddress_CountryId"
        self.billing_city = "#BillingNewAddress_City"
        self.billing_address = "#BillingNewAddress_Address1"
        self.billing_zip = "#BillingNewAddress_ZipPostalCode"
        self.billing_phone = "#BillingNewAddress_PhoneNumber"
        
        self.billing_continue = "input[onclick='Billing.save()']"
        
        # ============================================
        # SHIPPING METHOD (Step 2)
        # ============================================
        
        self.shipping_method = "input[name='shippingoption']"
        self.shipping_continue = "input[onclick='ShippingMethod.save()']"
        
        # ============================================
        # PAYMENT METHOD (Step 3)
        # ============================================
        
        self.payment_method = "input[name='paymentmethod']"
        self.payment_continue = "input[onclick='PaymentMethod.save()']"
        
        # ============================================
        # PAYMENT INFO (Step 4)
        # ============================================
        
        self.card_type = "#CreditCardType"
        self.card_number = "#CardNumber"
        self.card_expiry_month = "#ExpireMonth"
        self.card_expiry_year = "#ExpireYear"
        self.card_code = "#CardCode"
        
        self.payment_info_continue = "input[onclick='PaymentInfo.save()']"
        
        # ============================================
        # CONFIRM ORDER (Step 5)
        # ============================================
        
        self.confirm_button = "input[value='Confirm']"
        
        # ============================================
        # ORDER COMPLETED
        # ============================================
        
        self.order_complete_message = ".order-completed"
        self.order_number = ".order-number"
        self.continue_button = "input[value='Continue']"
    
    # ============================================
    # BILLING ADDRESS METHODS
    # ============================================
    
    def fill_billing_address(self, address_data: dict):
        """Fill billing address form"""
        print("📝 Filling billing address")
        
        self.fill(self.billing_first_name, address_data.get("first_name", "Test"))
        self.fill(self.billing_last_name, address_data.get("last_name", "User"))
        self.fill(self.billing_email, address_data.get("email", "test@example.com"))
        self.select_option(self.billing_country, address_data.get("country", "1"))  # 1 = USA
        self.fill(self.billing_city, address_data.get("city", "New York"))
        self.fill(self.billing_address, address_data.get("address", "123 Main St"))
        self.fill(self.billing_zip, address_data.get("zip", "10001"))
        self.fill(self.billing_phone, address_data.get("phone", "1234567890"))
        
        return self
    
    def click_billing_continue(self):
        """Proceed to shipping method"""
        self.click(self.billing_continue)
        return self
    
    # ============================================
    # SHIPPING METHOD METHODS
    # ============================================
    
    def select_shipping_method(self, method_index: int = 0):
        """Select shipping method"""
        methods = self.page.locator(self.shipping_method).all()
        if method_index < len(methods):
            methods[method_index].check()
        return self
    
    def click_shipping_continue(self):
        """Proceed to payment method"""
        self.click(self.shipping_continue)
        return self
    
    # ============================================
    # PAYMENT METHOD METHODS
    # ============================================
    
    def select_payment_method(self, method_index: int = 0):
        """Select payment method"""
        methods = self.page.locator(self.payment_method).all()
        if method_index < len(methods):
            methods[method_index].check()
        return self
    
    def click_payment_continue(self):
        """Proceed to payment info"""
        self.click(self.payment_continue)
        return self
    
    # ============================================
    # PAYMENT INFO METHODS
    # ============================================
    
    def enter_card_details(self, card_data: dict):
        """Enter credit card details"""
        print("💳 Entering card details")
        
        self.select_option(self.card_type, card_data.get("type", "1"))  # 1 = Visa
        self.fill(self.card_number, card_data.get("number", "4111111111111111"))
        self.select_option(self.card_expiry_month, card_data.get("expiry_month", "12"))
        self.select_option(self.card_expiry_year, card_data.get("expiry_year", "2026"))
        self.fill(self.card_code, card_data.get("cvv", "123"))
        
        return self
    
    def click_payment_info_continue(self):
        """Proceed to confirm order"""
        self.click(self.payment_info_continue)
        return self
    
    # ============================================
    # ORDER CONFIRMATION METHODS
    # ============================================
    
    def confirm_order(self):
        """Confirm the order"""
        print("✅ Confirming order")
        self.click(self.confirm_button)
        return self
    
    def get_order_number(self) -> str:
        """Get order number from confirmation"""
        return self.get_text(self.order_number).strip()
    
    def is_order_completed(self) -> bool:
        """Check if order was successfully placed"""
        return self.is_visible(self.order_complete_message)
    
    def continue_to_home(self):
        """Continue to home page after order"""
        self.click(self.continue_button)
        from page_object.home_page import HomePage
        return HomePage(self.page)