"""
Base Page - Parent class for all page objects
Contains common methods used across all pages
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Base class for all page objects"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def navigate_to(self, url):
        """Navigate to a specific URL"""
        self.driver.get(url)
    
    def find_element(self, locator):
        """Find a single element with explicit wait"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator):
        """Find multiple elements"""
        return self.driver.find_elements(*locator)
    
    def click(self, locator):
        """Click an element after waiting for it to be clickable"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def enter_text(self, locator, text):
        """Clear and enter text into an input field"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Get text from an element"""
        element = self.find_element(locator)
        return element.text
    
    def is_element_visible(self, locator, timeout=10):
        """Check if element is visible within timeout"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def get_current_url(self):
        """Get the current page URL"""
        return self.driver.current_url
    
    def get_page_title(self):
        """Get the current page title"""
        return self.driver.title
