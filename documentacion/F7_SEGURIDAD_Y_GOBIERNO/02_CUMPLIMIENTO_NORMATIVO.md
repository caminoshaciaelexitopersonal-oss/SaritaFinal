# Marco de Cumplimiento Normativo Internacional - Sistema SARITA

SARITA está diseñado para operar bajo los estándares más exigentes de privacidad y seguridad de la información, permitiendo su despliegue en mercados internacionales.

## 1. Alineación con GDPR (Unión Europea)

El sistema implementa las siguientes capacidades nativas:
- **Derecho al Olvido (Right to Erasure):** Proceso automatizado para la eliminación de datos personales tras validación del MCP.
- **Portabilidad de Datos:** Exportación de perfiles en formato JSON estándar.
- **Registro de Consentimiento:** Auditoría inmutable de cuándo y para qué un usuario dio su permiso.
- **Minimización de Datos:** El sistema solo solicita y almacena los campos estrictamente necesarios para la operación turística.
- **DPIA (Data Protection Impact Assessment):** El Agente Auditor realiza evaluaciones automáticas del impacto en la privacidad ante nuevos flujos de datos.

## 2. Alineación con ISO/IEC 27001

El sistema soporta los controles del Anexo A:
- **A.12.4.1 Registro de eventos:** Implementado vía Shadow Ledger SHA-256.
- **A.9 Control de acceso:** Implementado vía RBAC/ABAC avanzado.
- **A.10 Criptografía:** Políticas de cifrado en reposo y tránsito mandatorias.

## 3. SOC 2 Type II Readiness

SARITA mantiene la trazabilidad necesaria para auditorías de confianza (Trust Services Criteria):
- **Seguridad:** Protección contra accesos no autorizados.
- **Disponibilidad:** Monitoreo de SLA y plan de recuperación DRP.
- **Integridad del Procesamiento:** Verificación de transacciones vía PCA.
- **Confidencialidad:** Clasificación y cifrado de datos.
- **Privacidad:** Gestión del ciclo de vida del dato personal.

## 4. Retención de Información
Se establecen políticas de purga automática:
- **Logs de Auditoría de Seguridad:** 7 años.
- **Datos Transaccionales:** Permanentes (con opción de anonimización).
- **Contexto Efímero de Agentes:** 30 días.
- **Documentación Legal/Contratos:** 10 años.

## 5. Auditoría Externa
El sistema expone un **Portal de Auditoría** (Audit Vault) con acceso de solo lectura y firma digital para auditores externos certificados, permitiendo la verificación de la integridad de los registros sin comprometer la operación.
