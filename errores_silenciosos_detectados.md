# Reporte de Errores Silenciosos y Warnings - Fase 4

Este documento registra los errores y warnings detectados en las consolas del navegador y los logs del backend durante el proceso de QA.

## 1. Errores de Frontend (Consola del Navegador)

| Error/Warning | Ubicación | Impacto | Severidad |
| :--- | :--- | :--- | :--- |
| `[React Query] The Hashed Query Key...` | Consola, al navegar entre páginas | Bajo | Informativo |
| `Warning: Each child in a list should have a unique "key" prop.` | Múltiples componentes que renderizan listas (ej. tablas) | Bajo | Menor |

- **Observación:** No se detectaron errores críticos silenciosos (ej. `4xx` o `5xx` en la pestaña de Red que no se manejaran en la UI). Los warnings encontrados son comunes en desarrollo y no afectan la funcionalidad, pero deberían ser limpiados por buenas prácticas.

## 2. Errores de Backend (Logs de Django)

| Error/Warning | Ubicación | Impacto | Severidad |
| :--- | :--- | :--- | :--- |
| `UnorderedObjectListWarning: Pagination may yield inconsistent results...` | Log, al acceder a endpoints de listado sin un `ordering` explícito | Bajo | Menor |
| `UserWarning: app_settings.USERNAME_REQUIRED is deprecated...` | Log, al iniciar el servidor | Nulo | Informativo |

- **Observación:** Al igual que en el frontend, no se detectaron errores `5xx` silenciosos durante la navegación normal. Los `warnings` son de bajo impacto. El más relevante es el `UnorderedObjectListWarning`, que debería solucionarse añadiendo una cláusula `ordering` en los `Meta` de los modelos o en los `ViewSet` para garantizar una paginación consistente.

## Conclusión

El sistema es **relativamente silencioso y estable**. No se encontraron errores críticos que no dieran la cara al usuario. Los `warnings` detectados son de baja prioridad y pueden ser abordados en una fase de limpieza técnica.
