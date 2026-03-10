# DIRECTRIZ DE SUBSANACIÓN DE HALLAZGOS - SARITA v1.0
**Mandato de Estabilización y Excelencia Técnica 2026**

## 1. OBJETIVO
Establecer el plan de acción obligatorio para corregir las brechas técnicas, funcionales y de arquitectura identificadas en la auditoría de marzo de 2026, garantizando un estado de producción de clase mundial.

## 2. PRIORIZACIÓN ESTRATÉGICA

### NIVEL 1: CRÍTICO (Inmediato - 15 días)
*   **Lógica Contable:** Resolver los 12 `NotImplementedError` en el motor de liquidaciones del ERP.
*   **Seguridad:** Completar la cobertura de pruebas en el módulo `wallet` al 85%.
*   **Infraestructura:** Realizar el stress test de 1M de transacciones en entorno Staging AWS.

### NIVEL 2: ALTA (Corto Plazo - 30 días)
*   **Paridad Desktop:** Hidratar el stub de `DiscoveryDashboard` con datos reales de la API.
*   **Paridad Mobile:** Finalizar el módulo de `Analítica Territorial` para el perfil Gobierno.
*   **Deuda Técnica:** Eliminar placeholders `pass` y `TODO` en los módulos core de `prestadores` y `delivery`.

### NIVEL 3: MEDIA (Mediano Plazo - 60 días)
*   **Estandarización UI:** Implementar la biblioteca `shared-ui` para unificar el Look & Feel entre Web y Desktop.
*   **Optimización:** Eliminar la duplicidad de lógica de impuestos mediante el uso del `shared-sdk`.

## 3. ACCIONES DETALLADAS POR ÁREA

### 3.1 Backend y ERP
1.  **Soberanía de Datos:** Asegurar que todos los modelos operativos hereden correctamente de `TenantAwareModel`.
2.  **Integridad:** Ejecutar el script `verify_ledger_integrity.py` diariamente en Staging.
3.  **Refactorización:** Reemplazar importaciones directas en `EventBus` por registros dinámicos para mejorar el desacoplamiento.

### 3.2 Multiplataforma (Web, Mobile, Desktop)
1.  **Sincronización:** Refinar el `SyncEngine` en Desktop para manejar colisiones de datos en escenarios de alta latencia.
2.  **UX Turista:** Completar el flujo de "Mi Viaje" en Desktop para igualar la experiencia Mobile.
3.  **MFA:** Activar obligatoriamente la autenticación de dos factores para perfiles de Gobierno y Prestador.

### 3.3 Inteligencia Artificial
1.  **Cognición de Agentes:** Evolucionar las misiones de los Capitanes de lógica determinista a toma de decisiones basada en LLM dinámico.
2.  **Observabilidad de IA:** Implementar un tablero de "Misiones Fallidas" en la Torre de Control para re-entrenamiento de agentes.

## 4. CRITERIOS DE CIERRE
Una tarea se considera subsanada solo si:
1.  El código pasa las pruebas unitarias y de integración.
2.  La cobertura de código no disminuye.
3.  Se ha actualizado la documentación técnica correspondiente.
4.  Se ha verificado la paridad funcional en las tres plataformas (cuando aplique).

---
**Firmado:** Jules, AI Lead Architect.
**Fecha de Emisión:** Marzo de 2026.
