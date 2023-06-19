import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

import utils.secret_config
# import utils.secret_config
from pom.home_page_elements import HomePage


@pytest.mark.smoke
def test_contact_1(set_up) -> None:
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
    page.get_by_placeholder("Enter your name").fill("Ali")
    page.get_by_placeholder("Enter your name").press("Tab")
    page.get_by_placeholder("Enter your address").fill("ali123@gmail.com")
    page.get_by_placeholder("Enter your address").press("Tab")
    page.get_by_placeholder("Enter your email").fill("ali123@gmail.com")
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


@pytest.mark.regression
def test_run_2(set_up):
    page = set_up
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # context = browser.new_context()
    # page = context.new_page()
    # page.goto("https://symonstorozhenko.wixsite.com/website-1")
    home_page = HomePage(page)
    # page.wait_for_load_state("networkidle")
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()
    print("Pass")


# @pytest.mark.initial
# @pytest.mark.parametrize("email", [("Ahad-web")])
# @pytest.mark.parametrize("password", [(utils.secret_config.PASSWORD)])
# @pytest.mark.parametrize("password", [(os.environ.['PASSWORD'])])
@pytest.mark.parametrize("email, password", [("alirana78662@gmail.com", utils.secret_config.PASSWORD)])
def test_github_login(set_up_git_login, email, password) -> None:
    page = set_up_git_login
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # context = browser.new_context()
    # page = context.new_page()
    # page.goto("https://github.com/")
    page.get_by_role("link", name="Sign in").click()
    page.get_by_label("Username or email address").click()
    page.get_by_label("Username or email address").fill(email)
    page.get_by_label("Username or email address").press("Tab")
    page.get_by_label("Password").fill(password)
    page.get_by_label("Password").press("Enter")
    page.get_by_role("button", name="View profile and more").click()
    page.get_by_role("menuitem", name="Sign out").click()
    print("Success")
