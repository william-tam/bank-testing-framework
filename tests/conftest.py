"""
Pytest configuration and fixtures
"""
import pytest
from utils.driver_factory import get_driver
import os


@pytest.fixture(scope="function")
def driver():
    """
    Pytest fixture that creates a WebDriver instance for each test.
    Automatically closes the browser after the test completes.
    """
    # Check if running in CI environment (GitHub Actions)
    is_ci = os.getenv("CI", "false").lower() == "true"
    
    # Use headless mode in CI, regular mode locally
    driver_instance = get_driver(headless=is_ci)
    
    yield driver_instance
    
    # Cleanup: close browser after test
    driver_instance.quit()


@pytest.fixture(scope="function")
def headless_driver():
    """
    Fixture for tests that specifically need headless mode.
    """
    driver_instance = get_driver(headless=True)
    
    yield driver_instance
    
    driver_instance.quit()
