# Modelo de Datos y Diccionario - Sistema SARITA

## 1. Estándares de Naming
- **Tablas:** Plural, snake_case (e.g., `facturas_venta`, `perfiles_proveedor`).
- **Campos:** Singular, snake_case (e.g., `fecha_creacion`, `monto_total`).
- **Foreign Keys:** `nombre_tabla_id` (e.g., `usuario_id`).
- **Booleano:** Prefijo `is_` o `has_` (e.g., `is_active`, `has_verified`).

## 2. Diccionario de Datos Core (Entidades Principales)
- **User:** Corazón de la identidad.
- **ProviderProfile:** Nodo comercial del prestador.
- **Transaction:** Registro financiero atómico.
- **AgentMission:** Registro de actividad de IA.
- **AuditLog:** Registro inmutable de cambios.

## 3. Identificadores Únicos
- Uso mandatorio de **UUID v4** para todas las llaves primarias expuestas o utilizadas en integraciones.
- Los IDs secuenciales (Integer) se reservan para uso interno de la base de datos si es necesario por rendimiento, pero no se exponen en la API.

## 4. Versionado de Esquemas
- Las migraciones deben ser incrementales.
- No se permiten cambios destructivos en esquemas en producción sin un plan de transición.
- Uso de herramientas de migración (Django Migrations) con revisión obligatoria por el Agente Auditor.

## 5. Política de Retención
- **Datos Transaccionales:** Permanentes mientras la cuenta esté activa.
- **Logs de Auditoría:** 7 años mínimo.
- **Datos de Sesión:** 30 días.

## 6. Modelo de Auditoría (Shadow Tables / Audit Log)
Para entidades críticas y el núcleo de gobernanza, se mantiene un registro de auditoría que incluye:
- `timestamp` del evento.
- `usuario_id` que realizó la acción.
- `intencion` (Nombre del comando o acción).
- `parametros` (Input en formato JSON).
- `resultado` (Output en formato JSON).
- `integrity_hash` / `previous_hash` (Encadenamiento SHA-256).
