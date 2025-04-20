import allure
import pytest
from playwright.sync_api import Page
from Pages.login_page import Login_Page
from Pages.home_admin import Home_Page
from Pages.active_page import Active_Page
from Pages.steps import Steps
from Consts.link import Links
from playwright.sync_api import expect


@pytest.mark.usefixtures("browser")

class TestActive:
    @pytest.mark.parametrize(
        'login, password',
        [
            ('biblsoln', 'Qwerty12345'),
            ('swimsoln', 'Qwerty1234')

        ]
    )
    @allure.title("Залогиниться в системе")
    def test_login(self, browser: Page, login, password):
        steps=Steps(browser)
        steps.login_admin(login, password)
        expect(browser).to_have_url(Links.HOST_ADMIN) #Ок ли так прописывать проверку или лучше как в след тесте?

    @allure.title("Переход на страницу создания занятия")
    def test_go_to_active(self, browser: Page):
        home_page = Home_Page(browser)
        steps = Steps(browser)
        steps.login_admin()
        home_page.click_to_ae()
        home_page.click_to_active()
        home_page.click_to_button()
        browser.wait_for_load_state('networkidle')
        expect(browser).to_have_url("https://zabotaservice.ru/active/create")


    @allure.title("Создание занятия")
    def test_create_active(self, browser: Page):
        home_page = Home_Page(browser)
        steps = Steps(browser)
        steps.login_admin()
        home_page.click_to_ae()
        home_page.click_to_active()
        home_page.click_to_button()
        steps.create_active()
        expect(browser).to_have_url("https://zabotaservice.ru/active") #Как тут прописать ссылаясь на links
        #Можно тут прописать удаление сразу? или лучше отдельным тестом
        # home_page.click_to_delete_button()