# Índice de Documentación - Fase 3: Implementación del Núcleo MCP

Este directorio contiene los entregables técnicos y estratégicos de la Fase 3, el corazón del control del Sistema SARITA.

## Entregables Principales
1. [**Arquitectura Detallada**](01_ARQUITECTURA_DETALLADA_MCP.md): Los 6 pilares del control central.
2. [**Diagrama de Módulos**](02_DIAGRAMA_MODULOS_MCP.md): Flujos de orquestación y protocolos de compensación.
3. [**Especificación API**](03_ESPECIFICACION_API_MCP.md): Contrato interno para la coordinación de comandos.
4. [**Modelo de Estados**](04_MODELO_ESTADOS_MCP.md): Ciclo de vida persistente del comando.
5. [**Gestión de Riesgo y Failsafe**](05_GESTION_RIESGO_FAILSAFE.md): Evaluación en tiempo real y seguridad ante fallos.
6. [**Informe de Pruebas**](06_INFORME_PRUEBAS_ESTRES.md): Validación de escenarios de éxito, riesgo y auditoría.

## Código Fuente Nucleo MCP
- `backend/apps/admin_plataforma/mcp_core.py`: Implementación del motor de orquestación y auditoría.

---
**Estado de la Fase:** COMPLETADA.
