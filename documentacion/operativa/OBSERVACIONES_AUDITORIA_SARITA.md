# HALLAZGOS CRÍTICOS — AUDITORÍA EXPLORATORIA (FASE PRE-2.1)

## 1. Inconsistencias Jerárquicas (Agentes SARITA)
*   **Falla en Nómina:** El agente `CapitanPagosYTesoreria` (`backend/apps/sarita_agents/agents/general/sarita/coroneles/prestadores/capitanes/gestion_contable/nomina/capitan_pagos_y_tesoreria.py`) hereda de `CapitanTemplate` pero **no implementa el método obligatorio `_get_tenientes()`**. Esto genera una excepción `NotImplementedError` que bloquea la inicialización del `SaritaOrchestrator`.
*   **Agentes Cascarón:** Se detectó una estructura formal de archivos para agentes en los dominios de Nómina, Finanzas y SST, pero con lógica interna vacía o incompleta (herencia base sin especialización), lo que impide la ejecución de misiones reales en estos dominios.

## 2. Estado de Gestión Archivística (Exploración Técnica)
*   **Estructura:** Se ha verificado la existencia de los 8 dominios fundamentales (Captura -> Auditoría).
*   **Modelos:** Los modelos en `gestion_archivistica` poseen la estructura para trazabilidad (UUIDs, hashes de blockchain), pero la integración con el `QuintupleERPService` estaba desconectada antes de la intervención exploratoria.
*   **UI:** El módulo de Archivo Digital en el frontend tiene componentes de visualización funcionales, pero dependía de parches manuales en la API para mostrar datos debido a la falta de inicialización de registros en el Kernel.

## 3. Riesgos Operativos
*   **Bloqueo de Arranque:** El orquestador IA no puede iniciar si un solo Capitán en la cadena de mando tiene errores de importación o métodos no implementados.
*   **Desconexión de Mando:** Algunos agentes de nivel Sargentos no tienen Soldados asignados en el registro del Kernel, rompiendo la regla de "5 Soldados por Sargento" en dominios fuera del Comercial.
