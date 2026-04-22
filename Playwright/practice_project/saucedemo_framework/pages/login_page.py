from pages.base_page import BasePage

class LoginPage(BasePage):
    def login(self, username, password):
        self.username = "standard_user"
        self.password = "secret_sauce"
        self.page.locator("#user-name").fill(username)
        self.page.locator("#password").fill(password)
        self.page.locator("#login-button").click()
        print("✅ Login successful")