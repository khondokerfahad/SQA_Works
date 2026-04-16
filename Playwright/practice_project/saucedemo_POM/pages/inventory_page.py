from playwright.sync_api import Page, exoect

class InventoryPage:
    def __init__(self, page : Page):
        self.page = page
    
    def add_product_to_cart(self, product_name):
        # print("What product do you like to add in cart ?")
        # product_dict = {"Sauce Labs Backpack":"#add-to-cart-sauce-labs-backpack", 
        #                 "Sauce Labs Bike Light":"#add-to-cart-sauce-labs-bike-light",
        #                 "Sauce Labs Bolt T-Shirt":"#add-to-cart-sauce-labs-bolt-t-shirt",
        #                 "Sauce Labs Fleece Jacket":"#add-to-cart-sauce-labs-fleece-jacket",
        #                 "Sauce Labs Onesie":"#add-to-cart-sauce-labs-onesie",
        #                 "Test.allTheThings() T-Shirt (Red)":"button[id='add-to-cart-test.allthethings()-t-shirt-(red)']"}
        # self.page.locator(f"#add-to-cart-sauce-labs-").click()
        # self.page.locator("#add-to-cart-{product_name}.lower().replace(' ', '-')").click()
        if product_name == "Sauce Labs Backpack":
            self.page.locator("#add-to-cart-sauce-labs-backpack").click()
        elif product_name == "Sauce Labs Bike Light":
            self.page.locator("#add-to-cart-sauce-labs-bike-light").click()
        elif product_name == "Sauce Labs Bolt T-Shirt":
            self.page.locator("#add-to-cart-sauce-labs-bolt-t-shirt").click()
        elif product_name == "Sauce Labs Fleece Jacket":
            self.page.locator("#add-to-cart-sauce-labs-fleece-jacket").click()
        elif product_name == "Sauce Labs Onesie":
            self.page.locator("#add-to-cart-sauce-labs-onesie").click()
        elif product_name == "Test.allTheThings() T-Shirt (Red)":
            self.page.locator("button[id='add-to-cart-test.allthethings()-t-shirt-(red)']").click()
        else:
            self.page.get_by_role("button", name = "Add to Cart").first.click()
            
        print(f"✅ Added product : {product_name} to cart")
         
        
    def go_to_cart(self):
        self.page.locator(".shopping_cart_link").click()
        print(f"✅ Opend Shopping cart")