"""
WebDriver Factory - Sets up and configures Selenium WebDriver
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Update this with your test website URL
BASE_URL = "https://parabank.parasoft.com/parabank/index.htm"


def get_driver(headless=False):
    """
    Creates and returns a configured Chrome WebDriver instance.
    
    Args:
        headless (bool): Run browser in headless mode (no GUI)
    
    Returns:
        WebDriver: Configured Chrome WebDriver instance
    """
    chrome_options = Options()
    
    if headless:
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Additional options for stability
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
    # Auto-download and setup ChromeDriver
    service = Service(ChromeDriverManager().install())
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)  # Wait up to 10 seconds for elements
    
    return driver
