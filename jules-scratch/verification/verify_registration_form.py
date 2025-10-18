import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        try:
            # Navegar a la página de registro
            await page.goto("http://localhost:3000/registro")

            # Rellenar campos comunes
            await page.get_by_label("Correo Electrónico").fill("test.divipola@example.com")
            await page.get_by_label("Nombre de Usuario").fill("testdivipola")
            await page.get_by_label("Contraseña").fill("TestPassword123")
            await page.get_by_label("Confirmar Contraseña").fill("TestPassword123")

            # Seleccionar Departamento
            department_selector = page.get_by_label("Departamento")
            await department_selector.wait_for(state="visible", timeout=10000)
            await department_selector.select_option(label="Amazonas")

            # Esperar a que el selector de municipio se habilite y se cargue
            municipality_selector = page.get_by_label("Municipio")
            await expect(municipality_selector).to_be_enabled(timeout=10000)

            # Esperar a que la opción correcta esté presente
            await expect(municipality_selector.get_by_text("Leticia")).to_be_visible(timeout=5000)

            # Seleccionar Municipio
            await municipality_selector.select_option(label="Leticia")

            # Tomar captura de pantalla
            await page.screenshot(path="jules-scratch/verification/registration_form.png")

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(main())