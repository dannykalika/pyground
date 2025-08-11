import commons
from playwright.sync_api import Page, expect


def test_dynamic_id(page: Page):
    """
    Test Case: Dynamic ID

    Steps:
    1. Given: the user is on a page with dynamic ID elements
    2. When: the user wants to interact with Dynamic ID elements
    3. Then: element should be found and referenced

    Expected Result:
    The button should be found and clicked
    """
    page.goto(commons.url + '/dynamicid')
    btn = page.get_by_role('button', name='Button with Dynamic ID')
    expect(btn).to_be_visible()
    expect(btn).to_be_enabled()
    expect(btn).to_contain_text('Button with Dynamic ID')
