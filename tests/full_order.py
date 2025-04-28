from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.assertions import assert_text_contains
from conf.conf import *
from base.base_page import *
from pages.product_page import ProductPage
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service("/usr/local/bin/chromedriver")

import time
from selenium.webdriver.common.by import By

def test_order_checkout():
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(WEBPAGE)

    # Login
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    # Add one item
    product = ProductPage(driver)
    product.add_first_product_to_cart()
    product.go_to_cart()
    time.sleep(3)

    # Cart Page
    cart = CartPage(driver)
    cart_items = cart.get_cart_items()
    assert len(cart_items) == 1
    cart.proceed_to_checkout()
    time.sleep(3)

    # Checkout Page
    checkout = CheckoutPage(driver)
    checkout.fill_form("Cathy", "Wu", "12345")
    checkout.complete_order()
    time.sleep(3)

    assert_text_contains(driver.page_source, "Thank you for your order")

    time.sleep(2)
    driver.quit()