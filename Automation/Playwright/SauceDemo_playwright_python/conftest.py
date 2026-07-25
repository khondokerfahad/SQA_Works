import pytest

base_url = "https://www.saucedemo.com"

@pytest.fixture

def logged_in_page(page):
    page.goto(base_url)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_url("**/inventory.html")
    return page