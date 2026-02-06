# GOBERNANZA ANTI-CAPTURA (ANTI-CAPTURE GOVERNANCE)

**Versión:** 1.0 (Fase Final Z)
**Estado:** OFICIAL
**Objetivo:** Prevenir que el sistema sea capturado por intereses políticos, comerciales o técnicos que desvíen su propósito original.

---

## 1. SEPARACIÓN DE PODERES SISTÉMICOS

SARITA opera bajo una división de responsabilidades diseñada para el control mutuo:

1.  **Capa de Operación (Vía 2):** Los Prestadores controlan su negocio. No pueden modificar la gobernanza global del sistema.
2.  **Capa de Gobernanza (Vía 1):** El SuperAdmin/Estado define las reglas y límites. No puede intervenir en la propiedad privada de los datos operativos de los prestadores sin causa legal.
3.  **Capa Técnica (Mantenimiento):** El equipo de soporte no tiene acceso a los secretos criptográficos de los "Tenants" ni puede saltarse el GovernanceKernel.

## 2. BLINDAJE DEL GOVERNANCE KERNEL

El Núcleo de Gobernanza es el guardián de la soberanía. Sus reglas están protegidas por:

*   **Inmutabilidad de Políticas:** Los cambios en las políticas de autonomía requieren una firma digital de nivel SuperAdmin.
*   **Aislamiento de Lógica:** La lógica de "Quién puede hacer qué" está separada de la lógica de "Cómo se hace". Esto impide que una vulnerabilidad técnica en un módulo (ej. Comercial) afecte la seguridad del sistema completo.
*   **Consistencia Analítica:** Si un cambio en el sistema genera una desviación estadística en los KPIs de cumplimiento, el Kernel bloquea automáticamente las optimizaciones de IA.

## 3. LÍMITES AL PODER INSTITUCIONAL

Para evitar la captura política:

*   **Transparencia Radical:** Cada intervención soberana (Kill Switch o Rollback) genera una alerta pública en el Log Ejecutivo.
*   **Mandato Condicionado:** La IA solo puede ejecutar acciones que estén explícitamente dentro de su mandato tipificado. Ningún humano puede "pedirle" a SARITA que viole su propio marco de gobernanza.
*   **Portabilidad:** Los datos institucionales y operativos deben ser exportables en formatos estándar, evitando el "Vendor Lock-in" que permite la captura comercial.

## 4. PROTECCIÓN CONTRA EL "SUPERUSER" MALICIOSO

Aunque el SuperAdmin es la máxima autoridad, el sistema implementa:
*   **Doble Factor de Autoridad:** Acciones críticas (como el borrado masivo de logs) pueden ser configuradas para requerir dos firmas digitales de alto nivel.
*   **Auditabilidad Externa:** El sistema genera "Audit Bundles" firmados con SHA-256 para que entes de control externos puedan validar que el SuperAdmin no ha abusado de su poder.

---
**"El sistema es soberano solo si ninguna parte puede someter al todo."**
