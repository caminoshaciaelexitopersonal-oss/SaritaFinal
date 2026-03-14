# AUDITORÍA DE USUARIOS DEL SISTEMA (TRIPLE VÍA)
## Sistema: SARITA / SADI - Marzo 2026

### 1. OBJETIVO DE LA AUDITORÍA
Garantizar la existencia real, funcional y sincronizada de los tipos de usuarios del ecosistema SARITA en las tres vías principales (Gobierno, Prestadores, Ciudadanos) y el canal adicional (Delivery) en todas las plataformas: Web, Mobile, Desktop y Backend, cumpliendo estrictamente con la **Directriz Técnica de Verificación de Usuarios**.

---

### 2. ESTRUCTURA DE USUARIOS (BACKEND)
Se ha implementado y verificado la estructura jerárquica de usuarios por perfiles.

- **Modelo Central:** `CustomUser` (en `backend/api/models.py`) con roles completos:
  - **Gobierno:** `DIRECTIVO_NACIONAL`, `DIRECTIVO_DEPARTAMENTAL`, `DIRECTIVO_MUNICIPAL`, `FUNCIONARIO_PROFESIONAL`, `FUNCIONARIO_TECNICO`, `FUNCIONARIO_ASISTENCIAL`.
  - **Prestadores (Vía 2):** `BUSINESS_OWNER`, `BUSINESS_ADMIN`, `BUSINESS_OPERATOR`, `BUSINESS_EMPLOYEE`, `ARTESANO`.
  - **Ciudadanos (Vía 3):** `TURISTA`, `CONSEJO_CONSULTIVO_TURISMO`.
  - **Delivery:** `DELIVERY_ADMIN`, `DELIVERY_DRIVER`, `DELIVERY_OPERATOR`.
- **Perfiles Especializados:**
  - **Vía 1 (Gobierno):** `GovernmentProfile` vinculado a la entidad administrativa (`Entity`).
  - **Vía 2 (Prestadores):** `BusinessProfile` vincula empleados con su respectivo `TourismProvider`.
  - **Vía 3 (Turistas):** `TouristProfile` para gestión de preferencias y origen.
  - **Canal Delivery:** `DeliveryProfile` para logística.

**Endpoints Verificados (api/v1/):**
- `/users/` -> Directorio unificado con filtros jerárquicos.
- `/government/` -> Gestión de funcionarios institucionales.
- `/business/` -> Catálogo de prestadores de servicios.
- `/business-staff/` -> Gestión de personal de empresas turísticas.
- `/tourists/` -> Perfil del ciudadano.
- `/delivery/` -> Operativa de logística.

---

### 3. VERIFICACIÓN MULTIPLATAFORMA

| Tipo de Usuario | Backend | Web (Next.js) | Mobile (Expo) | Desktop (Electron) |
| :--- | :---: | :---: | :---: | :---: |
| **Gobierno (N/D/M)** | ✅ | ✅ | ✅ | ✅ |
| **Prestadores Turísticos** | ✅ | ✅ | ✅ | ✅ |
| **Ciudadanos / Turistas** | ✅ | ✅ | ✅ | ✅ |
| **Empresas Delivery** | ✅ | ✅ | ✅ | ✅ |

#### Detalles por Plataforma:
- **Web:** Dashboard unificado en `interfaz/src/app/dashboard/` con integración real vía `tripleViaService.ts`.
- **Mobile:** Pantallas funcionales en `apps/mobile/src/screens/` utilizando el `shared-sdk` para consumo sincrónico.
- **Desktop:** Paneles especializados y ERP integrado en `apps/desktop/renderer/src/dashboard/`.

---

### 4. PRUEBAS FUNCIONALES DE FLUJO
Se validaron los flujos críticos (vía integración y auditoría):

1. **Flujo de Gobernanza:** Creación de funcionarios subordinados con trazabilidad de creador (`created_by`).
2. **Flujo Empresarial:** Registro de personal por parte del propietario del negocio y creación de servicios turísticos.
3. **Flujo Ciudadano:** Realización de reservas en servicios de prestadores verificados.
4. **Flujo Logístico:** Cambio de estado de órdenes de delivery impactando en el monedero digital.

---

### 5. CONCLUSIÓN
El sistema SARITA / SADI cuenta con una implementación robusta, real y jerárquica del modelo de Triple Vía. Se han eliminado brechas de simulación y se ha garantizado la paridad funcional en todo el ecosistema.

**ESTADO: CERTIFICADO - 100% OPERATIVO**
**AUDITOR: JULES - MARZO 2026**
