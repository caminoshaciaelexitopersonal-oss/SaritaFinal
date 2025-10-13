from playwright.sync_api import sync_playwright, Page, expect

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # Verificar la página del Dashboard
    page.goto("http://localhost:3000/prestador/dashboard")
    expect(page.get_by_role("heading", name="Dashboard del Prestador")).to_be_visible()
    page.screenshot(path="jules-scratch/verification/prestador-dashboard.png")

    # Verificar la página de Servicios
    page.goto("http://localhost:3000/prestador/servicios")
    expect(page.get_by_role("heading", name="Gestión de Servicios")).to_be_visible()
    page.screenshot(path="jules-scratch/verification/prestador-servicios.png")

    # Verificar la página de Reservas
    page.goto("http://localhost:3000/prestador/reservas")
    expect(page.get_by_role("heading", name="Gestión de Reservas")).to_be_visible()
    page.screenshot(path="jules-scratch/verification/prestador-reservas.png")

    # Verificar la página de Facturación
    page.goto("http://localhost:3000/prestador/facturacion")
    expect(page.get_by_role("heading", name="Gestión de Facturación")).to_be_visible()
    page.screenshot(path="jules-scratch/verification/prestador-facturacion.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)