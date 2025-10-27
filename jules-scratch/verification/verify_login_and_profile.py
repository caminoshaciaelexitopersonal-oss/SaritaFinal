import re
from playwright.sync_api import sync_playwright, expect

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(60000)

    try:
        # 1. Navegar a la página de inicio de sesión con prefijo de idioma
        page.goto("http://localhost:3000/es/dashboard/login")

        # 2. Introducir credenciales
        page.get_by_label("Correo Electrónico o Usuario").fill("prestador@test.com")
        page.get_by_label("Contraseña").fill("testpassword123")

        # 3. Hacer clic en el botón de inicio de sesión
        page.get_by_role("button", name="Iniciar Sesión").click()

        # 4. Esperar a que la URL cambie, indicando una redirección exitosa
        expect(page).not_to_have_url(re.compile(".*login"))

        # 5. Navegar a la página de perfil
        page.goto("http://localhost:3000/es/dashboard/prestador/mi-negocio/gestion-operativa/genericos/perfil")

        # 6. Verificar que el encabezado del perfil esté visible
        expect(page.get_by_role("heading", name="Mi Perfil")).to_be_visible()

        # 7. Tomar captura de pantalla
        page.screenshot(path="jules-scratch/verification/final_verification.png")

        print("Verificación final completada con éxito.")

    except Exception as e:
        print(f"Error durante la verificación: {e}")
        page.screenshot(path="jules-scratch/verification/final_error.png")

    finally:
        context.close()
        browser.close()

with sync_playwright() as playwright:
    run(playwright)
