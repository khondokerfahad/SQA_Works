from page_object.base_page import BasePage

class LoginPage(BasePage):
    
    def __init__(self, page):
        super().__init__(page)
        
        self.email_field = "#Email"
        self.password_field = "#Password"
        self.login_button = "input[value='Log in']"
        self.error_summary = ".validation-summary-errors"
        self.field_error = ".field-validation-error"
        self.register_link = "a:has-text('Register')"
        self.remember_me = "#RememberMe"
    
    def login(self, email: str, password: str):
        """Complete login flow"""
        print(f"🔐 Login with email : {email}")
        
        self.fill(self.email_field, email)
        self.fill(self.password_field, password)
        self.click(self.login_button)
        
        self.page.wait_for_load_state("networkidle")
        
        # Check if login succeeded
        if self.is_visible("#small-searchterms") or self.is_visible(".account"):
            print("✅ Login successful!")
            
            from page_object.home_page import HomePage
            return HomePage(self.page)
        
        # Check for error
        if self.is_error_displayed():
            error = self.get_error_message()
            print(f"❌ Login failed: {error}")
            raise AssertionError(f"Login failed: {error}")
        
        # If we're still on login page
        if "login" in self.page.url:
            raise AssertionError("Login failed - still on login page")
        
        # Fallback
        from page_object.home_page import HomePage
        return HomePage(self.page)
    
    def is_error_displayed(self) -> bool:
        """Check if error is displayed"""
        return self.is_visible(self.error_summary) or self.is_visible(self.field_error)
    
    def get_error_message(self) -> str:
        """Get error message text"""
        if self.is_visible(self.error_summary):
            return self.get_text(self.error_summary)
        if self.is_visible(self.field_error):
            return self.get_text(self.field_error)
        return "No error message found"
    
    def is_login_page(self) -> bool:
        """Verify we're on the login page"""
        return self.is_visible(self.email_field)