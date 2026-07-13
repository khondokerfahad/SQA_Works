import pytest 
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from src.shopnest_inventory import purchase_product_fixed, check_stock, inventory_db

class TestInventorymanagement:
    @pytest.fixture
    def reset_inventory(self):
        inventory_db["product_123"] = {"name": "Wireless Headphones", "price": 99.99, "stock": 5}
        inventory_db["product_456"] = {"name": "USB-C Cable", "price": 19.99, "stock": 0}
        
        yield
        
    # Test 1: Normal purchase
    def test_normal_purchase_success(self, reset_inventory):
        """TC001: Verify successful purchase with sufficient stock"""
        result = purchase_product_fixed("product_123", 2)
        assert result["message"] == "Purchase successful"
        assert result["new_balance"] == 3
        assert check_stock("product_123") == 3
        print("---------------TC001 PASSED---------------")
        
    # Test 2: Purchase exact stock
    def test_purchase_exact_stock(self, reset_inventory):
        """TC002: Verify purchase of exactly available stock"""
        result = purchase_product_fixed("product_123", 5)
        assert result["message"] == "Purchase successful"
        assert result["new_balance"] == 0
        assert check_stock("product_123") == 0
        print("---------------TC002 PASSED---------------")
        
     # Test 3: Overselling fails
    def test_overselling_fails(self, reset_inventory):
        """TC003: Verify overselling is prevented"""
        result = purchase_product_fixed("product_123", 10)
        assert "error" in result
        assert "Insufficient stock" in result["error"]
        assert check_stock("product_123") == 5  # Stock unchanged
        print("---------------TC003 PASSED---------------")
    
    # Test 4: Negative quantity prevented
    def test_negative_quantity_prevented(self, reset_inventory):
        """TC004: Verify negative quantity is rejected"""
        result = purchase_product_fixed("product_123", -2)
        assert "error" in result
        assert "Quantity must be greater than 0" in result["error"]
        assert check_stock("product_123") == 5  # Stock unchanged
        print("---------------TC004 PASSED---------------")
    
    # Test 5: Zero quantity prevented
    def test_zero_quantity_prevented(self, reset_inventory):
        """TC005: Verify zero quantity is rejected"""
        result = purchase_product_fixed("product_123", 0)
        assert "error" in result
        assert "Quantity must be greater than 0" in result["error"]
        print("---------------TC005 PASSED---------------")
    
    # Test 6: Out of stock prevented
    def test_out_of_stock_prevented(self, reset_inventory):
        """TC006: Verify purchasing out-of-stock item is prevented"""
        result = purchase_product_fixed("product_456", 1)
        assert "error" in result
        assert "Insufficient stock" in result["error"]
        assert check_stock("product_456") == 0
        print("---------------TC006 PASSED---------------")
    
    # Test 7: Non-existent product
    def test_non_existent_product(self, reset_inventory):
        """TC007: Verify handling of non-existent product"""
        result = purchase_product_fixed("product_999", 1)
        assert "error" in result
        assert "Product not found" in result["error"]
        print("---------------TC007 PASSED---------------")
    
    # Test 8: Large quantity
    def test_large_quantity_integer(self, reset_inventory):
        """TC008: Verify handling of very large quantity"""
        result = purchase_product_fixed("product_123", 999999)
        assert "error" in result
        assert check_stock("product_123") == 5  # Stock unchanged
        print("---------------TC008 PASSED---------------")
    
    # Test 9: Multiple purchases
    def test_stock_accuracy_after_multiple_purchases(self, reset_inventory):
        """TC009: Verify stock accuracy after sequential purchases"""
        # Buy 2
        result1 = purchase_product_fixed("product_123", 2)
        assert result1["message"] == "Purchase successful"
        
        # Buy 2 more
        result2 = purchase_product_fixed("product_123", 2)
        assert result2["message"] == "Purchase successful"
        
        # Buy 1 more
        result3 = purchase_product_fixed("product_123", 1)
        assert result3["message"] == "Purchase successful"
        
        # Final stock should be 0
        assert check_stock("product_123") == 0
        print("---------------TC009 PASSED---------------")
    
    # Test 10: Atomicity - failed purchase doesn't change stock
    def test_insufficient_stock_does_not_modify_inventory(self, reset_inventory):
        """TC010: Verify stock doesn't change on failed purchase"""
        initial_stock = check_stock("product_123")
        
        # Attempt failed purchase
        result = purchase_product_fixed("product_123", 10)
        final_stock = check_stock("product_123")
        
        assert "error" in result
        assert final_stock == initial_stock  # Critical: Stock unchanged
        print("---------------TC010 PASSED---------------")