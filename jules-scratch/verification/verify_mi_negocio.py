# jules-scratch/verification/verify_mi_negocio.py
from playwright.sync_api import sync_playwright, expect
import re

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            # 1. Iniciar sesión como el usuario prestador de prueba
            page.goto("http://localhost:3000/es/login", timeout=60000)
            page.get_by_label("Correo Electrónico o Usuario").fill("prestador_test")
            page.get_by_label("Contraseña").fill("testpassword123")
            page.get_by_role("button", name="Iniciar Sesión").click()

            # Esperar a que la redirección al dashboard ocurra usando una expresión regular
            expect(page).to_have_url(re.compile(r".*/dashboard.*"), timeout=60000)
            print("Inicio de sesión exitoso.")

            # 2. Navegar a la página de Perfil
            page.goto("http://localhost:3000/es/dashboard/prestador/mi-negocio/gestion-operativa/genericos/perfil", timeout=60000)
            expect(page.get_by_role("heading", name="Gestionar Mi Perfil")).to_be_visible()
            print("Página de Perfil cargada correctamente.")

            # 3. Navegar a la página de Clientes
            page.goto("http://localhost:3000/es/dashboard/prestador/mi-negocio/gestion-operativa/genericos/clientes", timeout=60000)
            expect(page.get_by_role("heading", name="Mis Clientes (CRM)")).to_be_visible()
            print("Página de Clientes cargada correctamente.")

            # 4. Tomar captura de pantalla de la página de Clientes
            page.screenshot(path="jules-scratch/verification/verification.png")
            print("Verificación completada. Captura de pantalla guardada.")

        except Exception as e:
            print(f"Ocurrió un error durante la verificación: {e}")
            page.screenshot(path="jules-scratch/verification/error.png")
        finally:
            browser.close()

if __name__ == "__main__":
    run()
