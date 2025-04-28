from selenium.webdriver.common.by import By
from base.base_page import BasePage

class CartPage(BasePage):
    checkout_button = (By.ID, 'checkout')
    item_names = (By.CLASS_NAME, 'inventory_item_name')

    def get_cart_items(self):
        return [e.text for e in self.find_elements(*self.item_names)]

    def proceed_to_checkout(self):
        self.click(*self.checkout_button)
