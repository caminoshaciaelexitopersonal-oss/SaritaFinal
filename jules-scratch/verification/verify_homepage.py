from playwright.sync_api import sync_playwright, Page, expect

def test_homepage_loads(page: Page):
    """
    This test verifies that the homepage loads correctly and takes a screenshot.
    """
    # 1. Arrange: Go to the homepage.
    page.goto("http://localhost:3000")

    # 2. Assert: Confirm the title is correct.
    expect(page).to_have_title("Sarita")

    # 3. Assert: Confirm the header is visible.
    header = page.get_by_role("banner")
    expect(header).to_be_visible()

    # 4. Screenshot: Capture the final result for visual verification.
    page.screenshot(path="jules-scratch/verification/homepage.png")

def run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        test_homepage_loads(page)
        browser.close()

if __name__ == "__main__":
    run_test()