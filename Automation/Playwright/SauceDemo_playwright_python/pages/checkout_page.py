class CheckoutPage:
    
    def __init__(self, page):
        self.page = page
        
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.error_message = page.locator("h3[data-test='error']")
        
        #next page
        self.finish_button = page.locator("#finish")
        self.cart_items = page.locator(".cart_item")
        self.summary_info = page.locator(".summary_info")
        
        #next page
        self.complete_header = page.locator(".complete-header")
        self.back_home_button = page.locator("#back-to-products")
        
    def fill_information(self, first_name, last_name, postal_code):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()
        
    def finish_checkout(self):
        self.finish_button.click()
        
    def go_back_to_products(self):
        self.back_home_button.click()