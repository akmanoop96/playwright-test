import time

import pytest
from playwright.sync_api import Page, expect, Playwright



def test_playwrightBasics(playwright):
   browser=playwright.chromium.launch(headless=False)
   context=browser.new_context()
   page = context.new_page()
   page.goto("https:rahulshettyacademy.com")

def test_playwrightShortcut(page:Page):
    page.goto("https://rahulshettyacademy.com")

def test_core_locators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link",name='terms and conditions').click()
    page.get_by_role("button",name='Sign In').click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

def test_firefoxBrowser(playwright: Playwright):
    firefoxBrowser=playwright.firefox.launch(headless=False)
    firefoxBrowser.new_context()
    page = firefoxBrowser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("learningggg")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name='terms and conditions').click()
    page.get_by_role("button", name='Sign In').click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()









    time.sleep(5)








