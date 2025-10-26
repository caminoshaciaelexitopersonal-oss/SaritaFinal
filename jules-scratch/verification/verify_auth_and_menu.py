# jules-scratch/verification/verify_auth_and_menu.py
import re
from playwright.sync_api import sync_playwright, Page, expect

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    try:
        # 1. Navegar a la página de registro
        page.goto("http://localhost:3000/es/registro")
        expect(page.get_by_role("heading", name="Regístrate")).to_be_visible()

        # 2. Completar el formulario de registro
        page.get_by_placeholder("Nombres").fill("Test")
        page.get_by_placeholder("Apellidos").fill("User")
        page.get_by_placeholder("Nombre de usuario").fill("testuser")
        page.get_by_placeholder("correo@ejemplo.com").fill("testuser@example.com")

        # Seleccionar Departamento y Municipio
        page.get_by_label("Departamento").select_option(label="META")
        page.get_by_label("Municipio").select_option(label="VILLAVICENCIO")

        page.get_by_label("Tipo de documento").select_option(label="Cédula de Ciudadanía")
        page.get_by_placeholder("Número de documento").fill("123456789")

        page.get_by_label("Contraseña", exact=True).fill("Testpass123!")
        page.get_by_label("Confirmar contraseña").fill("Testpass123!")

        page.get_by_label("Rol").select_option(label="Prestador de Servicios Turísticos")

        # Aceptar términos y condiciones
        page.get_by_role("checkbox").check()

        # Enviar formulario
        page.get_by_role("button", name="Crear Cuenta").click()

        # 3. Verificar redirección a login
        expect(page.get_by_role("heading", name="Bienvenido de nuevo")).to_be_visible(timeout=10000)
        expect(page.get_by_text("Tu cuenta ha sido creada exitosamente.")).to_be_visible()

        # 4. Iniciar sesión
        page.get_by_placeholder("correo@ejemplo.com").fill("testuser@example.com")
        page.get_by_placeholder("Contraseña").fill("Testpass123!")
        page.get_by_role("button", name="Iniciar Sesión").click()

        # 5. Navegar al panel y verificar el menú
        expect(page.get_by_role("heading", name=re.compile(r"Bienvenido de nuevo,\s*testuser"))).to_be_visible(timeout=10000)

        # Verificar que la sección "Mi Negocio" está visible
        expect(page.get_by_text("Mi Negocio")).to_be_visible()

        # 6. Tomar captura de pantalla
        page.screenshot(path="jules-scratch/verification/verification.png")

    finally:
        context.close()
        browser.close()

with sync_playwright() as playwright:
    run(playwright)
