from playwright.sync_api import expect
from .base_page import BasePage
import allure

class NewsPage(BasePage):
    def __init__(self,page):
        super().__init__(page)


    @property
    def tags_block(self):
         return self.page.locator('//div[@class="news-tags-list_tags__KVfgf"]')

    def title_block(self):
        return self.page.locator('//h2[@class="page-heading-title_page_heading__title___WsFU"]')

    def tag(self):
        return self.page.locator('//*[@class="news-tags-list_tags__list__Ua_I4"]//li[4]')

    def text_title(self):
        element = self.title_block()
        return element.text_content()


    def check_text_title(self):
        expect(self.title_block()).to_contain_text("последние новости")

    def check_tags_block(self, isvisible=True):
        expect(self.tags_block).to_be_visible(visible=isvisible)

    def check_title_block(self, isvisible=True):
        expect(self.title_block).to_be_visible(visible=isvisible)

    @allure.step("Клик по тегу из блока популярных тем")
    def click_to_tag(self):
        self.tag().click()

    # def check_text_title(self):
    #     element = self.title_block()
    #     return element.text_content()
