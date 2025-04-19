import pytest
from playwright.sync_api import Page, sync_playwright

"""
browser:
  channel: "chrome"
  headless: False
  ignore_https_errors: True
  args: ["--start-maximized"]
"""
#док стринга

@pytest.fixture
def browser():
# def page():
    with sync_playwright() as playwright: #with закрывает объекты
        browser = playwright.chromium.launch(
            channel="chrome",
            headless=False,
            args=["--start-maximized"],
        )

        context = browser.new_context(ignore_https_errors=True, no_viewport=True)
        context.set_default_timeout(20_000)
        page = context.new_page()
        yield page
        browser.close()











# import pytest
# from playwright.sync_api import Page
#
# @pytest.fixture()
# def page(context):
#     page: Page = context.new_page()
#     page.set_viewport_size({'height': 1080, 'width': 1920})
#     yield page
