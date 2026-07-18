from playwright.sync_api import Page

class BasePage:
    def __init__(self, page:Page):
        self.page = page
    
    def click(self, selector:str):
        self.page.locator(selector).click()
        return self
    
    def fill(self, selector:str, text:str):
        self.page.locator(selector).fill(text)
        return self
    
    def get_text(self, selector:str) -> str:
        return self.page.locator(selector).text_content()
    
    def is_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()
    
