# Backend de SaritaUnificado

## Estado Actual del Proyecto (Post-Estabilización)

Este backend ha sido sometido a un proceso de estabilización intensivo para resolver errores críticos que impedían su arranque y funcionamiento básico. El objetivo principal de esta fase fue lograr un estado funcional desde el cual se pudiera continuar con el desarrollo y la auditoría.

El estado actual es **estable pero neutralizado**.

### Decisiones de Estabilización Clave

Para lograr la estabilidad, se tomaron las siguientes decisiones estratégicas:

1.  **Neutralización de Aplicaciones Incompletas:**
    *   Las aplicaciones `empresa`, `restaurante` y `turismo` se encontraron en un estado de desarrollo incompleto, causando múltiples `ImportError` y `ModuleNotFoundError`.
    *   **Solución:** Se neutralizaron temporalmente estas aplicaciones:
        *   Se crearon archivos `models.py` vacíos para resolver las dependencias de importación.
        *   Se comentó todo el contenido de sus respectivos `views.py`, `serializers.py` y `urls.py`.
        *   Se comentaron en `INSTALLED_APPS` en `settings.py`.

2.  **Neutralización del Sistema de Agentes de IA:**
    *   El sistema de agentes (`agents`) presentaba `NameError`s que impedían el arranque del servidor.
    *   **Solución:** Se neutralizó el sistema comentando las importaciones y las URLs relacionadas en `api/views.py` y `api/urls.py`.

3.  **Corrección de Dependencias Cruzadas:**
    *   Se resolvieron numerosos `ImportError` causados por una refactorización previa en la que modelos como `CategoriaPrestador` fueron movidos de la aplicación `api` a `prestadores` sin actualizar todas sus referencias.

4.  **Actualización de Configuraciones:**
    *   Se corrigieron advertencias de `django-allauth` en `settings.py`, actualizando la configuración a las directivas modernas para el inicio de sesión y registro por email (`ACCOUNT_LOGIN_METHODS` y `ACCOUNT_SIGNUP_FIELDS`).
    *   Se creó el directorio `static` que faltaba.

### ¿Cómo Ejecutar el Backend?

1.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Aplicar migraciones:**
    *   Como parte de la estabilización, es posible que se necesite reconstruir la base de datos.
    ```bash
    rm db.sqlite3
    python manage.py makemigrations
    python manage.py migrate
    ```

3.  **Crear un superusuario (opcional):**
    ```bash
    python manage.py createsuperuser
    ```

4.  **Ejecutar el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```
    El servidor estará disponible en `http://localhost:8000`.

## Próximos Pasos

Con el backend en un estado estable, los próximos pasos son:
1.  Completar la auditoría funcional para entender el comportamiento actual de la API.
2.  Proceder con la refactorización lógica y física del panel de prestadores bajo la nueva arquitectura "Mi Negocio".
3.  Reactivar y completar el desarrollo de las aplicaciones neutralizadas (`empresa`, `restaurante`, `turismo`) una por una.
