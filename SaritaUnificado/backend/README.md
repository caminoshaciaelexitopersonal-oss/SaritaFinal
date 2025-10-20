# Backend de Sarita Unificado

Este directorio contiene el backend de la aplicación Sarita Unificado, desarrollado con Django y Django REST Framework.

## Estado Actual

El proyecto se encuentra en un estado estable y funcional después de una fase intensiva de auditoría y corrección de errores. Los servidores de backend y frontend arrancan correctamente, y la comunicación entre ellos a través de la API REST está verificada.

### Decisiones de Arquitectura Clave:

1.  **Autenticación de API con `dj-rest-auth`:**
    *   Se ha configurado `dj-rest-auth` para manejar la autenticación de la API, utilizando `TokenAuthentication`.
    *   El login se realiza exclusivamente a través del campo `email`, con `username` deshabilitado para este propósito. Esto se configuró en `settings.py` con `ACCOUNT_AUTHENTICATION_METHOD = 'email'`.
    *   Las URLs de autenticación de la API se encuentran bajo el prefijo `/api/auth/`, utilizando `dj_rest_auth.urls`.

2.  **Neutralización y Restauración de Módulos:**
    *   Las aplicaciones `empresa`, `restaurante` y `turismo` fueron temporalmente "neutralizadas" (código comentado y migraciones eliminadas) para resolver dependencias circulares y errores de arranque.
    *   Tras estabilizar el núcleo, estas aplicaciones han sido restauradas a `INSTALLED_APPS` para permitir su desarrollo futuro, aunque su contenido sigue siendo un esqueleto.

## Cómo Ejecutar el Proyecto

### Prerrequisitos

*   Python 3.12+
*   Pip (gestor de paquetes de Python)

### Instalación

1.  **Navegar al directorio del backend:**
    ```bash
    cd SaritaUnificado/backend
    ```

2.  **Crear y activar un entorno virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

### Configuración de la Base de Datos

1.  **Eliminar la base de datos anterior (si existe):**
    ```bash
    rm db.sqlite3
    ```

2.  **Crear las migraciones:**
    ```bash
    python manage.py makemigrations
    ```

3.  **Aplicar las migraciones:**
    ```bash
    python manage.py migrate
    ```

### Cargar Datos de Prueba

Para poblar la base de datos con usuarios y contenido de prueba, ejecute el siguiente comando:
```bash
python manage.py setup_test_data
```
Esto creará, entre otros, el usuario `prestador_test@example.com` con la contraseña `password123`.

### Ejecutar el Servidor

```bash
python manage.py runserver
```

El servidor estará disponible en `http://localhost:8000`.
