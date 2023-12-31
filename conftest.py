import time

import pytest
from playwright.sync_api import Playwright


@pytest.fixture
def set_up(page):
    # # Access
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # context = browser.new_context()
    # # Open new page
    # page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(2000)

    yield page
    page.close()


@pytest.fixture
def contact_page_fill(set_up):
    # # Access
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # context = browser.new_context()
    # # Open new page
    # page = context.new_page()
    # page.goto("/collection")
    # page.set_default_timeout(3000)
    page = set_up
    # # Access
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # context = browser.new_context()
    # # Open new page
    # page = context.new_page()
    # page.goto("https://symonstorozhenko.wixsite.com/website-1")
    # Act what to do
    page.get_by_role("link", name="Contact Us").click()
    page.get_by_placeholder("Enter your name").click()
    page.get_by_placeholder("Enter your name").fill("Ahad")
    page.get_by_placeholder("Enter your name").press("Tab")
    page.get_by_placeholder("Enter your address").fill("ahada123@gmail.com")
    page.get_by_placeholder("Enter your address").press("Tab")
    page.get_by_placeholder("Enter your email").fill("ahada123@gmail.com")
    page.get_by_placeholder("Enter your address").click()
    page.get_by_placeholder("Enter your address").fill("12str 77 address")
    page.get_by_placeholder("Enter your phone number").click()
    page.get_by_placeholder("Enter your phone number").fill("12345887654")
    page.get_by_placeholder("Type the subject").click()
    page.get_by_placeholder("Type the subject").fill("dummy subject")
    page.get_by_placeholder("Type your message here...").click()
    page.get_by_placeholder("Type your message here...").fill("here is a message")
    page.get_by_test_id("buttonElement").click()
    print("Pass")

    yield page

# this code is for open multiple browsers while running your test

# @pytest.fixture(scope='session')
# def context_creation(playwright):
#     # # Access
#     browser = playwright.chromium.launch(headless=False, slow_mo=300)
#     context = browser.new_context()
#     # # Open new page
#     page = context.new_page()
#     page.goto("https://github.com/")
#     page.set_default_timeout(3000)
#
#     yield context
#     time.sleep(5)
#
#
# @pytest.fixture()
# def set_up_git_login(context_creation):
#     context = context_creation
#     page = context.new_page()
#     page.goto("https://github.com/")
#     page.set_default_timeout(3000)
#
#     yield page
#     time.sleep(3)
#     page.close()


# this code is using for multiple windows open and create storage state in form of json file....
@pytest.fixture(scope='session')
def context_creation(playwright):
    # # Access
    browser = playwright.chromium.launch(headless=False, slow_mo=300)
    context = browser.new_context()
    # # Open new page
    page = context.new_page()
    page.goto("https://github.com/")
    page.set_default_timeout(3000)
    # page.wait_for_load_state("Networkidle")
    time.sleep(2)
    context.storage_state(path='state.json')

    yield context
    time.sleep(5)


@pytest.fixture()
def set_up_git_login(context_creation, browser):
    context = browser.new_context(storage_state='state.json')
    page = context.new_page()
    page.goto("https://github.com/")
    page.set_default_timeout(3000)

    yield page
    time.sleep(3)
    page.close()
