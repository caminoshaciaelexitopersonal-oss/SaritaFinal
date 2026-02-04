# MODULOS OPERATIVOS ESPECIALIZADOS - SARITA

**Fecha:** 24 de Mayo de 2024
**Estado:** Auditoría de Especialización

## 1. MATRIZ DE ESPECIALIZACIÓN (VÍA 2)

### 🏨 HOTELES Y ALOJAMIENTOS
- **Capacidades:** Gestión de tipos de habitación (`RoomType`), amenidades y stock de unidades.
- **Estado:** ✅ REAL. Conectado a `/v1/mi-negocio/operativa/hotel/room-types/`.
- **UI:** Renderiza inventario real y permite auditoría de unidades.

### 🍽️ RESTAURANTES Y GASTRONOMÍA
- **Capacidades:** Plano de mesas interactivo, estados de ocupación (Libre/Ocupada/Sucia).
- **Estado:** ✅ REAL. Conectado a `/v1/mi-negocio/operativa/restaurante/tables/`.
- **UI:** Visualización de salón operativa.

### 🗺️ GUÍAS Y TURISMO
- **Capacidades:** Gestión de habilidades del guía y catálogo de tours.
- **Estado:** ⚠️ INTEGRADO. Backend preparado en `modulos_especializados/guias`.
- **UI:** Visualización de rutas y disponibilidad.

### 🚐 TRANSPORTE Y LOGÍSTICA
- **Capacidades:** Control de flota, mantenimiento y conductores.
- **Estado:** 🟡 PLANTILLA OPERATIVA. UI detallada con vehículos estáticos, backend preparado para recepción de datos en `modulos_especializados/transporte`.

## 2. DIFERENCIACIÓN UI/UX
- Cada tipo de negocio (Hotel, Restaurante, etc.) accede a una interfaz optimizada para su flujo crítico de trabajo, asegurando que la herramienta sea un habilitador operativo y no una carga administrativa.

## 3. PRÓXIMOS PASOS
- Sincronización total de los estados de limpieza en hoteles y tiempos de preparación en cocina para restaurantes vía SADI.
