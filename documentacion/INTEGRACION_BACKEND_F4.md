# DOCUMENTACIÓN DE INTEGRACIÓN BACKEND — FASE F4

Esta fase consolida la conexión técnica entre la interfaz Enterprise de Sarita y el Núcleo de Negocio (Backend).

---

## 🏗️ Arquitectura de Servicios (`/services`)

### 1. Cliente HTTP (`httpClient.ts`)
- **Base:** Axios.
- **Configuración:** Tiempo de espera de 15s y cabeceras JSON obligatorias.

### 2. Interceptores (`interceptors.ts`)
- **Request:**
    - Inyecta el token de sesión (Bearer/Token).
    - Añade cabeceras de contexto: `X-Company-ID` y `X-Accounting-Period`.
- **Response:**
    - Manejo de sesión expirada (401).
    - **Normalización de Errores:** Convierte fallos de red en objetos estructurados `{ code, message, technical, action }`.

---

## 🗺️ Mapa de Endpoints y Dominios

| Dominio | Módulo de Endpoints | Cobertura Principal |
| :--- | :--- | :--- |
| **Comercial** | `comercial.ts` | Funnels, Leads, Facturación de Venta. |
| **Contable** | `contable.ts` | Plan de Cuentas, Asientos, Reportes DIAN. |
| **Operativo** | `operativo.ts` | Perfil, Reservas, Inventario Servicios. |
| **Financiero** | `financiero.ts` | Tesorería, Cuentas Bancarias, Caja. |
| **Seguridad** | `seguridad.ts` | Login, Registro por Rol, Gestión de Sesión. |
| **Admin** | `admin.ts` | Inteligencia Decisora, Auditoría Global. |

---

## 🧬 Capa de Transformación (Mappers)
Se implementó un patrón de **Mappers** para desacoplar la UI de los nombres de campos del backend:
- `API Response` → `Mapper` → `ViewModel (UI Props)`.
- **Beneficio:** Si el backend cambia un campo (ej: `full_name` por `nombre_completo`), solo se actualiza el mapper, no las vistas.

---

## 🔐 Gobernanza de Datos
1. **SSOT:** El frontend no realiza cálculos financieros; consume el resultado del motor contable del backend.
2. **Contexto:** Las operaciones están protegidas por el contexto de Empresa y Período, garantizando multi-tenancy real.
3. **Auditoría:** Todas las peticiones POST/PATCH quedan registradas en el AuditLog del sistema mediante el usuario autenticado.

---

## 🚀 Pruebas de Integración
Se habilitó una ruta de simulación en `/dashboard/test-page` que verifica el flujo E2E:
- [x] Conexión HTTP.
- [x] Persistencia de Sesión.
- [x] Flujo Comercial -> Contable.
- [x] Generación de Balances.
