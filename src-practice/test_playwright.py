# from playwright.async_api import Playwright
import asyncio
import re
import pytest

from playwright.async_api import async_playwright, Page, expect

url = "https://www.amkette.com/pages/support"


# Sync test
# @pytest.mark.skip
# def test_first(page: Page):
#     page.goto(url)
#     expect(page).to_have_url(url)
#     expect(page).to_have_title(re.compile("Support –"))

#
# # Async test
# @pytest.mark.asyncio
# async def test_first():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         page = await browser.new_page()
#
#         await page.goto(url)
#         await expect(page).to_have_url(url)
#         await expect(page).to_have_title(re.compile("Support –"))
#
#         await asyncio.sleep(2)
#         await page.close()
#         await browser.close()
