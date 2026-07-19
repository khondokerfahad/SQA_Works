# tests/test_login.py

import pytest
from playwright.sync_api import Page, Browser
from page_object.base_page import BasePage
from page_object.login_page import LoginPage
from page_object.home_page import HomePage
from data.test_data import TestData

class TestLogin:
    
    
    @pytest.fixture(scope="function")
    def page(self, browser: Browser) -> Page:
        
        page = browser.new_page()
        page.goto(TestData.login_url)
        yield page
        page.close()
        print("Page closed")
    
    def test_valid_login(self, page: Page):
        
        print("\nValid Login Test")
        
        login_page = LoginPage(page)
        
        email = TestData.valid_user["email"]
        password = TestData.valid_user["password"]
        
        print(f"Logging in with: {email}")
        
        home_page = login_page.login(email, password)
        
        assert home_page.is_home_page(), "Should be on home page"
        print("Verified: On home page")
        
        assert home_page.is_user_logged_in(), "User should be logged in"
        print("User is logged in")
        
        print("Valid login works!")
    
    def test_invalid_login(self, page: Page):
       
        print("\nInvalid Login Test")
        
        login_page = LoginPage(page)
        print("Login page object created")
        
        email = TestData.invalid_user["email"]
        password = TestData.invalid_user["password"]
        
        print(f"Attempting login with: {email}")
        
        login_page.login(email, password)
        
        assert login_page.is_error_displayed(), "Error should be displayed"
        print("Error is displayed")
        
        error_message = login_page.get_error_message()
        assert "Login was unsuccessful" in error_message
        print(f"Error message: '{error_message}'")
        
        assert login_page.is_login_page(), "Should still be on login page"
        print("Still on login page")
        
        print("Invalid login shows error!")