import commons
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def visit_page(page: Page):
    page.goto(commons.url + '/verifytext')
    yield page


def test_inner_text(visit_page):
    """
    Test Case: Inner text

    Steps:
    1. Given: the user is on a page where there is an inner text
    2. Then: the user should be able to validate the inner text by getting the text

    Expected Result:
    The inner text should be found
    """
    page = visit_page
    text = page.locator('div.bg-primary').text_content()
    assert 'Welcome UserName!' in text


def test_inner_text_xpath(visit_page):
    """
    Test Case: Inner text via xpath

    Steps:
    1. Given: the user is on a page where there is an inner text
    2. Then: the XPATH selector strategy can be used to validate the inner text

    Expected Result:
    The inner text should be found
    """
    page = visit_page
    expect(
        page.locator("//div/span[normalize-space(.)='Welcome UserName!']")
    ).to_be_visible()
