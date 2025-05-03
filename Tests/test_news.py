import allure
import pytest
from playwright.sync_api import Page
from Pages.alt_page import AltPage
from Pages.news_page import NewsPage
from Pages.news_card import NewsCard
from Consts.link import Links


@pytest.mark.usefixtures("browser")
class TestNews:
    @allure.title("Открытие новостей с АлтынЕллар")
    def test_open_news(self, browser: Page):
        alt_page = AltPage(browser)
        news_page = NewsPage(browser)
        alt_page.open(Links.ALTELL)
        alt_page.check_button_look_all_exists()
        alt_page.click_button_look_all_exists()
        news_page.check_tags_block()

    @allure.title("Применение фильтров из блока популярных тем")
    def test_tag_from_popular(self, browser: Page):
        news_page = NewsPage(browser)
        news_page.open(Links.NEWS_PAGE)
        news_page.click_to_tag()
        print(news_page.text_title())
        news_page.check_text_title()

    @allure.title("Применение фильтров из карточки новости")
    def test_tag_from_newscard(self, browser: Page):
        news_page = NewsPage(browser)
        news_card = NewsCard(browser)
        news_card.open(Links.NEWS_CARD)
        news_card.click_to_tag()
        news_page.check_tags_block(False)

    @allure.title("Переход на страницу с несущ id новости. Отображается 404 ошибка")
    def test_non_exist_news(self, browser: Page):
        news_card = NewsCard(browser)
        news_card.open(Links.NON_EXIST_NEWS_CARD)
        news_card.check_not_found_block()
