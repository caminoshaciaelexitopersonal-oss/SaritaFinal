# Guía de Despliegue - SARITA

Esta guía describe los pasos necesarios para desplegar el sistema SARITA en un entorno de producción.

## 1. Prerrequisitos

-   Servidor (Ubuntu 22.04 o superior recomendado)
-   Docker y Docker Compose
-   Git
-   Credenciales para un servidor de bases de datos PostgreSQL
-   Credenciales para los servicios de Modelos de Lenguaje (LLMs) que se utilizarán

## 2. Configuración del Entorno

### 2.1. Clonar el Repositorio

```bash
git clone <URL_DEL_REPOSITORIO> SaritaUnificado
cd SaritaUnificado
```

### 2.2. Variables de Entorno

Cree un archivo `.env` en el directorio raíz del proyecto (`SaritaUnificado/`) y configure las siguientes variables:

```env
# Backend (Django)
SECRET_KEY=tu_clave_secreta_aqui
DEBUG=False
ALLOWED_HOSTS=tudominio.com,www.tudominio.com
DATABASE_URL=postgres://usuario:contraseña@host:puerto/nombre_db
CORS_ALLOWED_ORIGINS=https://tudominio.com,https://www.tudominio.com

# Modelos de Lenguaje (LLMs)
OPENAI_API_KEY=tu_api_key_de_openai
ANTHROPIC_API_KEY=tu_api_key_de_anthropic
# ...otras claves de API que necesites...

# Frontend (Next.js)
NEXT_PUBLIC_API_URL=https://tudominio.com/api
```

**Nota de Seguridad:** Nunca exponga sus claves secretas ni el archivo `.env` en un repositorio público.

## 3. Construcción y Despliegue con Docker

El proyecto está configurado para ser desplegado utilizando Docker y Docker Compose, lo que simplifica la gestión de los servicios de frontend y backend.

### 3.1. Archivo `docker-compose.yml` (Ejemplo)

A continuación, se muestra un ejemplo de cómo podría ser el archivo `docker-compose.yml` en la raíz del proyecto:

```yaml
version: '3.8'

services:
  backend:
    build:
      context: ./backend
    command: gunicorn core.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - ./backend:/app
      - static_volume:/app/staticfiles
    expose:
      - 8000
    env_file:
      - ./.env

  frontend:
    build:
      context: ./frontend
    command: npm start
    ports:
      - "3000:3000"
    depends_on:
      - backend
    env_file:
      - ./.env

  nginx:
    image: nginx:latest
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - static_volume:/app/staticfiles
      # Montar certificados SSL (recomendado usar Certbot)
      # - /etc/letsencrypt:/etc/letsencrypt
    depends_on:
      - backend
      - frontend

volumes:
  static_volume:
```

### 3.2. Configuración de Nginx

Cree un archivo `nginx.conf` para actuar como proxy inverso y servir los archivos estáticos.

```nginx
# nginx.conf (Ejemplo)

events {}

http {
    server {
        listen 80;
        server_name tudominio.com www.tudominio.com;

        # Redirigir HTTP a HTTPS (recomendado)
        # location / {
        #     return 301 https://$host$request_uri;
        # }

        location / {
            proxy_pass http://frontend:3000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }

        location /api/ {
            proxy_pass http://backend:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }

        location /static/ {
            alias /app/staticfiles/;
        }
    }
}
```

### 3.3. Iniciar los Servicios

1.  **Construir las imágenes de Docker:**

    ```bash
    docker-compose build
    ```

2.  **Ejecutar las migraciones de la base de datos y recolectar archivos estáticos:**

    ```bash
    docker-compose run --rm backend python manage.py migrate
    docker-compose run --rm backend python manage.py collectstatic --noinput
    ```

3.  **Iniciar todos los servicios en segundo plano:**

    ```bash
    docker-compose up -d
    ```

## 4. Tareas Post-Despliegue

-   **Crear un Superusuario:**

    ```bash
    docker-compose run --rm backend python manage.py createsuperuser
    ```

-   **Configurar Certificados SSL:** Se recomienda encarecidamente utilizar Certbot para obtener e instalar certificados SSL gratuitos de Let's Encrypt.

-   **Monitoreo:** Configure herramientas de monitoreo para supervisar el estado de los contenedores, el uso de recursos y los logs de la aplicación.