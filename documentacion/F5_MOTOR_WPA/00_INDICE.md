# Índice de Documentación - Fase 5: Motor de Procesamiento Autónomo (WPA)

Este directorio contiene los entregables técnicos y operativos del motor de ejecución del Sistema SARITA.

## Entregables Principales
1. [**Arquitectura WPA**](01_ARQUITECTURA_WPA.md): Diseño de componentes y flujo de ejecución asíncrona.
2. [**Estados y Compensación**](02_ESTADOS_Y_COMPENSACION.md): Máquina de estados y patrón SAGA para reversiones.
3. [**Especificación de Workflows**](03_ESPECIFICACION_WORKFLOWS.md): Estándar de definiciones JSON para orquestación.
4. [**Dashboard Operativo**](04_DASHBOARD_OPERATIVO.md): Monitoreo en tiempo real y controles de emergencia.
5. [**Informe de Pruebas**](05_INFORME_PRUEBAS_WPA.md): Validación de flujos secuenciales y fallos con rollback.

## Código Fuente WPA
- `backend/apps/admin_plataforma/wpa_core.py`: Implementación del motor SAGA y Executor Layer.
- `backend/apps/admin_plataforma/models.py`: Modelos de persistencia de workflows.

---
**Estado de la Fase:** COMPLETADA.
