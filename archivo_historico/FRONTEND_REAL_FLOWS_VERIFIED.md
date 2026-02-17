# FRONTEND REAL FLOWS VERIFIED - SARITA

**Fecha:** 24 de Mayo de 2024
**Estado:** Auditoría de Integración Completada

## 🟦 VÍA 1: GOBIERNO / SUPERADMIN
- **Dashboard Principal:** REAL. Consume `/api/dashboard/analytics/` para KPIs de usuarios, publicaciones y prestadores activos.
- **Centro de Soberanía:** REAL/MIXTO. Los indicadores de Kernel y Alertas están mapeados a servicios de backend, aunque la intervención manual se realiza vía `GovernanceKernel`.
- **Gobernanza:** REAL. Los componentes de auditoría visual (AuditLogViewer) están listos para reflejar el rastro de SHA-256 del backend.

## 🟦 VÍA 2: EMPRESARIOS (PRESTADORES)
- **Gestión Comercial (Facturación):** REAL. Integrado con `/api/v1/mi-negocio/comercial/facturas-venta/`.
- **Arquitecto de Embudos:** SIMULADO (MODO DEMO). Renderiza el editor visual vía `react-dnd` pero utiliza persistencia local/mock en esta fase.
- **Marketing Multicanal:** PARCIAL. La UI está lista pero la integración con SADI para ejecución de campañas masivas está en fase de desarrollo.
- **Gestión Operativa:** REAL. Módulos especializados (Hoteles, Restaurantes) tienen sus propias tablas y modelos en el backend.

## 🟦 VÍA 3: TURISTA (CLIENTE FINAL)
- **Portal Descubre:** REAL. Consume `/api/atractivos/`, `/api/rutas-turisticas/` y `/api/galeria-media/`.
- **Directorio:** REAL. Búsqueda y filtrado de prestadores y artesanos conectado al backend.
- **Ventas Web (Funnel):** REAL. La aplicación `web-ventas-frontend` interactúa con el intent engine de SADI para calificación de leads.

## 🟦 ESTADO DE AUTENTICACIÓN
- **Flujo:** Login y Registro 100% operativos con redirección inteligente por rol (SuperAdmin, Prestador, Turista).
- **Redirección:** Verificada la lógica de `AuthContext` que asegura que cada vía acceda a su panel correspondiente.
