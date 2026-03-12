# CIERRE FUNCIONAL DEL FRONTEND — SISTEMA SARITA

Este documento certifica la finalización de la Fase F-CF, donde el frontend ha sido alineado con la verdad operativa del backend, eliminando simulaciones y exponiendo los bloqueos reales de la arquitectura.

## 1. Módulos Cerrados Funcionalmente

Los siguientes módulos consumen endpoints reales y reflejan el estado verídico de la persistencia:

- **Vía 1: Dashboard de Soberanía:** Conectado a `SystemicObserver` y `sovereigntyService`. Las banderas de sistema y alertas ahora responden exclusivamente a la disponibilidad del backend.
- **Vía 1: Control de Autonomía:** Sincronizado con el Motor de Optimización Ecosistémica (`/admin/optimization/`).
- **Vía 2: Gestión Comercial (Facturación):** Consumo real de `/api/v1/mi-negocio/comercial/facturas-venta/`.
- **Vía 3: Landing Chat:** Integrado con `SADI Engine` para calificación de leads, con manejo de errores institucionales crudos.

## 2. Módulos Bloqueados (La Verdad Incómoda)

En cumplimiento de la directriz, se han bloqueado o marcado como "No Disponibles" los módulos que carecen de soporte real en el backend:

| Módulo | Estado en UI | Causa Técnica del Bloqueo |
| :--- | :--- | :--- |
| **Supervisión de Agentes** | BLOQUEADO | Endpoint de jerarquía SARITA no expuesto en el Kernel. |
| **Bitácora de Soberanía** | NO DISPONIBLE | Falta de servicio de humanización de logs de auditoría. |
| **Centro GRC** | VACÍO / SNAPSHOT | Ausencia de motor de riesgos dinámico en el backend. |
| **Centro de Operaciones** | BLOQUEADO | El motor de descomposición de servicios no posee persistencia activa. |
| **Gestión de Proyectos** | INEXISTENTE | Dominio comentado explícitamente en el routing de Django. |
| **SADI Execution Engine** | MOTOR INACTIVO | Ausencia de endpoint de ejecución en la app `sadi_agent`. |

## 3. Dependencias Reales Pendientes

Para desbloquear las funcionalidades restringidas, se requiere:
1. **BE:** Implementar los ViewSets para `GovernanceAuditLog` y `StrategyProposal`.
2. **Dominio:** Unificar los modelos de multi-tenancy (`Tenant` vs `ProviderProfile`) para habilitar la trazabilidad cruzada.
3. **Infraestructura:** Configurar el Result Backend de Celery para permitir el cierre de misiones de los agentes.

## 4. Evidencia Visual (Descripción)

- **Instrucción de Iconos:** Se restauró la visibilidad del sidebar y header corrigiendo los imports fallidos.
- **ViewState:** Todas las páginas bloqueadas utilizan el componente `ViewState` con iconografía de candado o alerta roja y mensajes institucionales de "Bloqueo de Dominio".
- **Header:** Ahora muestra explícitamente el modelo de datos en uso (`Modelo: ProviderProfile`) junto a la Entidad ID.
- **Disclaimer Contable:** Se añadió un banner ámbar en la Gestión Contable advirtiendo sobre la integración parcial del patrimonio.

---
**“Esta fase no busca que el frontend se vea completo, sino que diga la verdad del sistema. Prefiero una UI incómoda pero honesta, que una bonita pero falsa.”**

**[FIRMADO: JULES - CIERRE DE FASE F-CF]**
