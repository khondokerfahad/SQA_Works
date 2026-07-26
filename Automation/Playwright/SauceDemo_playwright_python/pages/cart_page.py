class CartPage:
    
    def __init__(self, page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator("#checkout")
        self.continue_shopping_button = page.locator("#continue-shopping")
        
    def get_item_names(self):
        return self.page.locator(".inventory_item_name").all_inner_texts()
    
    def remove_item_by_name(self, item_name):
        item = self.cart_items.filter(has_text = item_name)
        item.locator("button", has_text = "Remove").click()
        
    def get_cart_item_count(self):
        return self.cart_items.count()
    
    def got_to_checkout(self):
        self.checkout_button.click()
        
    def continue_shopping(self):
        self.continue_shopping_button.click()
        