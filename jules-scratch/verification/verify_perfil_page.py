from playwright.sync_api import sync_playwright, expect

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # 1. Verificar la página de inicio
    page.goto("http://localhost:3000/es")
    expect(page.get_by_role("heading", name="Bienvenido a Sarita Unificado")).to_be_visible()
    page.screenshot(path="jules-scratch/verification/01_homepage.png")

    # 2. Iniciar sesión como prestador
    page.goto("http://localhost:3000/login")
    page.get_by_label("Nombre de Usuario").fill("prestador")
    page.get_by_label("Contraseña").fill("prestador")
    page.get_by_role("button", name="Iniciar Sesión").click()

    # 3. Verificar el dashboard del prestador
    expect(page).to_have_url("http://localhost:3000/es/dashboard/prestador")

    # Navegar a la página de perfil
    page.goto("http://localhost:3000/es/dashboard/prestador/mi-negocio/gestion-operativa/genericos/perfil")

    # Verificar que el título de la página es correcto
    expect(page.get_by_role("heading", name="Gestionar Mi Perfil")).to_be_visible()

    # Verificar que un campo del formulario existe
    expect(page.get_by_label("Nombre Comercial")).to_be_visible()

    # Tomar el screenshot final
    page.screenshot(path="jules-scratch/verification/03_perfil_form.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
