from pathlib import Path

from playwright.sync_api import expect

from Consts.common import ROOT_DIR
from .base_page import BasePage
import allure

class Active_Page(BasePage):
    def __init__(self,page):
        super().__init__(page)


    @property
    def active_title(self):
        return self.page.locator('//input[@id="activelongwrite-title"]')


    def active_category(self):
        return self.page.locator('//span[@id="select2-activelongwrite-active_category_id-container"]')
    def active_category_select(self):
        return self.page.locator('//ul[@class="select2-results__options"]//li[2]')


    def active_sub_category(self):
        return self.page.locator('//input[@class="select2-search__field"]')
    def active_sub_category_select(self):
        return self.page.locator('//ul[@class="select2-results__options"]//li[1]')


    def active_type(self):
        return self.page.locator('//span[@id="select2-activelongwrite-registration_type_id-container"]')
    def active_type_select(self,text="По записи"):
        return self.page.locator(f'//li[text()="{text}"]')


    def active_descriptoin(self):
        return self.page.locator('//textarea[@id="activelongwrite-description"]')

    def teacher_name(self):
        return self.page.locator('//input[@id="activelongwrite-teacher"]')

    def teacher_descriptoin(self):
        return self.page.locator('//textarea[@id="activelongwrite-teacher_description"]')

    def input_image(self):
        return self.page.locator('//input[@id="w2"]')

    def upload_image(self):
        return self.page.locator('//div[@id="main-image-container"]//a[@href="/active/upload-image"]')


    def schedule_from(self):
        return self.page.locator('//input[@id="activelongwrite-active_schedule-0-time_from"]')

    def schedule_to(self):
        return self.page.locator('//input[@id="activelongwrite-active_schedule-0-time_to"]')

    def location(self):
        return self.page.locator('//span[@id="select2-activelongwrite-location_id-container"]')

    def location_select(self):
        return self.page.locator('//ul[@class="select2-results__options"]//li[4]')


    def geocoder(self):
        return self.page.locator('//input[@id="activelongwrite-address"]')

    def geocoder_select(self):
        return self.page.locator('//div[@class="rounded autocomplete-select-container border bg-white"]//div[1]')

    def phone(self):
        return self.page.locator('//input[@id="activelongwrite-phone-0"]')

    def save_button(self):
        return self.page.locator('//button[@class="btn btn-success save-button"]')

    # def dow_button(self):
    #     return self.page.locator('//button[@class="btn btn-success save-button"]')



    @allure.step("Ввод названия")
    def active_title_input(self):
        self.active_title.fill('Игра в шахматы')

    @allure.step("Выбор категории")
    def select_category(self):
        self.active_category().click()
        self.active_category_select().click()

    @allure.step("Выбор подкатегории")
    def select_sub_category(self):
        self.active_sub_category().click()
        self.active_sub_category_select().click()

    @allure.step("Выбор типа записи")
    def select_type(self,text="По записи"):
        self.active_type().click()
        self.active_type_select(text=text).click()

    @allure.step("Ввод описания")
    def active_description_input(self):
        self.active_descriptoin().fill('Ребенок будет заниматься самостоятельно, участие родителей не требуетсядля занятий подойдет любое электронное устройство (компьютер, планшет или телефон) с веб-камерой и микрофоном')

    @allure.step("Ввод педагога и его описания")
    def teacher_input(self):
        self.teacher_name().fill('Иванов Иван Иванович')
        self.teacher_descriptoin().fill("Заслуженный педагог по шахматам")

    @allure.step("Ввод расписания")
    def schedule_input(self):
        self.schedule_from().fill('1000')
        self.schedule_to().fill('1100')

    @allure.step("Ввод телефона")
    def phone_input(self):
        self.phone().fill('9999999999')

    @allure.step("Выбор населенного пункта")
    def select_location(self):
        self.location().click()
        self.location_select().click()

    @allure.step("Загрузка главного изображения")
    def upload_main_image(self):
        file_path = Path(ROOT_DIR / "test_data"/'main.jpeg')
        self.input_image().set_input_files(file_path)
        self.upload_image().click()

    @allure.step("Ввод адреса")
    def geocoder_input(self):
        # self.geocoder().click()
        self.geocoder().fill("Казань")
        self.geocoder_select().click()

    @allure.step("Нажать на сохранить")
    def click_to_save_button(self):
        self.save_button().click()
