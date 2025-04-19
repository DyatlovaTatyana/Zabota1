from Pages.login_page import Login_Page
from Pages.active_page import Active_Page
from Consts.link import Links

class Steps:
        def __init__(self, browser):
            self.browser = browser
            self.login_page = Login_Page(browser)
            self.active_page = Active_Page(browser)

        def login_admin(self):
            self.login_page.open_admin(Links.LOGIN)
            self.login_page.login.fill('biblsoln')
            self.login_page.password.fill('ffgfffffff')
            self.login_page.click_to_button()
            self.browser.wait_for_load_state('networkidle')

        def create_active(self):
            self.active_page.active_title_input()
            self.active_page.select_category()
            self.active_page.select_sub_category()
            self.active_page.select_type("Без записи")
            self.active_page.active_description_input()
            self.active_page.teacher_input()
            self.active_page.upload_main_image()
            self.active_page.schedule_input()
            self.active_page.select_location()
            self.active_page.geocoder_input()
            self.active_page.phone_input()
            self.active_page.click_to_save_button()
            self.browser.wait_for_load_state('networkidle')


