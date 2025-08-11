import commons
from playwright.sync_api import Page


def test_dynamic_table(page: Page):
    """
    Test Case: Dynamic Table

    Steps:
    1. Given: the user is on a page with a dynamic table
    2. When: the user wants to validate a specific set of data within the table
    3. Then: the XPATH selector strategy can be used to get the data

    Expected Result:
    The user should be able to validate the data within the table
    """
    page.goto(commons.url + '/dynamictable')
    table_text = page.locator(
        '//span[contains(text(), "Chrome")]/following-sibling::span[contains(text(), "%")]'
    ).text_content()
    comparing_text = page.locator('p.bg-warning').text_content()
    assert table_text in comparing_text
