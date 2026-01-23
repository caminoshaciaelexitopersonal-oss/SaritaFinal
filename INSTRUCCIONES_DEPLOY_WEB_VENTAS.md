# Instrucciones para el Despliegue del Frontend de Ventas (`web-ventas-frontend`)

## 1. Contexto

Se ha realizado una refactorización arquitectónica para separar el frontend de la **Web de Ventas** del frontend del **Dashboard de la Aplicación**, tal como se solicitó.

*   El frontend del Dashboard reside en `/frontend`.
*   El nuevo frontend de la Web de Ventas reside en `/web-ventas-frontend`.

**ADVERTENCIA IMPORTANTE:** Mi entorno de desarrollo no me permite modificar la configuración de orquestación de contenedores (como `docker-compose.yml`) ni los scripts de CI/CD.

Por lo tanto, aunque todos los archivos de la aplicación `web-ventas-frontend` están en su lugar y listos para ser construidos, el sistema **no la ejecutará automáticamente**.

## 2. Pasos Requeridos por el Administrador del Sistema

Para completar el despliegue de la nueva arquitectura, es necesario realizar los siguientes cambios en la configuración de su entorno:

### 2.1. Actualizar `docker-compose.yml`

Deberá añadir un nuevo servicio para el frontend de ventas. A continuación se muestra un **ejemplo** de cómo podría ser este servicio. Deberá adaptarlo a su configuración específica (redes, volúmenes, etc.).

```yaml
services:
  # ... (tus servicios existentes como backend, frontend, db, etc.)

  # NUEVO SERVICIO PARA LA WEB DE VENTAS
  web-ventas:
    build:
      context: ./web-ventas-frontend
      dockerfile: Dockerfile # Necesitarás crear este Dockerfile
    container_name: web-ventas
    restart: unless-stopped
    ports:
      - "3001:3001" # Expone el puerto 3001
    environment:
      - NODE_ENV=development # O production
      # Añade otras variables de entorno necesarias
    volumes:
      - ./web-ventas-frontend:/app
      - /app/node_modules
      - /app/.next
```

### 2.2. Crear un `Dockerfile` para la Web de Ventas

Dentro del directorio `web-ventas-frontend`, necesitará crear un `Dockerfile`. Puede usar el `Dockerfile` del frontend existente como plantilla.

**Ejemplo de `web-ventas-frontend/Dockerfile`:**

```dockerfile
FROM node:20-slim

WORKDIR /app

# Copiar package.json y lockfile
COPY package*.json ./
RUN npm install

# Copiar el resto de los archivos de la aplicación
COPY . .

# Exponer el puerto
EXPOSE 3001

# Comando para iniciar
CMD ["npm", "run", "dev"]
```

### 2.3. Configuración del Proxy Inverso (Nginx, etc.)

Asegúrese de que su proxy inverso esté configurado para dirigir el tráfico de su dominio público (ej. `www.su-dominio.com`) al puerto del contenedor de la web de ventas (ej. `3001`), y el tráfico del dominio del dashboard (ej. `app.su-dominio.com`) al puerto del contenedor del frontend original (ej. `3000`).

## 3. Conclusión

Una vez que estos pasos de configuración del entorno se hayan completado, la arquitectura de frontends separados estará completamente operativa. Todos los archivos de código fuente están listos y en su lugar.
