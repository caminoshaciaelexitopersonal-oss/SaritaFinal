# ESPECIFICACIÓN DEL KERNEL DE GOBERNANZA SUPRANACIONAL (SUPRANATIONAL KERNEL SPEC - SGK)

**Versión:** 1.0 (Fase Z-SUPRA)
**Módulo:** `apps.supranational_kernel`
**Rol:** Árbitro Técnico Neutral para Acuerdos Interestatales.

---

## 1. NATURALEZA DEL SGK
El Kernel de Gobernanza Supranacional (SGK) es el componente central de confianza para los despliegues de SARITA destinados a organismos multilaterales y bloques regionales. A diferencia del Kernel Nacional, el SGK no ejerce autoridad soberana, sino **autoridad de certificación y verificación de acuerdos**.

## 2. CAPACIDADES FUNCIONALES (LO QUE PUEDE HACER)

### 2.1 Verificación de Cumplimiento Técnico
*   **Función:** Compara los eventos reportados por los Nodos Nacionales contra los indicadores de cumplimiento definidos en el Tratado Constitutivo.
*   **Acción:** Emite certificados digitales de cumplimiento o reportes técnicos de desviación.

### 2.2 Detección de Incumplimientos Objetivos
*   **Función:** Identifica automáticamente cuando un dato técnico (ej: niveles de emisión, flujos migratorios autorizados, cuotas comerciales) sale de los rangos acordados.
*   **Acción:** Genera Alertas Institucionales de Riesgo dirigidas a todas las partes firmantes.

### 2.3 Registro de Consenso y Votación
*   **Función:** Proporciona un mecanismo inmutable para registrar votos ponderados, consensos técnicos y objeciones formales de los Estados.
*   **Acción:** Actualiza el estado del tratado en base a las decisiones soberanas registradas.

### 2.4 Generación de Evidencia Auditable
*   **Función:** Consolida logs de trazabilidad sobre la ejecución del tratado.
*   **Acción:** Produce "Supranational Audit Bundles" firmados criptográficamente para revisión externa.

## 3. LIMITACIONES ESTRUCTURALES (LO QUE NO PUEDE HACER)

*   **❌ No hay Mandato Ejecutivo:** El SGK nunca puede ordenar a un Estado realizar una acción física o política.
*   **❌ No hay Acceso Soberano:** El SGK tiene prohibido el acceso a bases de datos crudas de los Nodos Nacionales. Solo procesa eventos certificados.
*   **❌ No hay Modificación Remota:** No posee permisos para alterar la configuración interna de un Nodo Soberano.
*   **❌ No hay Decisión Autónoma:** El Kernel no "decide" quién tiene la razón en una disputa; solo reporta los hechos técnicos registrados.

## 4. INTEGRIDAD Y NEUTRALIDAD
El SGK reside en una infraestructura separada de cualquier nación firmante. Su código es abierto a auditoría por parte de todos los miembros y sus registros son inmutables mediante encadenamiento de hashes, garantizando que ninguna parte pueda manipular la bitácora de cumplimiento.

---
**"El SGK no gobierna países; gobierna la verdad técnica de lo que los países acordaron entre sí."**
