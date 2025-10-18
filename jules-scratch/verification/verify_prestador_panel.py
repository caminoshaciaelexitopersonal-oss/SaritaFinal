import re
from playwright.sync_api import sync_playwright, Page, expect

def run(playwright):
    # --- Helpers ---
    def generate_unique_data():
        timestamp = page.evaluate("() => Date.now()")
        return {
            "email": f"prestador_test_{timestamp}@example.com",
            "username": f"prestador_test_{timestamp}",
            "password": "password123",
            "nombre_negocio": "Hotel Verificado"
        }

    # --- Configuración ---
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    BASE_URL = "http://localhost:3000"

    # --- Generar datos para el nuevo prestador ---
    prestador_data = generate_unique_data()

    # --- 1. Registrar un nuevo Prestador ---
    try:
        page.goto(f"{BASE_URL}/registro")

        # Rellenar campos comunes
        page.get_by_label("Correo Electrónico").fill(prestador_data["email"])
        page.get_by_label("Nombre de Usuario").fill(prestador_data["username"])
        page.get_by_label("Contraseña").fill(prestador_data["password"])
        page.get_by_label("Confirmar Contraseña").fill(prestador_data["password"])
        page.get_by_label("Quiero registrarme como:").select_option("PRESTADOR")

        # Rellenar campos de ubicación (necesario para el registro)
        page.get_by_label("Departamento").select_option(label="META")
        # Esperar a que los municipios se carguen
        expect(page.get_by_label("Municipio")).to_have_count(1, timeout=10000)
        page.get_by_label("Municipio").select_option(label="VILLAVICENCIO")

        # Rellenar campos específicos de Prestador
        page.get_by_label("Nombre del Establecimiento").fill(prestador_data["nombre_negocio"])
        page.get_by_label("Categoría del Servicio").select_option(label="Hoteles")

        page.get_by_role("button", name="Crear Cuenta").click()

        # Esperar a ser redirigido a la página de login
        expect(page).to_have_url(re.compile(r".*/login"), timeout=15000)
        print("Registro de prestador exitoso.")

    except Exception as e:
        print(f"Error durante el registro: {e}")
        page.screenshot(path="jules-scratch/verification/error_registro.png")
        browser.close()
        return

    # --- 2. Iniciar Sesión ---
    try:
        page.get_by_label("Correo Electrónico").fill(prestador_data["email"])
        page.get_by_label("Contraseña").fill(prestador_data["password"])
        page.get_by_role("button", name="Iniciar Sesión").click()

        # Esperar a ser redirigido al dashboard
        expect(page).to_have_url(re.compile(r".*/dashboard"), timeout=15000)
        print("Inicio de sesión exitoso.")

    except Exception as e:
        print(f"Error durante el inicio de sesión: {e}")
        page.screenshot(path="jules-scratch/verification/error_login.png")
        browser.close()
        return

    # --- 3. Navegar al Perfil y Tomar Captura de Pantalla ---
    try:
        # Hacer clic en el enlace "Mi Perfil"
        page.get_by_role("link", name="Mi Perfil").click()

        # Esperar a que la página de perfil cargue
        expect(page).to_have_url(re.compile(r".*/dashboard/prestador/perfil"), timeout=15000)

        # Verificar que el formulario de perfil esté visible
        expect(page.get_by_label("Nombre del Negocio")).to_have_value(prestador_data["nombre_negocio"])
        print("Navegación al perfil exitosa.")

        # Tomar la captura de pantalla
        page.screenshot(path="jules-scratch/verification/verification.png")
        print("Captura de pantalla guardada en jules-scratch/verification/verification.png")

    except Exception as e:
        print(f"Error durante la navegación al perfil: {e}")
        page.screenshot(path="jules-scratch/verification/error_perfil.png")

    finally:
        # --- Limpieza ---
        browser.close()

with sync_playwright() as playwright:
    run(playwright)