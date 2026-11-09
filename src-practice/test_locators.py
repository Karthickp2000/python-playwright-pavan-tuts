"""
# from playwright.sync_api import Playwright
from playwright.sync_api import expect
"""
import re
import time

from playwright.sync_api import Page, expect

#variables
URL = "https://demo.nopcommerce.com/"

def test_locators(page:Page):
    page.goto(URL)
    expect(page).to_have_url(re.compile(URL))

    expect(page.locator("body")).not_to_be_empty()

    time.sleep(3)

