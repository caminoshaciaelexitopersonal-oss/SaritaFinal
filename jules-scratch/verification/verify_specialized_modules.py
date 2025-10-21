# jules-scratch/verification/verify_specialized_modules.py
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()

    # Iniciar sesión
    page.goto("http://localhost:3000/login", timeout=60000)
    page.get_by_label("Email").fill("prestador_test@example.com")
    page.get_by_label("Password").fill("password123")
    page.get_by_role("button", name="Login").click()
    page.wait_for_url("http://localhost:3000/dashboard")

    # Módulos Especializados
    base_url = "http://localhost:3000/dashboard/prestador/mi-negocio/gestion-operativa/especializados"

    modules = [
        ("hoteles/habitaciones", "hoteles_habitaciones.png"),
        ("hoteles/servicios-adicionales", "hoteles_servicios_adicionales.png"),
        ("restaurantes/menu", "restaurantes_menu.png"),
        ("restaurantes/mesas", "restaurantes_mesas.png"),
        ("guias/rutas", "guias_rutas.png"),
        ("guias/equipamiento", "guias_equipamiento.png"),
        ("transporte/vehiculos", "transporte_vehiculos.png"),
        ("transporte/conductores", "transporte_conductores.png"),
        ("agencias/paquetes", "agencias_paquetes.png"),
        ("agencias/itinerarios", "agencias_itinerarios.png"),
        ("artesanos/catalogo", "artesanos_catalogo.png"),
        ("artesanos/pedidos", "artesanos_pedidos.png"),
    ]

    for path, screenshot_name in modules:
        page.goto(f"{base_url}/{path}")
        page.screenshot(path=f"jules-scratch/verification/{screenshot_name}")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
