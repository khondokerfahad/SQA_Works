from page_object.base_page import BasePage
from page_object.home_page import HomePage

class login_page(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
        self.email_field = "#Email"
        self.password_field = "#Password"
        self.remember_checkbox = "#RememberMe"
        self.login_button = "input[value='Log in']"
        
        self.register_button = "input[value='Register']"
        self.error_message = ".field-validation-error"
        
    def login(self, email:str, password:str) -> HomePage:
        print(f"Login with email : {email}")
        
        self.fill(self.email_field, email)
        self.fill(self.password_field, password)
        self.click(self.remember_checkbox)
        self.click(self.login_button)
        
        print("---------------Login successful---------------")
        return HomePage(self.page)
    
    def get_error_message(self) -> str:
        return self.get_text(self.error_message)
    
    def is_error_displayed(self) -> bool:
        return self.get_text(self.error_message)
    
    def is_login_page(self) -> bool:
        return self.is_visible(self.email_field)