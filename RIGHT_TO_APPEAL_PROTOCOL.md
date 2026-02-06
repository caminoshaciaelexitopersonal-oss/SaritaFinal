# PROTOCOLO DE APELACIÓN Y REVISIÓN (RIGHT-TO-APPEAL PROTOCOL)

**Versión:** 1.0 (Fase Z-CIVIL)
**Módulo:** `apps.right_to_appeal_engine`
**Rol:** Mecanismo de Reversión y Apelación Técnica Inmediata.

---

## 1. EL DERECHO A LA APELACIÓN DIGITAL
Todo usuario afectado por una decisión automatizada de SARITA tiene el derecho inalienable a apelar la decisión sin fricciones técnicas o burocráticas. El **Right-to-Appeal Engine (RAE)** gestiona este flujo de forma automatizada hacia la resolución humana.

## 2. PROCEDIMIENTO DE APELACIÓN TÉCNICA

### Paso 1: Notificación de Decisión
Cuando el sistema ejecuta una acción de nivel H1 o superior, el usuario recibe un aviso con el enlace: **"¿Desea objetar esta decisión?"**.

### Paso 2: Activación de la Objeción (Freeze)
Al hacer clic en el botón de objeción, el RAE activa las siguientes acciones:
1.  **Congelamiento Temporal:** Se suspende cualquier efecto futuro de la decisión sobre el perfil del usuario.
2.  **Snapshot Forense:** El sistema captura el estado exacto (inputs, modelo, versión de regla) que generó la decisión apelada.
3.  **Registro en Evidence Vault:** La apelación queda sellada criptográficamente como una "Acción Civil Pendiente".

### Paso 3: Solicitud de Justificación (XAI Civil)
El sistema presenta al usuario la explicación comprensible de la decisión (ver `XAI_CIVIL_STANDARD.md`). El usuario puede marcar puntos específicos de la explicación con los que no está de acuerdo (ej: "Mis ingresos reportados son incorrectos").

### Paso 4: Escalamiento a Revisión Humana (Manual Override)
La apelación se envía a la cola de trabajo de un Funcionario Auditor con mandato legal.
*   **Tiempo Límite:** El sistema impone un SLA (Service Level Agreement) para la revisión humana; si el tiempo expira, el RAE puede revertir la acción preventivamente según la política del Nodo.

## 3. CAPACIDADES DEL FUNCIONARIO REVISOR
El humano autorizado podrá:
1.  **Confirmar:** La decisión de la IA era correcta. El congelamiento se levanta.
2.  **Revertir:** La decisión de la IA era errónea o injusta. El sistema realiza un rollback total.
3.  **Ajustar:** Modificar la decisión manualmente y registrar la corrección para el entrenamiento futuro del kernel de sesgo.

## 4. TRANSPARENCIA DEL PROCESO
El usuario puede seguir en tiempo real el estado de su apelación:
- `ESTADO: OBJETADO - EN REVISIÓN HUMANA`
- `ESTADO: REVERTIDO - ACCIÓN CANCELADA`
- `ESTADO: CONFIRMADO - DECISIÓN RATIFICADA`

---
**"La apelación no es un favor del sistema; es una instrucción de red del ciudadano."**
