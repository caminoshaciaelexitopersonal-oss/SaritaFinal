from playwright.sync_api import sync_playwright, expect
import time

def run_verification():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            # 1. Verificar la página de inicio y el menú
            print("Navegando a la página de inicio...")
            page.goto("http://localhost:3000/", timeout=60000)

            print("Esperando 10 segundos para la carga completa...")
            time.sleep(10)

            print("Esperando el enlace 'Descubre'...")
            discover_link = page.get_by_role("link", name="Descubre")
            expect(discover_link).to_be_visible(timeout=20000)

            print("Menú de inicio verificado. Tomando captura...")
            page.screenshot(path="jules-scratch/verification/01_homepage.png")

            # 2. Navegar al Portal de Empleo
            print("Navegando al Portal de Empleo...")
            page.get_by_role("link", name="Empleo").click()

            expect(page.get_by_role("heading", name="Portal de Empleo")).to_be_visible(timeout=15000)
            print("Página de Empleo verificada. Tomando captura...")
            page.screenshot(path="jules-scratch/verification/02_empleo.png")

            # 3. Navegar al Directorio de Guías
            print("Navegando al Directorio de Guías...")
            page.get_by_role("link", name="Descubre").click()
            page.get_by_role("link", name="Guías Turísticos").click()

            expect(page.get_by_role("heading", name="Directorio de Guías Turísticos")).to_be_visible(timeout=15000)
            print("Página de Guías verificada. Tomando captura final...")
            page.screenshot(path="jules-scratch/verification/03_guias.png")

        except Exception as e:
            print(f"Ocurrió un error durante la verificación: {e}")
            page.screenshot(path="jules-scratch/verification/error.png")
        finally:
            browser.close()

if __name__ == "__main__":
    run_verification()