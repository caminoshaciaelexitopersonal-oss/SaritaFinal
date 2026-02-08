# INFORME TOTAL DEL SISTEMA "SARITA" - AUDITORÍA INTEGRAL

**Fecha de Auditoría:** 2024-05-24
**Auditor:** Jules (IA Senior Software Engineer)
**Estado Global:** FASE META (Estabilizado y Auditado)

---

## 📘 1. Inventario Total del Sistema

### 📂 Estructura de Raíz
El proyecto está organizado en una arquitectura de monorepositorio con separación clara entre lógica de negocio (Backend), interfaces de usuario (Frontend), y documentación de soberanía.

- **`/backend`**: Núcleo Django con arquitectura modular basada en dominios.
- **`/frontend`**: Interfaz principal (Dashboard ERP y Portal Turístico) construida en Next.js 14.
- **`/web-ventas-frontend`**: Interfaz especializada para embudos de ventas y captación de prestadores.
- **`/DOCUMENTACION`**: Acervo de directrices, actas de cierre y manuales operativos.
- **`/.agents`**: Configuraciones y skills del sistema de agentes inteligentes.

### 📂 Backend (Django Apps) - Análisis por Dominios
El backend se divide en apps que representan los tres pilares (Vías) y la infraestructura de soporte.

#### VÍA 1 - CORPORACIONES / GOBIERNO
- **`apps.admin_plataforma`**: Control central del sistema, gestión de planes, y espejo de los 5 módulos para supervisión global.
- **`apps.governance_live`**: Máquina de estados del sistema (NORMAL a TOTAL DECOUPLING).
- **`apps.operational_treaties`**: Gestión de tratados de interoperabilidad y Kill Switch soberano.
- **`apps.peace_net`**: Monitoreo de riesgos sistémicos e indicadores de estabilidad.
- **`apps.international_interop`**: Pasarela diplomática para nodos federados.

#### VÍA 2 - EMPRESARIOS (PRESTADORES) - "MI NEGOCIO"
Implementado en `backend/apps/prestadores/mi_negocio/`.
1.  **Gestión Comercial**: `gestion_comercial/` - Facturación, clientes, embudos.
2.  **Gestión Operativa**: `gestion_operativa/` - Módulos especializados (Hoteles, Restaurantes, Tours, etc.).
3.  **Gestión Archivística**: `gestion_archivistica/` - Archivo digital con trazabilidad inmutable.
4.  **Gestión Contable**: `gestion_contable/` - Libros contables, nómina, activos fijos.
5.  **Gestión Financiera**: `gestion_financiera/` - Tesorería, flujo de caja.

#### VÍA 3 - TURISTA
- **`api/`**: Contiene los modelos públicos (Atractivos, Publicaciones, Artesanos, Reseñas).
- **`apps.cart`**: Carro de compras para servicios turísticos.
- **`apps.payments`**: Integración con pasarelas de pago (Wompi, etc.).

---

## 📘 2. Informe Técnico

### Backend (Django)
- **Framework**: Django 5.x con Django Rest Framework (DRF).
- **Autenticación**: JWT/Token-based vía `dj-rest-auth`.
- **Base de Datos**: SQLite (en sandbox) / PostgreSQL (producción teórica).
- **Documentación API**: OpenAPI 3.0 estabilizada (Spectacular).
- **Características Especiales**: `SystemicERPViewSetMixin` para trazabilidad automática y `GovernanceKernel` para toma de decisiones asistida por IA.

### Frontend (Next.js 14)
- **Framework**: Next.js 14 con App Router.
- **Estilos**: Tailwind CSS.
- **Contextos**: Centralización de seguridad y estado en `frontend/src/contexts/`.
- **Integración IA**: Capa de voz SADI integrada directamente en el layout del dashboard.

### Estado Real
- **Completo**: Estructura de 5 módulos, Sistema de Agentes, Gobernanza Supranacional.
- **Funcional**: Autenticación por roles, Facturación comercial, Gestión de perfiles, Embudos de venta.
- **En Fase Final**: Integración profunda de "intenciones" de IA con el Backend (estabilizada en la pre-auditoría).

---

## 📘 3. Informe Funcional

### Roles y Capacidades
1.  **SuperAdministrador (ADMIN)**:
    - Control total del ecosistema.
    - Acceso a la "Bitácora de Soberanía" y "Doctrina del Sistema".
    - Capacidad de activar el "Modo Emergencia".
2.  **Prestador (PRESTADOR)**:
    - Acceso al ERP "Mi Negocio" con los 5 módulos operativos.
    - Gestión de inventario, personal (nómina) y facturación.
3.  **Turista (TURISTA)**:
    - Consulta de atractivos, rutas y artesanos.
    - Capacidad de reserva y pago.
4.  **Agentes IA (Digital Servants)**:
    - Ejecución de misiones delegadas con jerarquía militar (General -> Coronel -> Capitán -> Teniente).

---

## 📘 4. Mapa de Flujos Reales

- **Registro de Prestador**: Captura en Funnel -> Creación de Perfil -> Verificación Documental por Admin -> Acceso a Dashboard.
- **Venta de Servicio**: Turista selecciona -> Pago en Pasarela -> Generación de Factura en Gestión Comercial -> Actualización de Inventario en Gestión Operativa.
- **Gobernanza**: Kernel detecta anomalía -> Cambio de Estado Sistémico -> Restricción de permisos delegados.

---

## 📘 5. Diagnóstico de Estabilidad

- **Riesgos**: Dependencia de UUIDs para relaciones cross-module puede ser compleja para reportes SQL directos (se mitiga con serializadores estabilizados).
- **Bloqueos Identificados**: El menú lateral presentaba comportamientos de "círculo infinito" por demoras en la validación del estado `isLoading` del AuthContext, ahora protegido por un timeout de 8 segundos y fallback de re-login.
- **Coherencia**: Se ha verificado que la UI de "Mi Negocio" tiene correspondencia 1:1 con las APIs del Backend.

---

## 🔍 FASE 7 - SISTEMA DE AGENTES (SARITA)
- **Estado**: **FUNCIONAL Y ESTRUCTURADO**.
- **Jerarquía**: Implementada en `apps.sarita_agents.agents.general.sarita.coroneles`.
- **Persistencia**: Registrada en modelos `Mision`, `PlanTáctico` y `TareaDelegada`.
- **Madurez**: Nivel Z4 (Autonomía Supervisada). Los agentes no actúan por libre albedrío; responden a "Directivas" validadas por el Kernel.

---

## 🏛️ FASE 8 - SUPER ADMIN Y GOBERNANZA
- **Diagnóstico**: El Super Admin es el **Gobernante Técnico** del sistema. No es un rol superficial.
- **Control Real**: Puede suspender tratados (Kill Switch), modificar reglas de scoring y auditar cualquier transacción del ERP.
- **Veredicto**: Listo para operación institucional.

---

## 📘 6. PLAN POR FASES (PROPUESTO)

1.  **Fase de Integración Cognitiva**: Mapeo de campos de los 5 módulos a esquemas de razonamiento para los Tenientes IA.
2.  **Fase de Blindaje Transaccional**: Implementación de firmas digitales para cada documento del Archivo Archivístico.
3.  **Fase de Expansión Territorial**: Activación de nodos nacionales e internacionales vía Peace-Net.

---

**FIN DEL INFORME**
