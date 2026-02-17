# MODELO DE AMENAZAS Y ANÁLISIS DE SEGURIDAD (SARITA)

**Fecha:** 24 de Mayo de 2024
**Versión:** 1.0 (Preparación para Certificación)

## 1. INTRODUCCIÓN
Este documento identifica las amenazas potenciales al sistema SARITA, evalúa su impacto y detalla las contramedidas implementadas para garantizar la integridad de la infraestructura digital soberana.

## 2. SUPERFICIE DE ATAQUE
- **API Endpoints:** Entrada principal para usuarios de la Triple Vía.
- **Orquestador de Voz (SADI):** Vector de entrada de lenguaje natural.
- **Interfaz Administrativa:** Control de gobernanza y políticas.
- **Base de Datos:** Persistencia de registros financieros y de auditoría.
- **Agentes IA:** Ejecución autónoma de tareas.

## 3. MATRIZ DE AMENAZAS (STRIDE)

| Amenaza | Descripción | Impacto | Mitigación SARITA |
| :--- | :--- | :--- | :--- |
| **Spoofing** | Suplantación de autoridad SuperAdmin. | Crítico | Autenticación JWT + RBAC estricto + Validación en Kernel. |
| **Tampering** | Modificación de logs de auditoría o políticas. | Crítico | **Audit Trail Inmutable**: Uso de Hashes para verificar integridad de logs. |
| **Repudiation** | Un usuario niega haber realizado una acción crítica. | Alto | Logs detallados con `user_id`, `timestamp` y `payload` firmado. |
| **Information Disclosure** | Fuga de datos de prestadores entre jurisdicciones. | Alto | **Tenant Isolation**: Middleware de separación de datos por Company/Entity. |
| **DoS** | Saturación de servicios de IA para bloquear el sistema. | Medio | Throttling en API y límites duros de ejecución autónoma. |
| **Elevation of Privilege** | Un Prestador intenta acceder a funciones de SuperAdmin. | Crítico | `PermissionGuard` en Frontend y validación redundante en Viewsets. |

## 4. RIESGOS ESPECÍFICOS DE IA
### A. Expansión No Autorizada de Autonomía
- **Riesgo:** La IA intenta modificar sus propios límites.
- **Contramedida:** Los modelos de `AutonomousAction` solo son modificables por el rol `ADMIN` (SuperAdmin) mediante intervención soberana manual.

### B. Alucinación en Comandos Críticos
- **Riesgo:** SADI interpreta erróneamente un comando de bloqueo.
- **Contramedida:** **Human-in-the-loop**: Acciones de alto impacto (Nivel 1 o superior) requieren confirmación verbal o visual explícita.

## 5. INFRAESTRUCTURA DE DEFENSA
1. **Governance Kernel:** Actúa como un firewall de intenciones de negocio.
2. **Autonomy Kill Switch:** Interruptor de emergencia accesible 24/7.
3. **XAI (Explainable AI):** Auditoría reconstructiva que obliga a la IA a justificar cada paso.

---
**Firmado:** Jules (AI Software Engineer)
**Estatus:** CERTIFICABLE
