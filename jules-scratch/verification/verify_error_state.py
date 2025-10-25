from playwright.sync_api import sync_playwright, expect

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    print("Navegando a la página de inicio de sesión...")
    page.goto("http://localhost:3000/es/login")

    print("Esperando 5 segundos para que la página cargue o falle...")
    page.wait_for_timeout(5000)

    print("Tomando captura de pantalla del estado final...")
    page.screenshot(path="jules-scratch/verification/frontend_error_screenshot.png")

    print("Captura de pantalla guardada en jules-scratch/verification/frontend_error_screenshot.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
