# Checklist de Despliegue a Producción - Sistema Sarita

Este documento proporciona una lista de verificación exhaustiva para el despliegue del sistema Sarita en un entorno de producción. Seguir estos pasos metódicamente es crucial para garantizar un lanzamiento estable y seguro.

---

## Fase 1: Pre-Despliegue y Preparación

| Tarea | Estado | Notas |
| :--- | :--- | :--- |
| **1.1. Congelación de Código** | `[ ]` | Confirmar que la rama a desplegar (`main` o `release`) está congelada y todas las pruebas han pasado. |
| **1.2. Backup de la Base de Datos** | `[ ]` | Realizar y verificar un backup completo de la base de datos de producción existente antes de aplicar cualquier cambio. |
| **1.3. Variables de Entorno** | `[ ]` | Asegurarse de que el archivo `.env` de producción esté completo y configurado correctamente. |
| &nbsp;&nbsp;&nbsp; `DJANGO_SECRET_KEY` | `[ ]` | Debe ser una clave segura y única para producción. |
| &nbsp;&nbsp;&nbsp; `DEBUG` | `[ ]` | **Debe estar en `False`**. |
| &nbsp;&nbsp;&nbsp; `ALLOWED_HOSTS` | `[ ]` | Debe contener el dominio de producción. |
| &nbsp;&nbsp;&nbsp; `DATABASE_URL` | `[ ]` | Apuntar a la base de datos de producción (PostgreSQL recomendado). |
| &nbsp;&nbsp;&nbsp; `CELERY_BROKER_URL` | `[ ]` | Apuntar al broker de Celery de producción (Redis o RabbitMQ). |
| &nbsp;&nbsp;&nbsp; `CORS_ALLOWED_ORIGINS` | `[ ]` | Configurado para el dominio del frontend de producción. |
| &nbsp;&nbsp;&nbsp; API Keys (SendGrid, Pasarelas, etc.) | `[ ]` | Todas las claves deben ser las de producción. |

## Fase 2: Despliegue del Backend (Django)

| Tarea | Estado | Notas |
| :--- | :--- | :--- |
| **2.1. Actualizar Código** | `[ ]` | `git pull` en la rama de producción en el servidor. |
| **2.2. Instalar Dependencias** | `[ ]` | `pip install -r requirements.txt` dentro del entorno virtual. |
| **2.3. Aplicar Migraciones** | `[ ]` | `python backend/manage.py migrate` |
| **2.4. Recolectar Archivos Estáticos** | `[ ]` | `python backend/manage.py collectstatic --noinput` |
| **2.5. Reiniciar Servicios del Backend** | `[ ]` | Reiniciar el servidor de aplicaciones (Gunicorn/uWSGI) y los workers de Celery. |

## Fase 3: Despliegue del Frontend (Next.js)

| Tarea | Estado | Notas |
| :--- | :--- | :--- |
| **3.1. Actualizar Código** | `[ ]` | `git pull` en la rama de producción en el servidor. |
| **3.2. Instalar Dependencias** | `[ ]` | `npm install` o `yarn install`. |
| **3.3. Construir la Aplicación** | `[ ]` | `npm run build` o `yarn build`. |
| **3.4. Reiniciar Servicio del Frontend** | `[ ]` | Reiniciar el servidor de Node.js (ej. `pm2 restart frontend`). |

## Fase 4: Verificación Post-Despliegue

| Tarea | Estado | Notas |
| :--- | :--- | :--- |
| **4.1. Revisar Logs** | `[ ]` | Monitorear los logs de Gunicorn, Nginx y Celery en busca de errores de inicio. |
| **4.2. Probar la API** | `[ ]` | Realizar una petición a un endpoint clave (ej. `/api/health-check/`) para confirmar que el backend responde. |
| **4.3. Probar el Frontend** | `[ ]` | Cargar la página de inicio en un navegador y verificar que se muestra correctamente. |
| **4.4. Flujo de Autenticación** | `[ ]` | Probar el inicio de sesión y el registro de un nuevo usuario. |
| **4.5. Funcionalidad Crítica** | `[ ]` | Realizar una prueba del flujo comercial principal: añadir un plan al carro y llegar al checkout. |
| **4.6. Comando de Voz (SADI)** | `[ ]` | Probar un comando de voz simple desde el panel de admin para verificar la conexión con la API de SADI. |
| **4.7. Limpiar Caché** | `[ ]` | Limpiar cualquier caché relevante (CDN, Cloudflare, caché del navegador) si es necesario. |

---

Una vez que todas las casillas de verificación estén marcadas, el despliegue se considerará **exitoso**.
