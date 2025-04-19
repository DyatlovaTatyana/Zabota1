from playwright.sync_api import expect
from .base_page import BasePage
import allure

class Home_Page(BasePage):
    def __init__(self,page):
        super().__init__(page)


    @property
    def altellar(self):
         return self.page.locator("text=Алтын Еллар")

    def active(self):
         return self.page.locator('//a[@href="/active"]')

    def button(self):
        return self.page.locator('//a[@class="btn btn-success"]')

    def delete_button(self):
        return self.page.locator('//tbody[1]//tr[1]//a[@data-method="post"]')

    @allure.step("Клик по разделу Алтын Еллар")
    def click_to_ae(self):
        # expect(self.altellar.first).to_be_visible()
        # #прописать ожидание
        # # self.page.wait_for_selector(self.altellar, state='attached')
        # self.altellar.first.wait_for(state='visible')
        self.altellar.first.click()

    @allure.step("Клик по разделу Занятия")
    def click_to_active(self):
        self.active().click()

    @allure.step("Клик по создать занятие")
    def click_to_button(self):
        self.button().click()

    @allure.step("Клик по удалению занятия")
    def click_to_delete_button(self):
        self.delete_button().click()

