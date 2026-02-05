# PROTOCOLO DE CUSTODIA EN EL EVIDENCE VAULT (EV)

**Versión:** 1.0 (Fase Z-LEGAL)
**Estado:** ESTRUCTURAL / CRÍTICO
**Propósito:** Garantizar la inmutabilidad y admisibilidad legal de las pruebas técnicas generadas por SARITA.

---

## 1. NATURALEZA DEL EVIDENCE VAULT (EV)
El Evidence Vault no es una base de datos operativa; es un **repositorio blindado de registros forenses**. Su diseño está optimizado para la integridad, no para la velocidad de consulta. Se utiliza para almacenar el rastro de cumplimiento de normas y las evidencias de ataques o fallos sistémicos.

## 2. PILARES DE INTEGRIDAD

### 2.1 Encadenamiento SHA-256 (Chained Integrity)
Cada registro en el EV contiene el hash del registro anterior. Una ruptura en esta cadena invalida automáticamente todo el set de pruebas, activando una alerta de "Corrupción Forense".

### 2.2 Sellado Temporal (Timestamping)
Todas las evidencias reciben una marca de tiempo inmutable sincronizada con fuentes de tiempo nacionales/internacionales. El EV prohíbe la modificación manual de la fecha de registro.

### 2.3 Notarización Digital (Blockchain Anchor)
Para niveles de riesgo L4 (Infraestructura Crítica), SARITA genera un hash consolidado diario y lo ancla en una red blockchain pública o institucional, proporcionando una prueba de existencia de la evidencia ante terceros externos.

## 3. PROTOCOLO DE ACCESO Y CADENA DE CUSTODIA
El acceso al EV es restringido por diseño:

1.  **Ingreso de Prueba:** Solo el Compliance Engine (CE) y el Governance Kernel (GK) pueden escribir en el EV mediante intenciones firmadas.
2.  **Consulta Auditora:** Solo usuarios con rol `Auditor` o `SuperAdmin` pueden visualizar las pruebas. Cada consulta queda registrada con identificación del usuario, hora y razón del acceso.
3.  **Extracción Legal (Audit Bundles):** La exportación de pruebas requiere una "Llave de Extracción" que combina firmas del nodo y, opcionalmente, de un organismo externo acreditado.

## 4. POLÍTICA DE PRESERVACIÓN Y PURGA
- **Vigencia Legal:** Los registros de impacto L3 y L4 se preservan por un mínimo de 10 años (alineado con términos de prescripción legal internacional).
- **Purga Automática:** Los eventos L0 y L1 pueden ser purgados tras 2 años para optimizar el almacenamiento, siempre que no estén vinculados a una investigación abierta.
- **Inviolabilidad de Purga:** Ningún humano puede borrar un registro individual antes de su fecha de caducidad técnica.

## 5. REQUISITOS DE ADMISIBILIDAD
Para que una prueba del EV sea presentada ante un tribunal, el sistema debe emitir un **Certificado de Integridad de Evidencia** que incluya:
- Hash de integridad de la prueba.
- Hash de la norma legal aplicada (versionado LK).
- Prueba de no alteración de la cadena de hashes (Validación de Chained Hash).

---
**"En el Evidence Vault, la verdad técnica se congela para que la justicia pueda verla años después."**
