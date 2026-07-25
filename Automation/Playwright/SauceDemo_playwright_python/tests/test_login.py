import pytest
from pages.login_page import LoginPage

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    page.wait_for_url("**/inventory.html")
    assert "inventory.html" in page.url
    
def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user1", "secret_sauce")
    assert login_page.error_message.is_visible()
    assert "Username and password do not match any user in this service" in login_page.error_message.inner_text()
    
def test_locked_user(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("locked_out_user", "secret_sauce")
    assert login_page.error_message.is_visible()
    assert "Sorry, this user has been locked out." in login_page.error_message.inner_text()
    
def test_blank_user_login(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("", "secret_sauce")
    assert login_page.error_message.is_visible()
    assert "Username is required" in login_page.error_message.inner_text()
    
def test_blank_password_login(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "")
    assert login_page.error_message.is_visible()
    assert "Password is required" in login_page.error_message.inner_text()
    