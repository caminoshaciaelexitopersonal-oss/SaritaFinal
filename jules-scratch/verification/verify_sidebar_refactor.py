import re
from playwright.sync_api import sync_playwright, expect

def run_verification(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    try:
        # 1. Navegar a la página de login
        page.goto("http://localhost:3000/login")

        # 2. Iniciar sesión como prestador
        page.get_by_label("Correo Electrónico o Usuario").fill("prestador_test@example.com")
        page.get_by_label("Contraseña").fill("password123")
        page.get_by_role("button", name="Iniciar Sesión").click()

        # 3. Esperar a que el dashboard cargue
        # La URL debería cambiar a /dashboard
        expect(page).to_have_url(re.compile(r".*/dashboard"))

        # 4. Verificar que el menú "Mi Negocio" y sus nuevas secciones están visibles
        sidebar = page.locator("aside")

        # El botón "Mi Negocio" debe estar visible
        mi_negocio_button = sidebar.get_by_role("button", name="Mi Negocio")
        expect(mi_negocio_button).to_be_visible()

        # Asegurarse de que el menú está expandido (hacer clic si es necesario)
        # En este caso, el menú se abre por defecto, pero es una buena práctica asegurarlo
        if mi_negocio_button.get_attribute("aria-expanded") == "false":
            mi_negocio_button.click()

        # 5. Verificar la presencia de las nuevas secciones
        expect(sidebar.get_by_role("button", name="Gestión Archivística")).to_be_visible()
        expect(sidebar.get_by_role("button", name="Gestión Financiera")).to_be_visible()

        # 6. Tomar la captura de pantalla
        screenshot_path = "jules-scratch/verification/sidebar_verification.png"
        sidebar.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
        # Tomar una captura de pantalla del error si es posible
        page.screenshot(path="jules-scratch/verification/error.png")
    finally:
        browser.close()

with sync_playwright() as playwright:
    run_verification(playwright)
