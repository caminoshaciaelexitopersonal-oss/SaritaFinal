# ARQUITECTURA UX MAESTRA — SISTEMA SARITA

## 1. Jerarquía de Navegación Global

El sistema se organiza en una estructura de 4 niveles de profundidad para garantizar la escalabilidad y el orden lógico de la información.

### 🔴 Nivel 0 — Capa de Sistema (Soberanía)
**Propósito:** Visión panorámica y control crítico.
- **Estado Global:** Indicadores de salud del ecosistema (Kernel status).
- **Alertas Críticas:** Centro de notificaciones de gobernanza.
- **Actividad en Tiempo Real:** Monitor de transacciones y misiones de agentes.
- **Ubicación:** Dashboard Central / Topbar persistente.

### 🟠 Nivel 1 — Dominios de Negocio
**Propósito:** Agrupación lógica de capacidades funcionales.
- **Técnico:** Infraestructura, logs y configuración base.
- **Comercial:** Embudos, marketing y gestión de leads.
- **Operativo:** Gestión diaria del prestador (reservas, habitaciones, rutas).
- **Administrativo:** Gestión de usuarios, permisos y auditoría.
- **Contable:** Registro de transacciones, libros y cumplimiento fiscal.
- **Financiero:** Tesorería, flujo de caja y proyecciones.
- **Analítica / IA:** Inteligencia decisora y optimización.

### 🟡 Nivel 2 — Módulos Especializados
**Propósito:** Herramientas específicas dentro de un dominio.
*Ejemplo Dominio Financiero:*
- Flujo de Caja
- Ingresos / Egresos
- Proyecciones de ROI
- Gestión de Impuestos
- Reportes Maestros

### 🟢 Nivel 3 — Vistas de Detalle (Operación)
**Propósito:** Interacción directa con los datos.
- **Listado:** Tablas con filtros inteligentes.
- **Detalle:** Ficha profunda de un registro.
- **Comparativa:** Análisis entre periodos o nodos.
- **Histórico:** Trazabilidad de cambios (Audit Log).
- **Simulación:** Capa de "What-if" para análisis predictivo (IA).

---

## 2. Mapa Maestro de Flujos

### Flujo de Gobernanza (SuperAdmin)
`Sistema (L0) -> Analítica (L1) -> Inteligencia Decisora (L2) -> Propuesta Estratégica (L3)`

### Flujo Operativo (Prestador)
`Dashboard (L0) -> Operativo (L1) -> Reservas (L2) -> Ficha de Cliente (L3)`

### Flujo de Crecimiento (Ventas)
`Marketing (L1) -> Embudos (L2) -> Simulación de Conversión (L3)`

---

## 3. Principios de Composición
1. **Contexto Persistente:** El usuario siempre sabe en qué Dominio y Módulo se encuentra (vía Breadcrumbs y Sidebar).
2. **Navegación No-Lineal:** Capacidad de saltar entre dominios relacionados (ej: de Venta a Asiento Contable) mediante "links semánticos".
3. **Profundidad Controlada:** No superar los 3 niveles de click para alcanzar una acción operativa.
