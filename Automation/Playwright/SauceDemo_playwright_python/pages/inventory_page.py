class InventoryPage:
    
    def __init__(self, page):
        self.page = page
        self.inventory_items = page.locator(".inventory_item")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.sort_dropdown = page.locator(".product_sort_container")
        
    def add_item_to_cart_by_name(self, item_name):
        item = self.page.locator(".inventory_item", has_text = item_name)
        item.locator("button", has_text= "Add to cart").click()
    
    def remove_item_from_cart_by_name(self, item_name):
        item = self.page.locator(".inventory_item", has_text=item_name)
        remove_button = item.locator("button", has_text="Remove")
        print("Button text before click:", remove_button.inner_text())
        remove_button.click()
        print("Button text after click:", item.locator("button").inner_text())
        
    def get_cart_count(self):
        # if self.cart_badge.is_visible():
        #     return int(self.cart_badge.inner_text())
        # return 0
        try:
            return int(self.cart_badge.inner_text())
        except Exception:
            return 0
    
    def sort_by(self, option_value):
        self.sort_dropdown.select_option(option_value)
        
    def go_to_cart(self):
        self.cart_icon.click()
        
    