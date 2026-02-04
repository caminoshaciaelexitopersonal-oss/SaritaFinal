# AGENT CONTROL MATRIX - SARITA

**Fecha:** 24 de Mayo de 2024
**Estado:** Jerarquía Controlada

## 1. CADENA DE MANDO (JERARQUÍA SARITA)
| Agente | Rango | Dominio | Control Visible |
| :--- | :--- | :--- | :--- |
| **General** | Lider Orquestador | Global | Kill-Switch / Pause |
| **Coronel Marketing** | Estratégico | Comercial | Kill-Switch / Pause |
| **Coronel Finanzas** | Estratégico | Financiero | Kill-Switch / Pause |
| **Coronel Prestadores** | Estratégico | Operativo | Kill-Switch / Pause |

## 2. MECANISMOS DE INTERVENCIÓN
- **Pausa Inmediata:** Detiene el procesamiento de misiones en cola para un agente específico.
- **Kill-Switch:** Desactiva totalmente la autonomía del agente, forzando la intervención humana para cualquier acción posterior.
- **Reanudación:** Requiere registro de motivo en el Log de Soberanía.

## 3. GOBERNANZA JERÁRQUICA
Se ha verificado visualmente que los agentes obedecen los límites de dominio. Un agente de marketing no tiene acceso a controles financieros, y su estado de autonomía está condicionado por los umbrales definidos en el Kernel de Gobernanza.
