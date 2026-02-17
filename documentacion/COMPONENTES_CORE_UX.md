# COMPONENTES CORE UX — SISTEMA SARITA

## 1. Componentes Universales

### 🔘 Sidebar Dinámica (Contextual)
- **Comportamiento:** Se adapta según el rol autenticado y la categoría del prestador.
- **Jerarquía:** Agrupa por Dominios (L1) y Módulos (L2).
- **Interacción:** Colapsable en dispositivos móviles; persistente en Desktop.
- **Atributo de Voz:** Cada enlace debe poseer un `aria-label` que coincida con el nombre del módulo.

### 🔘 Topbar de Soberanía
- **Propósito:** Control de contexto y estados globales.
- **Elementos:**
    - **Breadcrumbs:** Ruta semántica L0 > L1 > L2.
    - **Buscador Global:** Inteligente, permite comandos rápidos (ej: "Ir a Factura 502").
    - **Indicador de Kernel:** Semáforo visual del estado del backend.
    - **Selector de Tema:** Switch Día/Noche.

### 🔘 Panel de Estado y Alertas
- **Ubicación:** Lateral derecho o Dashboard L0.
- **Función:** Feed de actividad en tiempo real y notificaciones críticas de gobernanza.

---

## 2. Componentes de Datos (Análisis)

### 🔘 Tablas Inteligentes (Enterprise Grid)
- **Paginación:** Server-side obligatoria para grandes volúmenes.
- **Filtros:** Persistentes en la URL para facilitar el compartido de vistas.
- **Exportación:** Acciones rápidas para CSV/PDF/Excel.
- **Modo Densa:** Opción para ver más registros en pantallas tipo NOC.

### 🔘 Gráficas Predictivas (IA Ready)
- **Librería:** Recharts / Chart.js.
- **Tipos:**
    - Comparativas temporales (Barras/Líneas).
    - Distribución (Pie/Donut).
    - Proyecciones IA (Líneas punteadas para "Forecast").

---

## 3. Componentes de Acción (Intención)

### 🔘 Botones con Intención Semántica
- **Primarios (`brand`):** Acciones definitivas (Guardar, Enviar, Ejecutar).
- **Secundarios (`outline`):** Acciones reversibles o de navegación.
- **Críticos (`destructive`):** Bloqueos manuales o borrado permanente.
- **Confirmación:** Diálogos que explican la consecuencia de la acción (vía Kernel).

---

## 4. Estados Visuales (Feedback)
1. **Skeleton Loading:** Estructura gris animada que pre-visualiza el layout final.
2. **Empty State:** Ilustración (SVG) con botón de llamada a la acción (ej: "No hay facturas. Crear primera").
3. **Error Boundary:** Pantalla amigable que permite reintentar o reportar el fallo al Admin Técnico.
