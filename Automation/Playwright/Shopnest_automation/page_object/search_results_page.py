from page_object.base_page import BasePage

class SearchResultsPage(BasePage):
    """
    Search Results Page Object
    
    Shows products matching the search term
    """
    
    def __init__(self, page):
        super().__init__(page)
        
        # ============================================
        # LOCATORS
        # ============================================
        
        self.product_items = ".product-item"
        self.product_titles = ".product-title"
        self.product_prices = ".prices"
        self.no_results_message = ".no-results"
        
        # Search field (for refining search)
        self.search_field = "#small-searchterms"
        self.search_button = "input[value='Search']"
    
    # ============================================
    # ACTIONS
    # ============================================
    
    def get_product_count(self) -> int:
        """Get number of products in search results"""
        count = self.page.locator(self.product_items).count()
        print(f"📊 Product count: {count}")
        return count
    
    def get_product_names(self) -> list:
        """Get list of product names from results"""
        names = []
        elements = self.page.locator(self.product_titles).all()
        for element in elements:
            names.append(element.text_content().strip())
        return names
    
    def select_product_by_index(self, index: int):
        """
        Select product by position (0 = first)
        
        Why: Sometimes we want the first, second, or third product
        """
        print(f"🔍 Selecting product at index: {index}")
        
        # Check if we have enough products
        total_products = self.get_product_count()
        if total_products == 0:
            raise AssertionError("No products found in search results!")
        
        if index >= total_products:
            raise AssertionError(f"Index {index} out of range! Only {total_products} products found.")
        
        # Click the product
        self.page.locator(self.product_titles).nth(index).click()
        
        # Wait for product page to load
        self.page.wait_for_load_state("networkidle")
        
        # ✅ Import HERE to avoid circular imports
        from page_object.product_page import ProductPage
        return ProductPage(self.page)
    
    def select_product_by_name(self, name: str):
        """Select product by name"""
        print(f"🔍 Selecting product by name: {name}")
        
        product_selector = f".product-title a:has-text('{name}')"
        self.click(product_selector)
        
        # Wait for product page to load
        self.page.wait_for_load_state("networkidle")
        
        # ✅ Import HERE to avoid circular imports
        from page_object.product_page import ProductPage
        return ProductPage(self.page)
    
    def has_results(self) -> bool:
        """Check if there are search results"""
        count = self.get_product_count()
        has_results = count > 0
        print(f"🔍 Has results: {has_results}")
        return has_results
    
    def is_no_results_displayed(self) -> bool:
        """Check if 'no results' message is displayed"""
        return self.is_visible(self.no_results_message)
    
    def refine_search(self, keyword: str):
        """Refine search with new keyword"""
        print(f"🔍 Refining search: {keyword}")
        self.fill(self.search_field, keyword)
        self.click(self.search_button)
        self.page.wait_for_load_state("networkidle")
        return self
    
    def get_first_product_name(self) -> str:
        """Get the name of the first product"""
        if self.get_product_count() > 0:
            return self.page.locator(self.product_titles).first.text_content().strip()
        return None
    
    def get_product_prices(self) -> list:
        """Get list of product prices"""
        prices = []
        elements = self.page.locator(self.product_prices).all()
        for element in elements:
            prices.append(element.text_content().strip())
        return prices