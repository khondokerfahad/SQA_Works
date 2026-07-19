class TestData:
    
    # login_url = "https://demowebshop.tricentis.com/login"
    base_url = "https://demowebshop.tricentis.com/"
    login_url = base_url + "login"
    register_url = base_url + "register"
    cart_url = base_url + "cart"

    valid_user = {
        "email" : "wrkhmx4567@minitts.net",
        "password" : "valid_test_password_123",
        "first_name" : "test_fname",
        "last_name" : "test_lname"
    }
    
    wrong_mail_user = {
        "email" : "wrongmail@test.com",
        "password" : "valid_test_password_123"
    }
    
    wrong_pass_user = {
        "email" : "wrkhmx4567@minitts.net",
        "password" : "invalid_test_password_123"
    }
    
    invalid_user = {
        "email" : "wrongemail@test.com",
        "password" : "invalid_test_password_123"
    }
    
    empty_user = {
        "email" : "",
        "password" : ""
    }
    
    empty_email_user = {
        "email" : "",
        "password" : "valid_test_password_123"
    }
    
    empty_pass_user = {
        "email" : "wrkhmx4567@minitts.net",
        "password" : ""
    }
    
    ERROR_MESSAGES = {
        "login_failed": "Login was unsuccessful",
        "invalid_credentials": "No customer account found",
        "email_required": "Please enter your email",
        "password_required": "Please enter your password",
        "required_fields": "This field is required"
    }
    
    test_products = {
        "electronics" : "laptop",
        "books" : "fiction",
        "clothing" : "shirts"
    }
    