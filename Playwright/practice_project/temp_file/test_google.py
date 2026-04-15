import re
# import pytest
from playwright.sync_api import expect , Page

def test_google_search():
    page.wait_for_timeout(3000)
    page.goto("https://google.com/ncr")
    
    page.get_by_role("combobox", name="Search").fill("Playwright Automation")
    
    page.keyboard.press("Enter")
    
    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))
    
    