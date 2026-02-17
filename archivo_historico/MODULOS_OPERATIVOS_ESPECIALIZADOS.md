# MODULOS OPERATIVOS ESPECIALIZADOS - SARITA (Fase 16)

**Fecha:** 17 de Febrero de 2026
**Estado:** Reestructuración de Dominio `operativa_turistica`

## 1. MATRIZ DE ESPECIALIZACIÓN (VÍA 2)

### 🏨 HOTELES Y ALOJAMIENTOS (Operador Directo)
- **Capacidades:** Gestión de tipos de habitación (`RoomType`), amenidades y stock de unidades.
- **Estado:** ✅ REAL. Ubicado en `operativa_turistica/operadores_directos/hoteles`.
- **UI:** Renderiza inventario real y permite auditoría de unidades.

### 🍽️ RESTAURANTES Y GASTRONOMÍA (Operador Directo)
- **Capacidades:** Plano de mesas interactivo, estados de ocupación (Libre/Ocupada/Sucia).
- **Estado:** ✅ REAL. Ubicado en `operativa_turistica/operadores_directos/restaurantes`.
- **UI:** Visualización de salón operativa.

### 🗺️ GUÍAS Y TURISMO (Operador Directo)
- **Capacidades:** Gestión de habilidades del guía, tours y liquidación de comisiones.
- **Estado:** ✅ REAL. Ubicado en `operativa_turistica/operadores_directos/guias`.
- **UI:** Visualización de rutas y disponibilidad.

### 🚐 TRANSPORTE TURÍSTICO (Operador Directo)
- **Capacidades:** Control de flota, conductores, programación de viajes y reservas con control de capacidad.
- **Estado:** ✅ REAL. Ubicado en `operativa_turistica/operadores_directos/transporte`.

### 🎨 ARTESANOS (Cadena Productiva Turística)
- **Capacidades:** Gestión de materias primas, órdenes de producción de taller y bitácora de consumo automático.
- **Estado:** ✅ REAL. Ubicado en `operativa_turistica/cadena_productiva/artesanos`.
- **Anclaje:** Activación automática tras aprobación gubernamental (Vía 1).

## 2. ARQUITECTURA DE DOMINIO
La Operativa Turística se divide en dos grandes ramas para garantizar la coherencia semántica:
1. **Operadores Directos:** Servicios que el turista consume directamente (Cama, Comida, Guía, Transporte, Agencias, Bares).
2. **Cadena Productiva:** Actores económicos vinculados que proveen la experiencia cultural y productiva (Artesanos).

## 3. GOBERNANZA INTEGRADA
Todos los módulos están gobernados por el `CoronelOperativaTuristica` y el `GovernanceKernel`, integrando:
- **Monedero Soberano:** Para pagos y liquidaciones.
- **Quintuple ERP:** Para trazabilidad contable y financiera.
- **Ejército de Agentes:** Para automatización de flujos operativos.
