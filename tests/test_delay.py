import commons
from playwright.sync_api import Page, expect


def test_class(page: Page):
    """
    Test Case: Delay

    Steps:
    1. Given: the user is on a page where JavaScript is processing on the client side
    2. When: the user triggers client side logic
    3. Then: the page should wait for the logic to be processed

    Expected Result:
    The button should not exist until the delay is over
    """
    elements = commons.Elements(page)
    page.goto(commons.url + '/clientdelay')
    expect(elements.primary_button).to_be_visible()
    expect(elements.success).not_to_be_attached()
    elements.primary_button.click()
    expect(elements.success).to_be_visible(timeout=17000)
