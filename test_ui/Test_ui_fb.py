# from playwright.sync_api import Playwright, sync_playwright, expect
import os

from playwright.sync_api import Playwright, sync_playwright

import utils.secret_config


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.facebook.com/login/")
    page.wait_for_load_state("networkidle")
    page.locator("//input[@name='email']").fill("ahad123@gmail.com")
    # page.locator("//input[@name='pass']").fill(utils.secret_config.PASSWORD)
    page.locator("//input[@name='pass']").fill(os.environ["PASSWORD"])
    page.locator("//button[@name='login']").click()
    print("Login Success")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)
