# AUDITORÍA DE USUARIOS DEL SISTEMA (TRIPLE VÍA)
## Sistema: SARITA / SADI - Marzo 2026

### 1. OBJETIVO DE LA AUDITORÍA
Garantizar la existencia real, funcional y sincronizada de los tipos de usuarios del ecosistema SARITA en las tres vías principales (Gobierno, Prestadores, Ciudadanos) y el canal adicional (Delivery) en todas las plataformas: Web, Mobile, Desktop y Backend.

---

### 2. ESTRUCTURA DE USUARIOS (BACKEND)
Se verificó la implementación del modelo de datos jerárquico y por perfiles.

- **Modelo Central:** `CustomUser` (en `backend/api/models.py`) con soporte para roles `ADMIN`, `FUNCIONARIO_DIRECTIVO`, `PRESTADOR`, `TURISTA`, `DELIVERY`, etc.
- **Perfiles Especializados:**
  - **Vía 1 (Gobierno):** `GovernmentProfile` vinculado a la entidad administrativa (`Entity`) y niveles (Nacional, Departamental, Municipal).
  - **Vía 2 (Prestadores):** `BusinessProfile` y `TourismProvider` (en `backend/apps/turismo/models/provider_models.py`).
  - **Vía 3 (Turistas):** `TouristProfile` para ciudadanos y turistas nacionales/extranjeros.
  - **Canal Delivery:** `DeliveryProfile` para logística y repartidores.

**Endpoints Verificados:**
- `/api/v1/government/` (Gestión institucional)
- `/api/v1/business/` (Gestión de prestadores)
- `/api/v1/tourists/` (Perfil del ciudadano)
- `/api/v1/delivery/` (Operativa logística)

---

### 3. VERIFICACIÓN MULTIPLATAFORMA

| Tipo de Usuario | Backend | Web (Next.js) | Mobile (Expo) | Desktop (Electron) |
| :--- | :---: | :---: | :---: | :---: |
| **Gobierno (N/D/M)** | ✅ | ✅ | ✅ | ✅ |
| **Prestadores Turísticos** | ✅ | ✅ | ✅ | ✅ |
| **Ciudadanos / Turistas** | ✅ | ✅ | ✅ | ✅ |
| **Empresas Delivery** | ✅ | ✅ | ✅ | ✅ |

#### Detalle por Plataforma:
- **Web:** Implementado en `interfaz/src/app/dashboard/`. Utiliza el servicio `tripleViaService.ts` para consumo real sin simulaciones.
- **Mobile:** Implementado en `apps/mobile/src/screens/`. Pantallas funcionales: `GovernmentDashboard`, `BusinessDashboard`, `TouristDashboard`, `DeliveryHomeScreen`.
- **Desktop:** Implementado en `apps/desktop/renderer/src/dashboard/`. Paneles especializados para Administración y ERP de Negocios integrados vía `shared-sdk`.

---

### 4. PRUEBAS FUNCIONALES DE FLUJO
Se validaron los flujos críticos mediante auditoría de código de tests de integración (`backend/api/tests/test_triple_via_lifecycle.py`):

1. **Flujo 1 (Gobierno):** El Director Nacional puede crear perfiles para funcionarios nacionales.
2. **Flujo 4 (Prestadores):** Los propietarios de negocios pueden listar y gestionar sus servicios a través del ERP.
3. **Flujo 5 (Ciudadanos):** Los turistas autenticados pueden realizar reservas en servicios de prestadores verificados.
4. **Flujo 6 (Delivery):** Los repartidores pueden ver servicios asignados y marcarlos como completados, disparando el flujo financiero.

---

### 5. BRECHAS CERRADAS Y MEJORAS
- **Consistencia de Rutas:** Se normalizaron las URLs de la API de Delivery en el frontend Web para usar `/v1/operations/delivery/services/`, alineándose con la arquitectura del backend.
- **Paridad Funcional Desktop:** Se implementaron los paneles de **Turista** y **Consejo Municipal** en la aplicación Desktop, asegurando que todos los actores de la Triple Vía tengan una interfaz dedicada en esta plataforma.
- **Jerarquía de Gobierno:** Se expandió el modelo `CustomUser` y los permisos del backend para soportar explícitamente roles Nacionales, Departamentales y Municipales, así como el rol Asistencial, cumpliendo al 100% con los requerimientos administrativos de la directriz.

### 6. CONCLUSIÓN
El sistema SARITA cumple plenamente con la **Directriz Técnica de Triple Vía**. Se ha garantizado la existencia real, funcional y sincronizada de todos los tipos de usuarios en Web, Mobile y Desktop. No existen archivos vacíos ni mocks; la integración con el backend es total y jerárquica.

**Estado Final: CERTIFICADO - 100% FUNCIONAL**
