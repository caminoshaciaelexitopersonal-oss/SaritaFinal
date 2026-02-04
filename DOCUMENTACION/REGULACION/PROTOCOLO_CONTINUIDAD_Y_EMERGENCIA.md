# PROTOCOLO DE CONTINUIDAD OPERATIVA Y GESTIÓN DE EMERGENCIAS - SARITA

**Fecha:** 24 de Mayo de 2024
**Nivel:** Estratégico / Institucional

## 1. OBJETIVO
Establecer los procedimientos institucionales para garantizar la continuidad del sistema Sarita ante fallos críticos, garantizando la soberanía del SuperAdmin y la integridad de los datos.

## 2. MODOS OPERATIVOS DEL SISTEMA
| Modo | Activación | Impacto | Recuperación |
| :--- | :--- | :--- | :--- |
| **Normal** | Por defecto. | Operatividad total en las 3 vías. | N/A |
| **Auditoría** | Switch manual Admin. | Solo lectura forzado. Trazabilidad máxima. | Desactivación manual. |
| **Degradado** | Automático (Fallo API). | Funcionalidad core activa. Servicios IA inactivos. | Reconexión automática / Sincronización manual. |
| **Emergencia** | Kill-Switch Maestro. | Congelamiento total. Bloqueo de transacciones. | Justificación registrada + Re-activación Soberana. |

## 3. PROCEDIMIENTO DE INTERVENCIÓN (KILL-SWITCH)
1.  **Detección:** El SuperAdmin identifica un patrón anómalo o riesgo inminente.
2.  **Activación:** Uso del botón maestro en el Centro de Autonomía.
3.  **Registro:** Obligación legal de registrar el motivo de la intervención.
4.  **Investigación:** Los Agentes IA son pausados para permitir la auditoría humana.

## 4. RESPONSABILIDAD INSTITUCIONAL
Toda acción tomada en modo de emergencia queda vinculada al ID del SuperAdmin y es irreversible en términos de log de auditoría (SHA-256).
