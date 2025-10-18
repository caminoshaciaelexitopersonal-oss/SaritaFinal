import re
import uuid
from playwright.sync_api import sync_playwright, Page, expect

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    unique_id = str(uuid.uuid4())[:8]
    email = f"hotel_{unique_id}@example.com"
    username = f"hotel_{unique_id}"
    password = "password123"

    try:
        # 1. Registrar un nuevo usuario de tipo Hotel
        page.goto("http://localhost:3000/registro")

        page.get_by_label("Correo Electrónico").fill(email)
        page.get_by_label("Nombre de Usuario").fill(username)
        page.get_by_label("Contraseña", exact=True).fill(password)
        page.get_by_label("Confirmar Contraseña").fill(password)
        page.get_by_label("Quiero registrarme como:").select_option("PRESTADOR")

        expect(page.get_by_label("Nombre del Establecimiento")).to_be_visible()

        expect(page.get_by_role("option", name="Meta")).to_be_visible(timeout=20000)
        page.get_by_label("Departamento").select_option(label="Meta")

        expect(page.get_by_label("Municipio")).to_be_enabled()
        page.get_by_label("Municipio").select_option(label="PUERTO GAITAN")
        page.get_by_label("Nombre del Establecimiento").fill(f"Hotel Paraíso {unique_id}")

        expect(page.get_by_role("option", name="Hotel")).to_be_visible(timeout=20000)
        page.get_by_label("Categoría del Servicio").select_option(label="Hotel")

        page.get_by_role("button", name="Crear Cuenta").click()

        expect(page.get_by_text("¡Registro exitoso!")).to_be_visible(timeout=10000)

        # 2. Iniciar sesión con el nuevo usuario
        page.goto("http://localhost:3000/login")
        page.get_by_label("Correo Electrónico").fill(username)
        page.get_by_label("Contraseña").fill(password)
        page.get_by_role("button", name="Iniciar Sesión").click()

        # 3. Esperar a que el panel cargue y verificar la nueva navegación de "Mi Negocio"
        expect(page.get_by_role("button", name=re.compile("Mi Negocio"))).to_be_visible(timeout=15000)
        page.get_by_role("button", name=re.compile("Mi Negocio")).click()

        # Abrir la sección de Gestión Operativa
        page.get_by_role("button", name=re.compile("Gestión Operativa")).click()

        # Abrir Módulos Especializados
        page.get_by_role("button", name=re.compile("Módulos Especializados")).click()

        # Verificar que el enlace de Habitaciones es visible
        expect(page.get_by_role("link", name="Habitaciones")).to_be_visible()

        # Verificar que el enlace de Restaurante NO es visible
        expect(page.get_by_role("link", name="Menú/Carta")).not_to_be_visible()

        # 4. Tomar la captura de pantalla
        page.screenshot(path="jules-scratch/verification/refactored_dashboard_nav.png")
        print("Screenshot taken successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
        page.screenshot(path="jules-scratch/verification/error.png")
        raise

    finally:
        browser.close()

with sync_playwright() as playwright:
    run(playwright)