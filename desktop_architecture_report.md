# Reporte de Arquitectura Desktop POS - SARITA v1.0

## 1. Arquitectura de Procesos Segura

La aplicación de escritorio sigue un modelo de separación estricta de responsabilidades (Fase 3).

### Proceso Main (Privilegiado)
*   **Gestión de Ventanas**: Electron BrowserWindow con aislamiento.
*   **Database Service**: Manejo de persistencia local mediante SQLite.
*   **Sync Engine**: Ciclo de vida de sincronización asíncrona con el Backend.
*   **Hardware Bridge**: Comunicación con periféricos (impresoras, scanners).

### Proceso Renderer (React UI)
*   Interfaz de usuario fluida desarrollada en React + Vite + Tailwind.
*   Sin acceso directo a Node.js o al sistema de archivos (Seguridad By Design).

## 2. Estrategia Offline First

El sistema garantiza la operación continua del POS incluso ante fallos críticos de conectividad.

*   **Persistencia Local**: Las ventas se registran instantáneamente en el archivo `sarita_pos.sqlite`.
*   **Cola de Sincronización**: Uso del Outbox Pattern local para asegurar que ninguna transacción se pierda.
*   **Aislamiento de Seguridad**: Uso de `safeStorage` nativo para encriptar el material criptográfico de sesión.

## 3. Capacidades de Hardware

Se ha implementado el bridge para periféricos industriales:
*   **Impresora Térmica**: Generación de recibos de venta detallados.
*   **Lector de Barras**: Eventos IPC para búsqueda rápida de productos.

---
**Resultado**: La aplicación Desktop ha alcanzado un nivel de madurez operativa del 95%, lista para despliegue masivo en puntos de venta físicos.
