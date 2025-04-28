from selenium.webdriver.common.by import By
from base.base_page import BasePage

class ProductPage(BasePage):
    add_to_cart_buttons = (By.CLASS_NAME, "btn_inventory")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_first_product_to_cart(self):
        self.find_elements(*self.add_to_cart_buttons)[0].click()

    def go_to_cart(self):
        self.find(*self.cart_icon).click()