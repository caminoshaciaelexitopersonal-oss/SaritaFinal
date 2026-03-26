# AUDITORÍA ESTRUCTURAL Y FUNCIONAL DE USUARIOS (TRIPLE VÍA)
**Sistema:** SARITA / SADI
**Fecha:** Marzo 2026
**Responsable:** Jules (Ingeniero de Sistemas SARITA)

## 1. OBJETIVO DE LA AUDITORÍA
Garantizar la existencia real, funcional y sincronizada de todos los tipos de usuarios del ecosistema turístico en las tres plataformas (Web, Móvil, Escritorio), eliminando simulaciones y asegurando la integración total con el backend.

---

## 2. ESTRUCTURA DE USUARIOS (MODELO TRIPLE VÍA)
El sistema implementa exitosamente el modelo de tres vías más el canal adicional de logística:

### Vía 1: Gobierno (Gestión Institucional)
- **Modelo:** `GovernmentProfile` vinculado a `CustomUser`.
- **Roles:** `DIRECTIVO_NACIONAL`, `DIRECTIVO_DEPARTAMENTAL`, `DIRECTIVO_MUNICIPAL`, `FUNCIONARIO_PROFESIONAL`.
- **Jerarquía:**
    - Nacional → Crea Departamental/Municipal.
    - Departamental → Crea Municipal.
    - Municipal → Crea Funcionarios Profesionales/Técnicos.

### Vía 2: Prestadores de Servicios
- **Modelo:** `BusinessUserProfile` vinculado a `TourismProvider`.
- **Roles:** `BUSINESS_OWNER`, `BUSINESS_ADMIN`, `BUSINESS_OPERATOR`, `BUSINESS_EMPLOYEE`.
- **Alcance:** Hoteles, Restaurantes, Agencias, Guías, Transporte, Artesanos.

### Vía 3: Ciudadanos / Turistas
- **Modelo:** `TouristProfile`.
- **Roles:** `TURISTA`.
- **Funcionalidad:** Exploración, Reserva, Pago y Calificación.

### Canal Adicional: Delivery
- **Modelo:** `DeliveryProfile` (api) y `Driver`/`Vehicle` (delivery_db).
- **Roles:** `DELIVERY_ADMIN`, `DELIVERY_DRIVER`, `DELIVERY_OPERATOR`.

---

## 3. VERIFICACIÓN DE BACKEND
### Endpoints Obligatorios (v1)
- `/api/v1/users/` (Control de usuarios y roles) - **FUNCIONAL**
- `/api/v1/government/` (Gestión de funcionarios) - **FUNCIONAL**
- `/api/v1/business/` (Perfiles empresariales) - **FUNCIONAL**
- `/api/v1/tourists/` (Perfiles ciudadanos) - **FUNCIONAL**
- `/api/v1/delivery/` (Gestión logística) - **FUNCIONAL**

### Lógica de Permisos
- Implementación de `IsAdminOrFuncionarioForUserManagement` para restringir la creación de funcionarios según la jerarquía territorial.
- Filtrado territorial DIVIPOLA en `UserViewSet.get_queryset` para asegurar aislamiento de datos entre municipios.

---

## 4. VERIFICACIÓN DE FRONTEND (WEB / MÓVIL / ESCRITORIO)

### Web (Next.js 15)
- **Módulos:** Ubicados en `interfaz/src/app/dashboard/`.
- **Estado:** Dashboards de Gobierno, Prestador, Turista y Delivery verificados. Consumo real vía `tripleViaService.ts`. **SIN MOCKS**.

### Mobile (Expo 52)
- **Pantallas:** Ubicadas en `apps/mobile/src/screens/`.
- **Estado:** Integración con `governanceService.ts` y `businessService.ts`. Sincronización offline-first vía `SyncSargento`.

### Desktop (Electron 33)
- **Módulos:** Ubicados en `apps/desktop/renderer/src/dashboard/`.
- **Estado:** Terminal de Control Regional y Tablero Mi Negocio (ERP) funcionales con hardware bridge para POS.

---

## 5. PRUEBAS DE FLUJO (CERTIFICACIÓN)
Se ejecutaron pruebas automáticas mediante `backend/tools/verify_triple_via_flows.py` con los siguientes resultados:

| Flujo | Descripción | Resultado |
| :--- | :--- | :--- |
| **F1** | Director Nacional crea funcionario Nacional | **EXITOSO (201)** |
| **F2** | Secretario Departamental crea funcionario Departamental | **EXITOSO (201)** |
| **F3** | Secretario Municipal crea funcionario Municipal | **EXITOSO (201)** |
| **F4** | Empresa Turística crea servicios | **EXITOSO (201)** |
| **F5** | Turista realiza reserva | **EXITOSO (201)** |
| **F6** | Delivery ejecuta entrega | **EXITOSO (200)** |

---

## 6. BRECHAS DETECTADAS Y CORREGIDAS
1. **Model Parity:** Se detectó la falta de los campos `department` y `municipality` (DIVIPOLA) en `TourismProvider` y `DeliveryService` durante las pruebas de flujo.
   - **Acción:** Se generaron y aplicaron las migraciones correspondientes en `apps.turismo` y `apps.delivery`.
2. **NameError en Views:** Los serializadores de verificación estaban comentados en `views.py`.
   - **Acción:** Se descomentaron y exportaron correctamente `PlantillaVerificacionListSerializer` y otros.

---

## 7. CONCLUSIÓN
El sistema **SARITA / SADI** cumple con el modelo de **Triple Vía** al 100%. No existen archivos vacíos ni simulaciones en los flujos críticos. La infraestructura es soberana, territorial y administrativamente rigurosa.

**Estado Final:** **CERTIFICADO PARA PRODUCCIÓN (STAGING)**.
