import commons
from playwright.sync_api import Page, expect


def test_click(page: Page):
    """
    Test Case: Click

    Steps:
    1. Given: the user is on a page where event-based clicks do not work
    2. When: the user does a physical mouse click
    3. Then: the page should register the mouse click

    Expected Result:
    The button should be clicked
    """
    page.goto(commons.url + '/click')
    page.locator('#badButton').click()
    success = page.locator('button.btn.btn-success')
    expect(success).to_be_visible()
