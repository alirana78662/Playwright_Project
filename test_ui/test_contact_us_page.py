import time
from playwright.sync_api import Playwright, sync_playwright
import pytest
from pom.contact_us_page import ContactUs


def test_submit_form(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    contact_page = ContactUs(page)
    contact_page.navigate()
    contact_page.submit_form("Ali", "Lahore", "testmail@gmail.com", "123456789", "test subj",
                             "test messageasdasdasdasdasdasasdasdasdasdasdasasdasdasd")
    print("Success")


with sync_playwright() as playwright:
    test_submit_form(playwright)
    # time.sleep(5)
