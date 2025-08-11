import commons
import pytest
from playwright.sync_api import Page, expect, Error


def test_class(page: Page):
    """
    Test Case: Hidden Layers

    Steps:
    1. Given: the user is on a page where elements are cached
    2. When: the user wants to interact with a cached element
    3. Then: the state of the element should persist

    Expected Result:
    The button inactive state should persist
    """
    page.goto(commons.url + '/hiddenlayers')
    greenbtn = page.locator('#greenButton')
    bluebtn = page.locator('#blueButton')
    expect(greenbtn).to_be_visible()
    expect(bluebtn).not_to_be_visible()
    greenbtn.click()
    expect(bluebtn).to_be_visible()
    with pytest.raises(Error) as errinfo:
        greenbtn.click(timeout=500)
    assert 'Timeout' in str(errinfo.value)
    assert 'intercepts pointer events' in str(errinfo.value)
