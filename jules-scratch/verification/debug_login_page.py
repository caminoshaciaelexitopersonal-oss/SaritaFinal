from playwright.sync_api import sync_playwright, Page, expect

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    try:
        print("Navigating to login page...")
        page.goto("http://localhost:3000/login", timeout=60000)

        print("Taking screenshot of login page...")
        page.screenshot(path="jules-scratch/verification/login_page_debug.png")
        print("Screenshot 'login_page_debug.png' taken successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
        page.screenshot(path="jules-scratch/verification/error_debug.png")
        print("Error screenshot taken.")
    finally:
        context.close()
        browser.close()

with sync_playwright() as playwright:
    run(playwright)