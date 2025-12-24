import json


def test_register(invoke_browser, page):
    page=invoke_browser
    with open("creds.json") as s:
        data= json.load(s)
    page.get_by_role("link", name="Signup / Login").click()
    page.get_by_text("New User Signup!", exact=True)
    page.get_by_placeholder("Name").fill(data["name"])
    page.locator("input[data-qa='signup-email']").fill(data["email"])