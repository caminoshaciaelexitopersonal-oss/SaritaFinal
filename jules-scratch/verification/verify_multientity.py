from playwright.sync_api import sync_playwright, expect

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # Verificar formulario de registro
    page.goto("http://localhost:3000/registro")
    expect(page.get_by_label("Departamento")).to_be_visible()
    expect(page.get_by_label("Municipio")).to_be_visible()

    # Iniciar sesión como admin de entidad
    page.goto("http://localhost:3000/login")
    page.get_by_label('Correo Electrónico o Usuario').fill('admin_meta@example.com')
    page.get_by_label('Contraseña').fill('password123')
    page.get_by_role('button', { 'name': 'Ingresar' }).click()

    # Esperar a que el header se actualice con el nombre de la entidad
    expect(page.locator('header')).to_contain_text('Turismo del Meta', timeout=10000)

    # Tomar screenshot
    page.screenshot(path="jules-scratch/verification/verification.png")

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)