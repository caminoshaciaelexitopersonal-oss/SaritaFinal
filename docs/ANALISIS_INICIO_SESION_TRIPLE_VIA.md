# Análisis de Lógica e Inicio de Sesión - Modelo Triple Vía

Este documento detalla el flujo técnico y operativo para el acceso al sistema SARITA, desglosado por sus tres vías principales de interacción.

## 1. Arquitectura de Identidad y Roles

La autenticación centralizada reside en el modelo `CustomUser` (`backend/api/models.py`), el cual implementa una estructura de roles que segmenta el ecosistema:

### Vía 1: Gobierno (Gobernanza Institucional)
*   **Roles:** `ADMIN`, `DIRECTIVO` (Nacional, Departamental, Municipal), `FUNCIONARIO` (Profesional, Técnico, Asistencial).
*   **Perfil:** `GovernmentProfile`, vinculado a una `Entity` (Alcaldía, Gobernación).
*   **Seguridad Territorial:** El acceso a los datos está blindado por códigos **DIVIPOLA**. Un funcionario municipal solo tiene alcance sobre los registros de su municipio, garantizando la soberanía de datos local.

### Vía 2: Negocios (Prestadores y Artesanos)
*   **Roles:** `BUSINESS_OWNER`, `PRESTADOR`, `ARTESANO`, `EVENT_MANAGER`.
*   **Perfil:** `BusinessUserProfile` vinculado a un `TourismProvider`.
*   **Validación:** Es mandatorio el uso del **R.N.T. (Registro Nacional de Turismo)** para prestadores, lo que permite la interoperabilidad con bases de datos estatales.

### Vía 3: Turistas (Ciudadanos y Social)
*   **Rol:** `TURISTA`.
*   **Perfil:** `TouristProfile`.
*   **Protección:** El acceso a funciones sociales (Citas/Rooms) requiere validación de mayoría de edad (18+) basada en el campo `birthdate`.

---

## 2. Mecanismos de Inicio de Sesión (Backend)

El backend ofrece dos motores de autenticación robustos:

### A. Autenticación Estándar (JWT + MFA)
Utilizada para el flujo general de todas las aplicaciones.
*   **Endpoint:** `/api/v1/auth/login/`
*   **Proceso:**
    1.  Validación de credenciales (`email`/`password`).
    2.  Si se requiere **MFA**, el sistema solicita un código de verificación.
    3.  Emisión de tokens **JWT** (Access y Refresh).
*   **Seguridad:** Implementa `enterprise_exception_handler` para respuestas de error estandarizadas.

### B. Login vía R.N.T. (Exclusivo Vía 2)
Un motor de soberanía digital que permite el acceso mediante el registro oficial.
*   **Endpoint:** `/api/v1/tourism-providers/login-rnt/`
*   **Servicio:** `RNTIntegrationService`.
*   **Lógica:** Consulta en tiempo real la validez del número R.N.T. en la API de MINCIT/CONFECAMARAS. Si el prestador está activo, se genera una sesión automática en SARITA.

---

## 3. Implementación Multi-Plataforma (Frontend)

El sistema garantiza la paridad funcional mediante el uso de la **Shared-SDK** (`sarita-platform/shared-sdk`).

### Web (Next.js 15)
*   **Gestor:** `AuthContext.tsx`.
*   **Flujo:** Tras el login, redirige según el rol:
    *   **Turistas:** `/mi-viaje` (Favoritos y planes).
    *   **Otros:** `/dashboard` (Panel administrativo/operativo).
*   **Persistencia:** `localStorage` con interceptores de Axios para la renovación de tokens.

### Mobile (Expo 52)
*   **Gestor:** `AuthContext.tsx` móvil.
*   **Seguridad:** Utiliza `expo-secure-store` para persistencia cifrada de tokens.
*   **SADI Mobile:** Al iniciar sesión, se configura automáticamente el **Sargento de IA Local** basado en la potencia del hardware del dispositivo.

### Desktop (Electron 33)
*   **Gestor:** `AuthContext.tsx` desktop.
*   **Integración:** Conectado directamente al **Hardware Bridge** para el módulo POS, permitiendo que tras el login se habiliten periféricos como impresoras térmicas y escáneres de identidad.

---

## 4. Onboarding y Registro Georeferenciado

El registro utiliza el `LocationAwareRegisterSerializer`, que obliga a la captura de:
1.  **Ubicación DIVIPOLA:** Departamento y Municipio.
2.  **Sincronización RNT:** Para prestadores, el registro dispara un proceso de validación en segundo plano que certifica el negocio en menos de 30 días.

---
**Certificación:** El sistema ha sido auditado (Marzo 2026) y se encuentra al **100% de paridad funcional** sin el uso de mocks en los flujos críticos de acceso.
