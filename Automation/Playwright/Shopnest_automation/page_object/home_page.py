from page_object.base_page import BasePage

class HomePage(BasePage):
    
    def __init__(self, page):
        super().__init__(page)
        
        self.search_field = "#small-searchterms"
        self.search_button = "input[value='Search']"
        self.cart_icon = ".cart-label"
        self.account_link = ".account"
        self.logout_link = "a:has-text('Log out')"
        self.welcome_message = ".topic-html-content-header"
        self.product_cards = ".product-item"
    
    def is_home_page(self) -> bool:
        """Verify we're on the home page"""
        self.page.wait_for_timeout(1000)
        return self.is_visible(self.search_field)
    
    def is_user_logged_in(self) -> bool:
        """Check if user is logged in"""
        return self.is_visible(self.account_link)
    
    def search(self, keyword: str):
        """Search for a product"""
        print(f"🔍 Searching for: {keyword}")
        self.fill(self.search_field, keyword)
        self.click(self.search_button)
        self.page.wait_for_load_state("networkidle")
        from page_object.search_results_page import SearchResultsPage
        return SearchResultsPage(self.page)
    
    def go_to_cart(self):
        """Navigate to cart"""
        print("🛒 Going to cart")
        self.click(self.cart_icon)
        from page_object.cart_page import CartPage
        return CartPage(self.page)
    
    def logout(self):
        """Logout from application"""
        print("🚪 Logging out")
        self.click(self.logout_link)
        return self