# ETAPA 1: BUILDER
# Propósito: Instalar dependencias en un entorno con herramientas de compilación.
FROM python:3.11-slim as builder

# --- Configuración del Entorno ---
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# --- Instalación de Dependencias del Sistema Operativo ---
RUN apt-get update && apt-get install -y --no-install-recommends gcc build-essential libpq-dev

# --- Instalación de Dependencias de Python ---
WORKDIR /opt/venv
RUN python -m venv .
ENV PATH="/opt/venv/bin:$PATH"

COPY ./backend/requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# ==============================================================================
# ETAPA 2: RUNNER (Imagen Final de Producción)
# Propósito: Crear una imagen final ligera y segura, sin herramientas de build.
# ==============================================================================
FROM python:3.11-slim

# --- Configuración del Entorno de Producción ---
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=puerto_gaitan_turismo.settings

# --- Creación de Usuario no-root ---
RUN addgroup --system appgroup && adduser --system --group appuser

# --- Creación del Directorio de la Aplicación ---
WORKDIR /app
RUN mkdir -p /app/staticfiles && chown -R appuser:appgroup /app

# --- Copia de Archivos ---
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY ./backend /app
RUN chown -R appuser:appgroup /app

# --- Preparación Final ---
USER appuser
RUN python manage.py collectstatic --noinput

# --- Ejecución ---
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "--log-level", "info", "puerto_gaitan_turismo.wsgi:application"]
