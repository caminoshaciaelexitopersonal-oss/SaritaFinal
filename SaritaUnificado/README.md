# Sarita Unificado

Este proyecto es una plataforma de turismo multi-entidad, diseñada para ser una solución robusta, escalable y personalizable para diferentes organizaciones turísticas (municipales, departamentales, etc.).

El backend está construido con Django y Django REST Framework, mientras que el frontend es una aplicación moderna con Next.js y React.

## Requisitos

- Python 3.10+
- Node.js 18+
- Docker y Docker Compose (recomendado para desarrollo)

## Instalación y Configuración (Backend)

1.  **Navegar al directorio del backend:**
    ```bash
    cd SaritaUnificado/backend
    ```

2.  **Crear un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instalar dependencias de Python:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplicar migraciones de la base de datos:**
    ```bash
    python manage.py migrate
    ```

5.  **Poblar datos de ubicación (Departamentos y Municipios):**
    Este es un paso crucial para la funcionalidad de registro y ubicación.
    ```bash
    python manage.py load_locations api/data/departamentos_municipios.json
    ```

6.  **Crear un superusuario (opcional, para acceso de admin):**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Iniciar el servidor de desarrollo del backend:**
    ```bash
    python manage.py runserver
    ```
    El backend estará disponible en `http://localhost:8000`.

## Instalación y Configuración (Frontend)

1.  **Navegar al directorio del frontend:**
    ```bash
    cd SaritaUnificado/frontend
    ```

2.  **Instalar dependencias de Node.js:**
    ```bash
    npm install
    ```

3.  **Iniciar el servidor de desarrollo del frontend:**
    ```bash
    npm run dev
    ```
    El frontend estará disponible en `http://localhost:3000`.

## Arquitectura Multi-Entidad

El sistema ahora soporta múltiples entidades, cada una con su propia configuración (nombre, logo, colores).

### ¿Cómo crear una entidad y un administrador?

Actualmente, la creación de entidades y la asignación de administradores se realiza a través del shell de Django, ya que requiere un nivel de acceso elevado.

1.  **Abrir el shell de Django:**
    ```bash
    python manage.py shell
    ```

2.  **Ejecutar el siguiente script en el shell:**
    Reemplaza los valores de ejemplo con los datos que desees.

    ```python
    from api.models import Entity, CustomUser, Profile, Department, Municipality

    # 1. Crear la entidad
    entidad_turismo, created = Entity.objects.get_or_create(
        slug='turismo-meta',
        defaults={
            'name': 'Turismo del Meta',
            'type': 'departamental',
            'primary_color': '#FF5733'
        }
    )
    if created:
        print(f"Entidad '{entidad_turismo.name}' creada.")
    else:
        print(f"Entidad '{entidad_turismo.name}' ya existía.")

    # 2. Crear el usuario administrador de la entidad
    admin_user, created = CustomUser.objects.get_or_create(
        username='admin_meta',
        email='admin_meta@example.com',
        defaults={
            'first_name': 'Admin',
            'last_name': 'Meta',
            'role': CustomUser.Role.ADMIN_ENTIDAD
        }
    )
    if created:
        admin_user.set_password('password123')
        admin_user.save()
        print(f"Usuario '{admin_user.username}' creado.")
    else:
        print(f"Usuario '{admin_user.username}' ya existía.")

    # 3. Crear el perfil y asociar el usuario a la entidad
    profile, created = Profile.objects.get_or_create(
        user=admin_user,
        defaults={'entity': entidad_turismo}
    )
    if not created:
        profile.entity = entidad_turismo
        profile.save()
    print(f"Perfil para '{admin_user.username}' asociado a la entidad '{entidad_turismo.name}'.")
    ```

Una vez completado, puedes iniciar sesión con el usuario `admin_meta` (o el que hayas creado) y la contraseña `password123` para gestionar tu entidad.

---

### Configuración de Subdominios para Desarrollo Local

Para probar la funcionalidad de subdominios (p. ej., `turismo-meta.localhost:3000`), necesitas editar el archivo `hosts` de tu sistema operativo para que estos subdominios apunten a tu máquina local.

1.  **Abrir el archivo `hosts` con permisos de administrador:**
    *   **macOS/Linux:** `sudo nano /etc/hosts`
    *   **Windows:** Abre el Bloc de notas como Administrador y busca `C:\Windows\System32\drivers\etc\hosts`.

2.  **Añadir una línea por cada subdominio que quieras probar:**
    Añade la siguiente línea al final del archivo. Puedes añadir tantos subdominios como necesites.

    ```
    127.0.0.1  turismo-meta.localhost
    ```

3.  **Guardar los cambios.**

Ahora, al visitar `http://turismo-meta.localhost:3000` en tu navegador, el middleware de Django detectará el subdominio `turismo-meta` y cargará la entidad correspondiente.

---

## Ejecutar Pruebas

Las pruebas End-to-End se ejecutan con Playwright.

1.  **Navegar al directorio del frontend:**
    ```bash
    cd SaritaUnificado/frontend
    ```
2.  **Instalar las dependencias de Playwright (si es la primera vez):**
    ```bash
    npx playwright install
    ```
3.  **Ejecutar las pruebas:**
    Asegúrate de que los servidores de backend y frontend estén corriendo.
    ```bash
    npx playwright test
    ```
    **Nota:** Si las pruebas fallan por `timeout` al iniciar el servidor, una estrategia es iniciar el servidor manualmente en una terminal (`npm run dev &`) y luego comentar la sección `webServer` en `playwright.config.ts` antes de ejecutar el comando de prueba.