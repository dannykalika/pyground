import commons
from playwright.sync_api import Page, expect


def test_ajax(page: Page):
    """
    Test Case: Ajax Requests

    Steps:
    1. Given: the user is on a page where AJAX requests are needed
    2. When: the user triggers an AJAX request on the page
    3. Then: the page should be updated with necessary content upon completion of the request

    Expected Result:
    The request should be completed successfully
    """
    elements = commons.Elements(page)
    page.goto(commons.url + '/ajax')
    success = elements.success
    request_btn = page.locator('#ajaxButton')
    expect(success).not_to_be_attached()
    request_btn.click()
    page.wait_for_load_state('networkidle')
    expect(success).to_be_visible()
