import pytest

def test_simple():
    """Simple test to verify pytest is working"""
    assert 1 + 1 == 2
    print("✅ Basic test passed!")

def test_string():
    """Another simple test"""
    assert "hello".upper() == "HELLO"
    print("✅ String test passed!")