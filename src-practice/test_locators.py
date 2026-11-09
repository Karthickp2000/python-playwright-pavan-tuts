"""
# from playwright.sync_api import Playwright
from playwright.sync_api import expect
"""
from playwright.sync_api import Page

def test_locators(page:Page):
    page.goto("https://demo.nopcommerce.com/")