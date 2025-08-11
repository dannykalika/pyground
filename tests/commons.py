from playwright.sync_api import Page

url = 'http://uitestingplayground.com'


class Elements:
    def __init__(self, page: Page):
        self.page = page
        self.primary_button = self.page.locator('.btn-primary')
        self.success_button = self.page.locator('.bg-success')
