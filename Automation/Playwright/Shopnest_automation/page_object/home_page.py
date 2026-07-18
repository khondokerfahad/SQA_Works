from page_object.base_page import BasePage

class HomePage(BasPage):
    def __init__(self, page):
        super().__init__(page)
        
        self.search_field = "#small-searchterms"
        self.cart_icon = ".cart-label"
        self.user_avatar = ".account"
        self.logout_link = "a:has-text('Log out')"
        self.welcome_message = ".topic-html-content-header"
        
    def search(self, keyword:str):
        print(f"Search operation going. Searching : {keyword}")
        return self
    
    def go_to_cart(self):
        print("Cart operation going")
        
        self.click(self.cart_icon)
        return self
    
    def logout(self):
        print("Logout operation going")
        return self
    
    def is_home_page(self) -> bool:
        return self.is_visible(self.search_field)
    
    def is_user_logged_in(self) -> bool:
        return self.is_visible(self.user_avatar)
    
    def get_welcome_text(self) -> str:
        return self.get_text(self.welcome_message)
    
    def get_logged_in_user(self) -> str:
        return self.get_text(self.user_avatar)