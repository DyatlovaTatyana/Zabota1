from playwright.sync_api import expect
from .base_page import BasePage
import allure

class Login_Page(BasePage):
    def __init__(self,page):
        super().__init__(page)


    @property
    def login(self):
         return self.page.locator('//input[@id="loginform-username"]')

    @property
    def password(self):
         return self.page.locator('//input[@id="loginform-password"]')

    def button(self):
         return self.page.locator('//button[@type="submit"]')

    # def login_input(self):
    #     self.login.fill('biblsoln')
    #
    # def password_input(self):
    #     self.password.fill('Qwerty12345')

    def click_to_button(self):
        self.button().click()
