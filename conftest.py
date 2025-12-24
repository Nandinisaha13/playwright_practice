import pytest


@pytest.fixture(scope="function")
def invoke_browser(page):
    page.goto("http://automationexercise.com")
    yield page