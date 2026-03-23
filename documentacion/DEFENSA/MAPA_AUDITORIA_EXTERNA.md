# MAPA DE AUDITORÍA EXTERNA (SARITA)
**Guía para Auditores Independientes y Reguladores**

## 1. OBJETIVOS DE LA AUDITORÍA
Facilitar la verificación de la integridad, seguridad y cumplimiento ético del sistema Sarita por parte de entes externos.

## 2. PUNTOS DE VERIFICACIÓN (AUDIT POINTS)

### 2.1 Auditoría Técnica (Seguridad y Código)
- **Ubicación de Evidencia:** `GovernanceAuditLog` (Backend) / Panel de GRC (Frontend).
- **Qué verificar:** Coherencia de los hashes SHA-256 en la cadena de bloques de auditoría.
- **Acceso:** Exportar "Bundle de Auditoría" desde el Centro de Supervisión.

### 2.2 Auditoría Ética y de IA (XAI)
- **Ubicación de Evidencia:** `AutonomousExecutionLog` / Panel de Autonomía.
- **Qué verificar:** Calidad de las explicaciones de la IA. ¿Son legibles? ¿Corresponden a los datos?
- **Escenario:** Revisar decisiones de optimización que afectaron a prestadores.

### 2.3 Auditoría de Soberanía (Control Humano)
- **Ubicación de Evidencia:** Registro de intervenciones de SuperAdmin.
- **Qué verificar:** Uso del Kill Switch y reversiones de acciones autónomas.
- **Métrica:** Tiempo transcurrido entre una alerta sistémica y la respuesta humana.

### 2.4 Auditoría Financiera
- **Ubicación de Evidencia:** `FinancialEventRecord` / Módulo de Gestión Contable.
- **Qué verificar:** Trazabilidad E2E desde la sesión de voz (Vía 3) hasta el registro contable (Vía 2).

## 3. HERRAMIENTAS DE EXTRACCIÓN
- **Exportador Institucional:** Genera reportes PDF/JSON firmados digitalmente.
- **Modo Auditor:** Interfaz de solo lectura con visualización de metadatos ocultos.

---
*Sarita está diseñada para ser una "Caja de Cristal", permitiendo la inspección total de sus procesos sin comprometer la seguridad operativa.*
