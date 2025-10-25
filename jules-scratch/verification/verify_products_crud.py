from playwright.sync_api import sync_playwright, expect
import time

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # Iniciar sesión
    page.goto("http://localhost:3000/es/login")
    expect(page.get_by_role("heading", name="Iniciar Sesión")).to_be_visible()
    page.get_by_label("Nombre de Usuario").fill("prestador")
    page.get_by_label("Contraseña").fill("prestador")
    page.get_by_role("button", name="Iniciar Sesión").click()
    expect(page).to_have_url("http://localhost:3000/es/dashboard/prestador", timeout=10000)

    # Navegar a Productos/Servicios
    page.goto("http://localhost:3000/es/dashboard/prestador/mi-negocio/gestion-operativa/genericos/productos-servicios")

    # Verificar que la tabla está vacía
    expect(page.get_by_text("No has añadido ningún producto o servicio todavía.")).to_be_visible()

    # Crear un nuevo producto
    page.get_by_role("button", name="Añadir Nuevo").click()
    expect(page.get_by_role("heading", name="Añadir Nuevo Producto/Servicio")).to_be_visible()
    page.get_by_label("Nombre").fill("Servicio de Prueba de Jules")
    page.get_by_label("Precio").fill("15000")
    page.get_by_label("Descripción").fill("Esta es una descripción de prueba.")
    page.get_by_role("button", name="Guardar").click()

    # Verificar que el nuevo producto aparece en la tabla
    expect(page.get_by_text("Servicio de Prueba de Jules")).to_be_visible()
    expect(page.get_by_text("$15,000.00")).to_be_visible()
    page.screenshot(path="jules-scratch/verification/01_product_created.png")

    # Editar el producto
    page.get_by_role("button", name="Editar").first.click()
    expect(page.get_by_role("heading", name="Editar Producto/Servicio")).to_be_visible()
    page.get_by_label("Nombre").fill("Servicio Editado por Jules")
    page.get_by_role("button", name="Guardar").click()

    # Verificar que el producto fue editado
    expect(page.get_by_text("Servicio Editado por Jules")).to_be_visible()
    page.screenshot(path="jules-scratch/verification/02_product_edited.png")

    # Eliminar el producto
    page.get_by_role("button", name="Eliminar").first.click()

    # Aceptar el diálogo de confirmación
    page.once("dialog", lambda dialog: dialog.accept())

    # Esperar a que la UI se actualice después de la eliminación
    expect(page.get_by_text("No has añadido ningún producto o servicio todavía.")).to_be_visible()
    page.screenshot(path="jules-scratch/verification/03_product_deleted.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
