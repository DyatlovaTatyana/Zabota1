from Consts.link import Links



class BasePage:

    def __init__(self, page):
        self.page = page

    def open(self, url=''):
        self.page.goto(Links.HOST + url)

    def open_admin(self, url=''):
        self.page.goto(Links.HOST_ADMIN + url)

