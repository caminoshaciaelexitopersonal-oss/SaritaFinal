# PLAN DE REUBICACIÓN DE AGENTES - FASE 1.3

## 1. Directriz General

El análisis de la FASE 1.2 concluyó que la arquitectura de agentes en `backend/agents` (la "antigua") es significativamente más rica, específica y funcionalmente superior a la implementación actual en `backend/apps/sarita_agents` (la "nueva").

Por lo tanto, la estrategia principal será una **reubicación y adaptación completas**. El objetivo es transferir la lógica de negocio detallada de los Capitanes y Tenientes antiguos a la nueva estructura para que esta pueda ejecutarla de forma asíncrona y auditable.

## 2. Estrategia de Reubicación

La reubicación se realizará siguiendo un principio de "mover y adaptar":

1.  **Mover:** Se copiarán los directorios y archivos de los Capitanes desde `backend/agents/` a la ubicación equivalente en `backend/apps/sarita_agents/agents/`.
2.  **Adaptar:** Una vez movidos, los archivos de los Capitanes serán modificados para:
    *   Heredar de la nueva clase base `CapitanTemplate` de `sarita_agents`.
    *   Adaptar sus métodos `plan()` y `delegate()` para que funcionen con los nuevos modelos de persistencia (`PlanTáctico`, `TareaDelegada`) y el sistema de tareas Celery.
    *   Ajustar los `imports` para que sean absolutos y consistentes con la nueva estructura de la app de Django.

## 3. Agentes a Reubicar

La siguiente tabla detalla los directorios de Capitanes que serán reubicados. La acción para todos ellos es **✅ Trasladar y Adaptar**.

| Dominio (Coronel) | Subdominio Funcional | Directorio de Capitanes a Mover | Destino |
| :--- | :--- | :--- | :--- |
| `prestadores` | `gestion_archivistica` | `backend/agents/.../capitanes/gestion_archivistica/` | `backend/apps/sarita_agents/.../capitanes/gestion_archivistica/` |
| `prestadores` | `gestion_comercial` | `backend/agents/.../capitanes/gestion_comercial/` | `backend/apps/sarita_agents/.../capitanes/gestion_comercial/` |
| `prestadores` | `gestion_contable` | `backend/agents/.../capitanes/gestion_contable/` | `backend/apps/sarita_agents/.../capitanes/gestion_contable/` |
| `prestadores` | `gestion_financiera` | `backend/agents/.../capitanes/gestion_financiera/` | `backend/apps/sarita_agents/.../capitanes/gestion_financiera/` |
| `prestadores` | `gestion_operativa` | `backend/agents/.../capitanes/gestion_operativa/` | `backend/apps/sarita_agents/.../capitanes/gestion_operativa/` |

*(Nota: Este plan se enfoca en el Coronel `prestadores` como prueba de concepto, pero la misma lógica se aplicará a los demás Coroneles en el futuro).*

## 4. Próximo Paso

Este plan se presentará para su aprobación en la **FASE 1.4**. No se moverá ningún archivo hasta recibir autorización explícita.
