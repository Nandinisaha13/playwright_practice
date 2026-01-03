import json
import time
from playwright.sync_api import expect


def test_register(invoke_browser, page): #test case 1
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
    page.get_by_role("textbox", name="State *").fill("check")
    page.get_by_label("City *", exact=True).fill("City")
    page.locator("#zipcode").fill("373839")
    page.get_by_role("textbox", name="Mobile Number *").fill("3938494940")
    page.get_by_role("button", name="Create Account").click()
    expect(page.locator("b:has-text('ACCOUNT CREATED!')")).to_be_visible()
    page.get_by_role("link", name="Continue").click()
    logged_in_text = f"Logged in as {data['name']}"
    expect(page.get_by_text(logged_in_text, exact=True)).to_be_visible()
    page.get_by_text("Delete Account", exact=True).click()
    expect(page.locator("b:has-text('ACCOUNT DELETED!')")).to_be_visible()

    time.sleep(4)

def test_case2(invoke_browser, page):
    page=invoke_browser
    with open("creds.json") as s:
        data= json.load(s)
    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_role("heading", name="Login to your account")).to_be_visible()
    page.locator("//input[@data-qa='login-email']").fill(data["email1"])
    page.get_by_placeholder("Password", exact=True).fill("hello")
    page.get_by_role("button", name="Login").click()
    h=f"Logged in as {data['name']}"
    expect(page.get_by_text(h, exact=True)).to_be_visible()
    page.get_by_text("Delete Account", exact=True).click()
    expect(page.locator("b:has-text('ACCOUNT DELETED!')")).to_be_visible()

