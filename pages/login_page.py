"""
Login Page Object - Represents the login page of the bank website
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.driver_factory import BASE_URL
import time

class LoginPage(BasePage):
    """Page object for the login page"""
    
    # Locators - Update these based on your actual website's HTML
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "button")
    HOME_PAGE = (By.ID, "loginPanel")
    ERROR_MESSAGE = (By.CLASS_NAME, "error")
    LOGO = (By.CLASS_NAME, "logo")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{BASE_URL}"
    
    def navigate(self):
        """Navigate to the login page"""
        self.navigate_to(self.url)
    
    def is_loaded(self):
        """Check if login page is properly loaded"""
        return self.is_element_visible(self.HOME_PAGE)
    
    def enter_username(self, username):
        """Enter username into the username field"""
        self.enter_text(self.USERNAME_INPUT, username)
    
    def enter_password(self, password):
        """Enter password into the password field"""
        self.enter_text(self.PASSWORD_INPUT, password)
    
    def click_login(self):
        """Click the login button"""
        self.click(self.LOGIN_BUTTON)       
    
    def login(self, username, password):
        """Complete login flow"""
        self.enter_username(username)
        self.enter_password(password)
        time.sleep(3)
        self.click_login()
    
    def get_error_message(self):
        """Get error message text if present"""
        if self.is_element_visible(self.ERROR_MESSAGE, timeout=3):
            return self.get_text(self.ERROR_MESSAGE)
        return None
    
    def is_logo_visible(self):
        """Check if bank logo is visible"""
        return self.is_element_visible(self.LOGO)
