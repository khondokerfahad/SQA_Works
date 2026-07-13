from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page : Page):
        self.page = page
    
    def login(self, username:str, password:str):
        self.page.locator("user-name", name="Username").fill("standard_user")
        self.page.locator("password", name="Password").fill("secret_sauce")
        self.page.locator("button", name="Login").click()