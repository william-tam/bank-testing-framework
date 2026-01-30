# Bank site testing framework
A Selenium based testing framework that automates the testing of a fake website called Parabank. It ensures all essential APIs of the site works as intended, such as sending/receiving bank statements.

# Project structure
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

## Getting Started
## Prerequisites
Python 3.9+
Chrome Browser
Git

## Local setup
1. Clone the repository

git clone https://github.com/william-tam/bank-testing-framework.git
cd bank-testing-framework

Create virtual environment

bashpython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies

bashpip install -r requirements.txt

Run tests locally

bashpytest tests/ -v
Using Docker

Build the Docker image

bashdocker build -t bank-tests .

Run tests in Docker

bashdocker run --rm bank-tests
CI/CD with GitHub Actions
Tests automatically run on:

Every push to main branch
Every pull request

View results in the "Actions" tab of your GitHub repository.