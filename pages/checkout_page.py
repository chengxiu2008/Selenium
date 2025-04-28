from selenium.webdriver.common.by import By
from base.base_page import BasePage

class CheckoutPage(BasePage):
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    finish_button = (By.ID, "finish")

    def fill_form(self, fname, lname, zip_code):
        self.type(*self.first_name, fname)
        self.type(*self.last_name, lname)
        self.type(*self.postal_code, zip_code)
        self.click(*self.continue_button)

    def complete_order(self):
        self.click(*self.finish_button)