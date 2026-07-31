from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'
    page.goto(URL)

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.focus()

    for char in 'user@gmail.com':
        page.keyboard.type(char, delay=200)  # for normal typing

    page.keyboard.press("ControlOrMeta+A")  # for combination of keys
    page.keyboard.press("Delete")

    page.wait_for_timeout(3000)
