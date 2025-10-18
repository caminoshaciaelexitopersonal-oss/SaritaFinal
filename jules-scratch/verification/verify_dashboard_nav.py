import re
import uuid
from playwright.sync_api import sync_playwright, Page, expect

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # Generar credenciales únicas para cada ejecución
    unique_id = str(uuid.uuid4())[:8]
    email = f"restaurante_{unique_id}@example.com"
    username = f"restaurante_{unique_id}"
    password = "password123"

    try:
        # 1. Registrar un nuevo usuario de tipo Restaurante
        page.goto("http://localhost:3000/registro")

        # Llenar campos comunes
        page.get_by_label("Correo Electrónico").fill(email)
        page.get_by_label("Nombre de Usuario").fill(username)
        page.get_by_label("Contraseña", exact=True).fill(password)
        page.get_by_label("Confirmar Contraseña").fill(password)
        page.get_by_label("Quiero registrarme como:").select_option("PRESTADOR")

        # Esperar a que aparezcan los campos de prestador
        expect(page.get_by_label("Nombre del Establecimiento")).to_be_visible()

        # Llenar campos de ubicación y prestador
        # AÑADIDO: Esperar explícitamente a que la opción exista antes de seleccionarla
        expect(page.get_by_role("option", name="Meta")).to_be_visible(timeout=15000)
        page.get_by_label("Departamento").select_option(label="Meta")

        # Esperar a que se carguen los municipios
        expect(page.get_by_label("Municipio")).to_be_enabled()
        page.get_by_label("Municipio").select_option(label="PUERTO GAITAN")
        page.get_by_label("Nombre del Establecimiento").fill(f"Restaurante Sabores {unique_id}")

        # Esperar a que las categorías se carguen
        expect(page.get_by_role("option", name="Restaurante")).to_be_visible(timeout=15000)
        page.get_by_label("Categoría del Servicio").select_option(label="Restaurante")

        page.get_by_role("button", name="Crear Cuenta").click()

        # Esperar al mensaje de éxito
        expect(page.get_by_text("¡Registro exitoso!")).to_be_visible(timeout=10000)

        # 2. Iniciar sesión con el nuevo usuario
        page.goto("http://localhost:3000/login")
        page.get_by_label("Correo Electrónico").fill(username) # Se usa username para login
        page.get_by_label("Contraseña").fill(password)
        page.get_by_role("button", name="Iniciar Sesión").click()

        # 3. Esperar a que el panel cargue y verificar el menú
        expect(page.get_by_role("heading", name="Panel de Control")).to_be_visible(timeout=15000)

        # Abrir las secciones del menú
        page.get_by_role("button", name=re.compile("Panel de Prestador")).click()
        page.get_by_role("button", name=re.compile("Módulos Específicos")).click()

        # Verificar que los enlaces específicos de restaurante son visibles
        expect(page.get_by_role("link", name="Menú/Carta")).to_be_visible()
        expect(page.get_by_role("link", name="Gestión de Mesas")).to_be_visible()
        expect(page.get_by_role("link", name="Pedidos (TPV)")).to_be_visible()

        # 4. Tomar la captura de pantalla
        page.screenshot(path="jules-scratch/verification/dashboard_nav_verification.png")
        print("Screenshot taken successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
        page.screenshot(path="jules-scratch/verification/error.png")
        raise

    finally:
        browser.close()

with sync_playwright() as playwright:
    run(playwright)