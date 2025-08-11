import commons
from playwright.sync_api import Page, expect


def test_class(page: Page):
    """
    Test Case: Class

    Steps:
    1. Given: the user is on a page where elements are using classes
    2. When: the user wants to interact with a specific element
    3. Then: the unique class should be used to reference the element

    Expected Result:
    The button should be found
    """
    page.goto(commons.url + '/classattr')
    btn = page.locator('.btn-primary')
    expect(btn).to_be_visible()
    expect(btn).to_be_enabled()
    expect(btn).to_contain_text('Button')
