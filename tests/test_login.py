# File: tests/test_login.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


def test_login_success():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Tell Selenium exactly where chromedriver is (important for GitHub Actions)
    service = Service("/usr/local/bin/chromedriver")

    # Launch the browser
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Go to the test site
    driver.get("https://www.saucedemo.com/")

    # Find username and password fields, fill them
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")

    # Click the login button
    driver.find_element("id", "login-button").click()

    # Wait a little (not best practice, but ok for demo)
    time.sleep(2)

    # Verify we're logged in by checking presence of the Products page
    assert "inventory.html" in driver.current_url

    # Close browser
    driver.quit()
