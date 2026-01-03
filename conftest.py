import pytest


@pytest.fixture(scope="function")
def invoke_browser(page):
    page.goto("https://automationexercise.com")
    yield page