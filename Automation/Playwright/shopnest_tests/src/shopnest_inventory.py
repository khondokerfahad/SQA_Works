# src/shopnest_inventory.py - COMPLETE FIXED VERSION (All lowercase 'error')

# Mock "Database" representing our product stock
inventory_db = {
    "product_123": {"name": "Wireless Headphones", "price": 99.99, "stock": 5},
    "product_456": {"name": "USB-C Cable", "price": 19.99, "stock": 0}
}

def check_stock(product_id):
    """Returns the current stock for a product."""
    if product_id in inventory_db:
        return inventory_db[product_id]["stock"]
    return None

def update_inventory(product_id, quantity_change):
    """
    Updates the stock for a product.
    quantity_change: Positive means restocking. Negative means purchasing.
    """
    # Check if product exists
    if product_id not in inventory_db:
        return {"error": "Product not found"}  # ✅ Lowercase 'error'
    
    current_stock = inventory_db[product_id]["stock"]
    new_stock = current_stock + quantity_change
    
    # Check if new stock would be negative
    if new_stock < 0:
        return {"error": f"Insufficient stock. Only {current_stock} available"}  # ✅ Lowercase 'error'
    
    # Update the database
    inventory_db[product_id]["stock"] = new_stock
    
    return {"message": "Inventory updated", "new_stock": new_stock}

def purchase_product_fixed(product_id, quantity):
    """
    FIXED VERSION: Proper validation with error handling.
    """
    # STEP 1: Validate INPUT (quantity must be positive)
    if quantity <= 0:
        return {"error": "Quantity must be greater than 0"}  # ✅ Lowercase 'error'
    
    # STEP 2: Validate product EXISTS (MUST be BEFORE accessing inventory_db[product_id])
    if product_id not in inventory_db:
        return {"error": "Product not found"}  # ✅ Lowercase 'error'
    
    # STEP 3: Get current stock safely (product exists at this point)
    current_stock = inventory_db[product_id]["stock"]
    
    # STEP 4: Check if enough stock is available
    if quantity > current_stock:
        return {"error": f"Insufficient stock. Only {current_stock} available"}  # ✅ Lowercase 'error'
    
    # STEP 5: If all checks pass, update inventory
    result = update_inventory(product_id, -quantity)
    
    # STEP 6: Check if update_inventory returned an error
    if "error" in result:
        return result
    
    # STEP 7: Return success message
    return {"message": "Purchase successful", "new_balance": result["new_stock"]}






# inventory_db = {
#     "product_123" : {"name" : "Wireless Headphones", "price" : 99.99, "stock" : 5},
#     "product_456" : {"name" : "USB-C cable", "price" : 19.99, "stock" : 0}
# }

# def check_stock(product_id):
#     if product_id in inventory_db:
#         return inventory_db[product_id]["stock"]
#     return None

# def update_inventory(product_id, quantity_change):
#     if product_id not in inventory_db:
#         return {"Error" : "Product is not found"}
    
#     current_stock = inventory_db[product_id]["stock"]
#     new_stock = current_stock + quantity_change
    
#     if new_stock < 0:
#         return {"Error" : "Insufficient Stock"}
    
#     inventory_db[product_id]["stock"] = new_stock
#     return {"message": "Inventory updated", "new_stock": new_stock}

# def purchase_product_fixed(product_id, quantity):
#     if quantity <= 0:
#         return {"Error" : {f"Insufficient Stock"}}
    
#     if product_id not in inventory_db:
#         return {"Error" : {"Product not found"}}
    
#     current_stock = inventory_db[product_id]["stock"]
#     if quantity > current_stock:
#         return {"Error" : {f"Insufficient Stock, only available quantity {current_stock}"}}
    
#     # current_stock = inventory_db[product_id]["stock"]
#     result = update_inventory(product_id, -quantity)
    
#     if "Error" in result:
#         return result
    
#     return {"message": "Purchase successful", "new_balance": result["new_stock"]}


