import commons
from playwright.sync_api import Page, expect


def test_scroll(page: Page):
    """
    Test Case: Scroll

    Steps:
    1. Given: the user is on a page where scroll bars are present
    2. When: there is a hidden element in the scroll view
    3. Then: the user should be able to scroll to the element

    Expected Result:
    The hidden element should be visible after scrolling
    """
    page.goto(commons.url + '/scrollbars')
    hidden_button = page.locator('#hidingButton')
    hidden_button.scroll_into_view_if_needed()
    expect(hidden_button).to_be_in_viewport()
