# SNAPSHOT FUNCIONAL DEL FRONTEND - FASE F0

**Fecha:** 30 de Enero de 2025
**Estado Operativo:** ⚠️ PARCIAL / BLOQUEADO

## 🗺️ Mapeo de Rutas y Estado Real

### 1. Panel del Prestador (/dashboard/prestador)
- **Gestión Comercial:** ❌ BLOQUEADO. El error de react-dnd impide el renderizado de los componentes de embudo y kanban.
- **Gestión Contable:** ⚠️ VISUAL. Estructura de tablas y formularios presente, pero depende de mocks para funcionalidad completa.
- **Gestión Operativa:** ✅ FUNCIONAL (Base). Se visualizan los módulos especializados por categoría (Hoteles, Restaurantes).
- **Gestión Archivística:** ✅ FUNCIONAL (Base). Carga de documentos y tablas de archivos operativas.

### 2. Panel del SuperAdmin (/dashboard/admin_plataforma)
- **Inteligencia Decisora:** ✅ FUNCIONAL (UI). Panel de auditoría IA y aprobación de propuestas estratégicas visible.
- **Optimización:** ✅ FUNCIONAL (UI). Métricas de rendimiento y motor de optimización visualmente operativos.
- **Gobernanza Web:** ⚠️ PARCIAL. El listado de páginas depende de la respuesta del backend CMS.

### 3. Portal del Turista (/descubre, /directorio)
- **Directorio:** ✅ FUNCIONAL. Mapa interactivo y listado de prestadores operativo con datos reales/mock.
- **Atractivos:** ✅ FUNCIONAL. Listado y detalle de sitios turísticos.
- **Agenda:** ✅ FUNCIONAL. Calendario de eventos operativo.

### 4. Embudo de Ventas (web-ventas-frontend)
- **Landing Conversacional:** ✅ FUNCIONAL (UI). La interfaz de chat con SARITA carga correctamente.
- **Checkout:** ❌ BLOQUEADO. Los errores de importación impiden la compilación y prueba de este flujo.

## 🚧 Identificación de Placeholders y "En Construcción"
- Los módulos de CRM Avanzado y Analíticas Predictivas en el Dashboard Comercial muestran placeholders de "Próximamente" o dependen de componentes AI que no cargan por falta de SDKs.
- Las páginas de Configuración Global en el SuperAdmin tienen secciones marcadas como experimentales.

---
**Fase F0 - Paso 5 Completado.**
- Se ha mapeado el estado funcional base.
- Se confirman los bloqueos críticos que impiden una navegación E2E fluida.
