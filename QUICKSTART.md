# Quick Start Guide 🚀

Welcome! This guide will get you up and running in 10 minutes.

## Step 1: Update the Test URL (2 min)

Open `utils/driver_factory.py` and update this line:
```python
BASE_URL = "https://your-bank-test-site.com"  # Change this!
```

## Step 2: Update Page Locators (5 min)

1. Open the bank website in Chrome
2. Right-click on the username field → Inspect
3. Look for `id=` or `class=` in the HTML
4. Open `pages/login_page.py` and update these locators:

```python
USERNAME_INPUT = (By.ID, "username")  # Update with actual ID
PASSWORD_INPUT = (By.ID, "password")  # Update with actual ID
LOGIN_BUTTON = (By.ID, "login-button")  # Update with actual ID
```

**Finding locators tips:**
- `By.ID` - Use if element has `id="something"`
- `By.CLASS_NAME` - Use if element has `class="something"`
- `By.CSS_SELECTOR` - Use for more complex selectors
- `By.XPATH` - Use as last resort

## Step 3: Run Your First Test (3 min)

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/test_login.py -v
```

You should see output like:
```
tests/test_login.py::test_login_page_loads PASSED
tests/test_login.py::test_logo_visible_on_login_page PASSED
```

## What's Next?

### Add More Page Objects
Create new files in `pages/` for other pages:
- `dashboard_page.py` - For the main dashboard
- `transfer_page.py` - For money transfers
- `account_page.py` - For account details

### Write More Tests
Add test files in `tests/`:
- `test_dashboard.py`
- `test_transfer.py`
- `test_account.py`

### Try Docker
```bash
docker build -t bank-tests .
docker run --rm bank-tests
```

### Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-repo-url>
git push -u origin main
```

The GitHub Action will run automatically!

## Common Issues

**"Element not found" error?**
- Check your locators are correct
- Add `time.sleep(2)` before the failing line to see what's happening

**ChromeDriver error?**
- Make sure Chrome browser is installed
- Try: `pip install --upgrade webdriver-manager`

**Tests pass locally but fail in Docker?**
- Timing issues - add more waits
- Check if headless mode causes different behavior

## Need Help?

- Check `README.md` for detailed documentation
- Look at example tests in `tests/test_login.py`
- Review page object pattern in `pages/login_page.py`
