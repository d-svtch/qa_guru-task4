from selene import browser
import pytest
browser.config.base_url = 'https://demoqa.com'

@pytest.fixture(autouse=True)
def operations_with_browser():
    browser.open("/automation-practice-form")
    yield
    browser.quit()