import json
import time
from playwright.sync_api import expect


def test_register(invoke_browser, page):
    page=invoke_browser
    with open("creds.json") as s:
        data= json.load(s)
    page.get_by_role("link", name="Signup / Login").click()
    page.get_by_text("New User Signup!", exact=True)
    page.get_by_placeholder("Name").fill(data["name"])
    page.locator("input[data-qa='signup-email']").fill(data["email"])
    page.get_by_role("button", name="Signup").click()
    expect(page.get_by_text("Enter Account Information")).to_be_visible()
    page.get_by_role("radio", name="Mrs.").check()
    page.get_by_label("Name *", exact=True).fill(data["name"])
    page.get_by_label("Password *", exact=True).fill("hello")
    page.locator("[name='days']").select_option(data["day"])
    page.locator("[name='months']").select_option(data["month"])
    page.locator("#years:visible").select_option(data["year"])
    page.get_by_role("checkbox", name="Sign up for our newsletter!").check()
    page.get_by_role("checkbox", name="Receive special offers from our partners!").check()
    page.get_by_role("textbox", name="First name *").fill("Nandini")
    page.get_by_role("textbox", name="Last name *").fill("Saha")
    page.locator("#company").fill("Zoops")
    page.locator("#address1").fill("Just a street address,jssi")
    page.locator("#address2").fill("optional")
    page.get_by_label("Country *").select_option(data["country"])
    time.sleep(4)