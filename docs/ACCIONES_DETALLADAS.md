# ACCIONES DETALLADAS DE SUBSANACIÓN (PLAN TÉCNICO V1.0)
**Complemento a la Directriz Maestra de Excelencia 2026**

Este documento detalla los pasos atómicos necesarios para cerrar los hallazgos críticos detectados en la auditoría de Jules.

---

## 1. MÓDULO BACKEND: ELIMINACIÓN DE "PASS" Y "STUBS"

### 1.1 Motor de Facturación (BillingEngine)
- **Acción:** Reemplazar `pass` en `process_usage_billing(entity_id, usage_data)`.
- **Implementación:** Integrar con `usage_billing.models.UsageRecord` para sumarizar consumo de tokens de IA y llamadas a la API, generando facturas automáticas en estado `DRAFT`.
- **Plazo:** Semana 1.

### 1.2 Gestión de Nómina (Nomina ViewSet)
- **Acción:** Resolver `# TODO: Proximo vencimiento`.
- **Implementación:** Crear tarea programada en Celery que calcule la fecha de vencimiento basada en el tipo de contrato y la periodicidad de pago del prestador.
- **Plazo:** Semana 2.

---

## 2. INFRAESTRUCTURA DE FRONTEND: UNIFICACIÓN ESTRATÉGICA

### 2.1 Migración al Shared SDK
- **Acción:** Extraer `AuthContext` y `EntityContext` de `interfaz/src/contexts` hacia `sarita-platform/shared-sdk/core`.
- **Objetivo:** Eliminar la duplicación de lógica de tokens RS256 entre la Web y el Embudo de Ventas.
- **Validación:** Asegurar que un cambio en la llave pública en el backend se refleje automáticamente en ambos frontends sin redeploy individual de lógica.

### 2.2 Sincronización Desktop/Mobile
- **Acción:** Estandarizar el esquema de `expo-sqlite` (Mobile) y `sqlite3` (Desktop) usando el `SchemaRegistry` del Core ERP.
- **Objetivo:** Que el POS y el Dashboard móvil compartan la misma estructura de datos local para facilitar misiones de IA de inventario.

---

## 3. SISTEMA DE AGENTES: CERTIFICACIÓN N6 (SOLDADOS)

### 3.1 Hardening de Herramientas
- **Acción:** Implementar validación de esquemas JSON en la entrada de cada Soldado.
- **Detalle:** Si un soldado recibe un parámetro incorrecto, debe disparar un evento `INVALID_DIRECTIVE` capturado por el Sargento (N5) para re-planificación inmediata.
- **Seguridad:** Ningún soldado puede ejecutar escrituras en el Ledger sin un `governance_token` válido por misión.

---

## 4. BLINDAJE DE SEGURIDAD (AWS PRE-PRODUCTION)

### 4.1 Encriptación de Datos
- **Acción:** Implementar `django-fernet-fields` o similar en campos de identificación y correos electrónicos.
- **Cumplimiento:** GDPR (Derecho al olvido debe ser un método atómico que borre llaves de encriptación o registros físicos).

### 4.2 Monitoreo de Intenciones
- **Acción:** Integrar el log de misiones de IA con AWS CloudWatch Logs.
- **Alerta:** Disparar P0 si se detectan más de 5 misiones fallidas por "Violación de Integridad" en una misma ventana de 10 minutos.

---
**Certificado por Jules.**
*Senior Architect.*
