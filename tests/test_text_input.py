import commons
from playwright.sync_api import Page, expect


def test_test_input(page: Page):
    """
    Test Case: Test input

    Steps:
    1. Given: the user is on a page where sending text via DOM events does not work
    2. When: the user emulates real keyboard input
    3. Then: the input should be applied to the application

    Expected Result:
    The text should be sent to the input
    """
    page.goto(commons.url + '/textinput')
    page.get_by_role('textbox', name='Set New Button Name').fill(
        'adding input text to element'
    )
    page.get_by_role('button', name='Button That Should Change it').click()
    expect(
        page.get_by_role('button', name='adding input text to element')
    ).to_be_visible()
