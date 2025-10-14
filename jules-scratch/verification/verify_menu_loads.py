from playwright.sync_api import sync_playwright, expect, TimeoutError

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # Capturar eventos de la consola
    page.on("console", lambda msg: print(f"CONSOLE: {msg.text}"))

    try:
        # 1. Navegar a la página de inicio
        page.goto("http://localhost:3000", wait_until="domcontentloaded")

        # 2. Esperar a que un elemento del menú sea visible
        discover_link = page.get_by_role("link", name="Descubre")

        # 3. Verificar que el enlace es visible
        expect(discover_link).to_be_visible(timeout=20000)

        # 4. Tomar la captura de pantalla de éxito
        page.screenshot(path="jules-scratch/verification/menu-verification.png")
        print("Screenshot taken successfully.")

    except TimeoutError as e:
        print(f"Timeout error: {e}")
        page.screenshot(path="jules-scratch/verification/error.png")
        print("Error screenshot taken.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        page.screenshot(path="jules-scratch/verification/unexpected_error.png")
    finally:
        browser.close()

with sync_playwright() as playwright:
    run(playwright)