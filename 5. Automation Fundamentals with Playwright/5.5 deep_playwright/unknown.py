from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'
    page.goto(URL)

    # unknown = page.locator('#unknown')
    # expect(unknown).to_be_disabled()

    # login_button = page.get_by_test_id('login-page-login-button')
    # login_button.fill('unknown')

    page.evaluate(
        """
        const title = document.getElementById('authentication-ui-course-title-text')
        title.textContent = 'New Text'
        """
    )

    page.wait_for_timeout(3000)
