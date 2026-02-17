# PROTOCOLOS DE OPERACIÓN ESTÁNDAR (SOP) — SARITA CORE

**Versión:** 1.0
**Estado:** VIGENTE
**Audiencia:** Operadores del Sistema / Administradores de Infraestructura

---

## SOP-01: ALTA DE NUEVO TENANT (Inquilino Institucional)

### Propósito
Registrar una nueva entidad institucional (Alcaldía, Gobernación, Corporación) en el ecosistema SARITA garantizando aislamiento criptográfico.

### Procedimiento
1. **Creación de Entidad:** Acceder al Panel SuperAdmin y crear un registro en `api.models.Entity`.
2. **Creación de Compañía (Tenant):** Crear un registro en `apps.companies.models.Company` asociando el código único de la entidad.
3. **Verificación de Llaves:** Validar que la señal `create_company_encryption_key` haya generado la sal criptográfica en `CompanyEncryptionKey`.
4. **Asignación de Administrador:** Crear un usuario con rol `ADMIN_ENTIDAD` y vincularlo al perfil de la nueva entidad.
5. **Aprovisionamiento de Módulos:** Activar las banderas de servicios (Gobernanza, Turismo) según el contrato institucional.

---

## SOP-02: ALTA DE NUEVO PRESTADOR DE SERVICIOS (Vía 2)

### Propósito
Integrar a un empresario turístico al ERP de Vía 2 bajo la supervisión de un nodo institucional.

### Procedimiento
1. **Auto-Registro:** El prestador inicia el flujo en `/registro/prestador`.
2. **Carga de Evidencias:** El sistema requiere adjuntar RNT y Cámara de Comercio (Almacenado en `DocumentoVerificacion`).
3. **Validación Institucional:** Un Funcionario con rol `Auditor` revisa el expediente en el panel GRC.
4. **Activación de Perfil:** Tras la aprobación, se genera el `ProviderProfile` y se habilita el acceso a los 5 módulos ERP.
5. **Inducción SADI:** El sistema lanza una misión de bienvenida vía agente SADI para configurar el Plan de Cuentas inicial.

---

## SOP-03: RESPUESTA A INCIDENTES DE SEGURIDAD

### Propósito
Contener y neutralizar amenazas detectadas por el sistema de defensa activa.

### Procedimiento
1. **Detección:** Alerta roja en `SecurityShield` o HTTP 429 masivos en `ForensicSecurityLog`.
2. **Contención Automática:** El sistema invalida el token de la sesión atacante.
3. **Intervención Humana:**
   - Si el ataque persiste: El SuperAdmin debe activar el **"Modo Ataque"** (Kill Switch) desde el dashboard.
   - Esto congela todas las escrituras (`SYSTEM_ATTACK_MODE = True`).
4. **Análisis Forense:** Revisar la cadena de integridad en `ForensicSecurityLog` para identificar el vector y la IP de origen.
5. **Restauración:** Una vez mitigado el vector, desactivar el Modo Ataque y reanudar operaciones.

---

## SOP-04: GESTIÓN DE FALLAS Y MODO DEGRADADO

### Propósito
Mantener la disponibilidad del sistema ante fallos parciales de servicios externos (LLM, Pasarelas de Pago).

### Procedimiento
1. **Fallo de LLM (SADI/SARITA):** El frontend detecta timeout > 15s.
   - **Acción:** Cambiar automáticamente a "Modo Manual" (Formularios tradicionales).
   - El sistema muestra el Badge de "Servicio Degradado - Ámbar".
2. **Fallo de Backend:**
   - **Acción:** El Middleware activa el caché estático de Vía 3 (Turista) para permitir la navegación de destinos aunque la reserva esté deshabilitada.

---

## SOP-05: PROTOCOLO DE ESCALAMIENTO DE CARGA

### Propósito
Prevenir la degradación por saturación de recursos.

### Procedimiento
1. **Monitor de Umbrales:** Si el uso de CPU supera el 80% o las peticiones concurrentes > 500 por nodo.
2. **Acción de Escalamiento:**
   - Incrementar Workers de Celery para misiones de agentes.
   - Habilitar Rate Limiting agresivo para usuarios de rol `TURISTA` (Reducción a 10 req/min).
3. **Optimización de Base de Datos:** Ejecutar `ANALYZE` en tablas críticas de facturación y auditoría.

---
**"La disciplina operativa es la única garantía de soberanía tecnológica."**
