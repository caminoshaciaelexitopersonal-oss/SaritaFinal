# ETAPA 1: BUILDER
# Propósito: Compilación de dependencias y optimización de espacio.
FROM python:3.11-slim as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/venv
RUN python -m venv .
ENV PATH="/opt/venv/bin:$PATH"

COPY ./backend/requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# ==============================================================================
# ETAPA 2: RUNNER (Imagen Final de Producción)
# ==============================================================================
FROM python:3.11-slim

LABEL maintainer="Sarita Core Team"
LABEL version="1.0-EOS"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=puerto_gaitan_turismo.settings
ENV PORT 8000

# Instalación de librerías compartidas mínimas (libpq para postgres)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    procps \
    && rm -rf /var/lib/apt/lists/*

# Usuario no-root para mayor seguridad
RUN addgroup --system appgroup && adduser --system --group appuser

WORKDIR /app
RUN mkdir -p /app/staticfiles /app/mediafiles && chown -R appuser:appgroup /app

# Copiar entorno virtual optimizado
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copiar código fuente
COPY ./backend /app
RUN chown -R appuser:appgroup /app

# Exponer el puerto
EXPOSE ${PORT}

# Switch to non-root user
USER appuser

# Healthcheck nativo de Docker
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:${PORT}/api/v1/infra/health/liveness/ || exit 1

# Comando de ejecución con Gunicorn configurado para EOS
CMD ["gunicorn", "--bind", "0.0.0.0:8000", \
     "--workers", "4", \
     "--threads", "2", \
     "--worker-class", "gthread", \
     "--timeout", "60", \
     "--access-logfile", "-", \
     "--error-logfile", "-", \
     "puerto_gaitan_turismo.wsgi:application"]
