# pages/login_page.py
from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def login(self, username, password):
        self.type(*self.username_input, text=username) # to split a tuple into individual arguments.
        self.type(*self.password_input, text=password)
        self.click(*self.login_button)