# Inventario del Sistema Sarita - Fase de Auditoría

## Estructura de Vías (Triple Vía)

### 🔹 Vía 1: Corporaciones / Gobierno (Admin Plataforma)
- **Backend:** `backend/apps/admin_plataforma/`
  - Control de gobernanza, políticas, auditoría y supervisión transversal.
  - Gestión de destinos, rutas e inventarios turísticos.
- **Frontend:** `frontend/src/app/dashboard/admin_plataforma/`
  - Paneles de analítica, inteligencia, gobernanza y optimización.

### 🔹 Vía 2: Empresarios (Prestadores de Servicios)
- **Backend:** `backend/apps/prestadores/mi_negocio/`
  - **Módulos Core:**
    1. Gestión Comercial: `gestion_comercial/` (Funnels, Marketing, Sales, AI)
    2. Gestión Contable: `gestion_contable/` (Activos, Compras, Nómina, Impuestos)
    3. Gestión Operativa: `gestion_operativa/` (Módulos especializados por tipo de prestador)
    4. Gestión Financiera: `gestion_financiera/` (Presupuestos, flujo de caja)
    5. Gestión Archivística: `gestion_archivistica/` (Documentación legal, DIAN)
- **Frontend:** `frontend/src/app/dashboard/prestador/mi-negocio/`
  - Interfaces correspondientes a los 5 módulos core.

### 🔹 Vía 3: Turista (Cara al Cliente)
- **Backend:** `backend/apps/web_funnel/`
- **Frontend:**
  - `web-ventas-frontend/`: Landing pages y embudos de venta.
  - `frontend/src/app/descubre/`: Exploración de destinos.
  - `frontend/src/app/directorio/`: Directorio de prestadores.

## Componentes Críticos de Inteligencia (SADI / SARITA)
- **Backend Agents:** `backend/apps/sarita_agents/`
  - Jerarquía Militar: General -> Coroneles -> Capitanes -> Tenientes.
  - Dominios: Gubernamental, Prestadores, Turistas, Administrador General.
- **SADI Agent:** `backend/apps/sadi_agent/`
  - Orquestador de voz e inteligencia semántica. Endpoints de `/intent/` y `/audio/` activos.
- **Governance Kernel:** `backend/apps/admin_plataforma/services/governance_kernel.py`
  - Gestiona niveles de autoridad: OPERATIONAL (1), DELEGATED (2), SOVEREIGN (3).

## Mapa de Roles y Permisos (CustomUser)
- **ADMIN:** Super Administrador (Autoridad Soberana).
- **ADMIN_ENTIDAD:** Gobernaciones/Alcaldías.
- **FUNCIONARIO_DIRECTIVO / PROFESIONAL:** Gestión técnica de la entidad.
- **PRESTADOR / ARTESANO:** Usuarios de la Vía 2 (ERP).
- **TURISTA:** Usuario final (Vía 3).

## Estado General Detectado
- **Backend:** Muy estructurado y con lógica densa en dominios comerciales y contables.
- **Frontend:** En proceso de estabilización. Se detectaron errores de dependencias (react-dnd) y uso de placeholders en versiones anteriores.
- **Documentación:** Abundante documentación de arquitectura en la raíz del proyecto.
