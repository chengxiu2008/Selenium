# tests/test_login.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from conf.conf import *
import time

def test_login_success():
    driver = webdriver.Chrome(service=Service(CHROMEDRIVER))
    driver.get(WEBPAGE)

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    time.sleep(2)
    assert "inventory" in driver.current_url  # Verify login worked
    driver.quit()