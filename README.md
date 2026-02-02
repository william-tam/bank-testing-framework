# Bank Website Testing Framework

A Selenium-based testing framework for automated testing of bank website functionality.

## Project Structure

```
bank-testing-framework/
├── tests/                  # Test files
│   ├── __init__.py
│   └── test_login.py      # Example login test
├── pages/                  # Page Object Models
│   ├── __init__.py
│   ├── base_page.py       # Base page class
│   └── login_page.py      # Login page object
├── utils/                  # Utility functions
│   ├── __init__.py
│   └── driver_factory.py  # WebDriver setup
├── requirements.txt        # Python dependencies
├── pytest.ini             # Pytest configuration
├── Dockerfile             # Docker container setup
├── .github/
│   └── workflows/
│       └── test.yml       # GitHub Actions CI/CD
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.9+
- Chrome browser
- Git

### Local Setup

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd bank-testing-framework
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run tests locally**
```bash
pytest tests/ -v
```

### Using Docker

1. **Build the Docker image**
```bash
docker build -t bank-tests .
```

2. **Run tests in Docker**
```bash
docker run --rm bank-tests
```

### CI/CD with GitHub Actions

Tests automatically run on:
- Every push to main branch
- Every pull request

View results in the "Actions" tab of your GitHub repository.

## Writing Tests

Tests use the Page Object Model pattern. Here's a simple example:

```python
def test_login_page_loads(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    assert login_page.is_loaded()
```

## Configuration

- **Test URL**: Update `BASE_URL` in `utils/driver_factory.py`
- **Browser**: Change browser type in `driver_factory.py` (Chrome/Firefox)
- **Timeouts**: Adjust in `base_page.py`

## Next Steps

1. Update the `BASE_URL` in `utils/driver_factory.py` with your test website
2. Add more page objects in `pages/` for different pages
3. Write tests in `tests/` using your page objects
4. Run locally first, then try Docker, then push to GitHub

## Troubleshooting

**ChromeDriver issues?**
- The framework uses webdriver-manager to auto-download drivers
- Make sure Chrome browser is installed

**Tests failing in Docker?**
- Docker uses headless mode by default
- Check logs with `docker run --rm bank-tests`

## Resources

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Page Object Model Pattern](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
