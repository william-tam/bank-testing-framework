"""
Login Tests - Tests for the login functionality
"""
import pytest
from pages.login_page import LoginPage
import time

@pytest.mark.smoke
def test_login_page_loads(driver):
    """Test that the login page loads successfully"""
    login_page = LoginPage(driver)
    login_page.navigate()
    time.sleep(2    )
    
    assert login_page.is_loaded(), "Login page did not load properly"

@pytest.mark.smoke
def test_logo_visible_on_login_page(driver):
    """Test that the bank logo is visible on login page"""
    login_page = LoginPage(driver)
    login_page.navigate()
    
    assert login_page.is_logo_visible(), "Bank logo is not visible on login page"


@pytest.mark.login
def test_login_with_valid_credentials(driver):
    """Test login with valid credentials"""
    login_page = LoginPage(driver)
    login_page.navigate()
    
    # Update these with valid test credentials for your test site
    login_page.login(username="testuser", password="testpass123")
    
    # Add assertion based on successful login behavior
    # Example: Check if redirected to dashboard
    # assert "dashboard" in login_page.get_current_url().lower()


# @pytest.mark.login
# def test_login_with_invalid_credentials(driver):
#     """Test login with invalid credentials shows error"""
#     login_page = LoginPage(driver)
#     login_page.navigate()
    
#     login_page.login(username="bleh", password="blah")
    
#     # Check for error message
#     error_message = login_page.get_error_message()
#     print(error_message)
#     time.sleep(3)
#     assert error_message is not None, "No error message displayed for invalid credentials"


@pytest.mark.login
def test_login_with_empty_username(driver):
    """Test that login fails with empty username"""
    login_page = LoginPage(driver)
    login_page.navigate()
    
    login_page.enter_password("somepassword")
    login_page.click_login()
    
    # Should still be on login page or show error
    assert login_page.is_loaded(), "Should remain on login page with empty username"


@pytest.mark.login
def test_login_with_empty_password(driver):
    """Test that login fails with empty password"""
    login_page = LoginPage(driver)
    login_page.navigate()
    
    login_page.enter_username("testuser")
    login_page.click_login()
    
    # Should still be on login page or show error
    assert login_page.is_loaded(), "Should remain on login page with empty password"
