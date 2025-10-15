import re
from playwright.sync_api import sync_playwright, Page, expect

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    try:
        # 1. Navegar a la página de login
        page.goto("http://localhost:3000/login", timeout=60000)

        # 2. Esperar a que el formulario de login esté visible
        expect(page.get_by_role("heading", name="Acceso al Sistema")).to_be_visible(timeout=15000)

        # 3. Iniciar sesión con las etiquetas correctas
        page.get_by_label("Correo Electrónico o Usuario").fill("prestador@test.com")
        page.get_by_label("Contraseña").fill("password123")
        page.get_by_role("button", name="Iniciar Sesión").click()

        # 4. Esperar a la navegación al dashboard y verificar el layout
        expect(page.get_by_role("heading", name="Panel de Prestador")).to_be_visible(timeout=15000)

        # 5. Hacer clic en el enlace "Mi Perfil"
        profile_link = page.get_by_role("button", name="Mi Perfil")
        expect(profile_link).to_be_visible()
        profile_link.click()

        # 6. Verificar que el título "Perfil del Prestador" sea visible
        expect(page.get_by_role("heading", name="Perfil del Prestador")).to_be_visible(timeout=5000)

        # 7. Tomar captura de pantalla
        page.screenshot(path="jules-scratch/verification/prestador_perfil_view.png")
        print("Screenshot taken successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
        page.screenshot(path="jules-scratch/verification/error.png")
    finally:
        context.close()
        browser.close()

with sync_playwright() as playwright:
    run(playwright)