# MATRIZ DE CONTROL DE AUTONOMÍA (FASE 7)

Esta matriz define qué agentes y módulos pueden actuar, bajo qué nivel y con qué restricciones específicas.

| Dominio | Agente Responsable | Nivel Máximo | Límite Financiero | Límite Frecuencia | Reversibilidad |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Comercial** | Capitan Marketing | L2 (Autónomo) | $500.00 / acción | 5 / día | 100% (Snapshot) |
| **Contable** | Capitan Finanzas | L1 (Propositivo) | N/A | N/A | Manual |
| **Operativo** | Teniente Operación | L2 (Autónomo) | N/A | 20 / día | Alta |
| **Gobernanza** | General Sarita | L1 (Propositivo) | N/A | N/A | N/A |
| **Financiero** | Coronel Finanzas | L0 (Informativo) | N/A | N/A | N/A |
| **SADI (Voz)** | SADI Orchestrator | L2 (Autónomo) | N/A | Ilimitado (Comandos) | Total |

## PROTOCOLO DE ESCALAMIENTO
- Para elevar un dominio de L1 a L2 se requiere: **Certificación Técnica + Firma SuperAdmin.**
- El nivel L3 está **reservado permanentemente** para:
    - Modificación de bases de datos críticas.
    - Transferencias bancarias externas.
    - Modificación de usuarios Admin.
    - Alteración de logs de auditoría.

## REGLA DE SUPREMACÍA
En caso de conflicto entre una decisión de la IA y una orden manual del SuperAdmin, la orden manual tiene **prioridad absoluta** y anula cualquier proceso autónomo en curso.
