# For Async api

# import asyncio
# from playwright.async_api import async_playwright

# async def main():
#     async with async_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = await browser.new_page()
#         await page.goto('https://google.com')
#         print(await page.title())
#         await browser.close()

# asyncio.run(main())

from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        
        print("Opening Google .....")
        page.goto("https://google.com/ncr")
        
        page.get_by_role("combobox").fill("Playwright Python")
        page.keyboard.press("Enter")
        
        page.wait_for_timeout(3000)
        page.screenshot(path="google.png")
        
        print("Test Complete .......")
        
if __name__ == "__main__":
    main()
    
    