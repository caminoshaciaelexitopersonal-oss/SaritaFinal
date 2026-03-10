# DIRECTRIZ DE SUBSANACIÓN DE HALLAZGOS Y EXCELENCIA TÉCNICA 2026

**Objetivo:** Transformar el sistema SARITA de un prototipo avanzado a una plataforma de **Talla Mundial (Nivel 10+)**, garantizando la resiliencia sistémica, la paridad total y el cumplimiento de estándares internacionales de producción.

---

## 1. SUBSANACIÓN DEL BACKEND Y LÓGICA CRÍTICA
Para alcanzar la talla mundial, el backend debe eliminar toda incertidumbre algorítmica.

- **[P0] Cálculo de Costos Reales:** Implementar los motores de recálculo en `reservas` y `ai_views` para que la rentabilidad sea trazable en el Ledger inmutable.
- **[P0] Nómina SMMLV 2026:** Finalizar el módulo de liquidación automática cumpliendo con la normativa laboral proyectada, incluyendo el cálculo de provisiones en tiempo real.
- **[P1] Saneamiento de Deuda:** Eliminar los 335 marcadores de deuda técnica (`TODO`, `FIXME`). No se permite código en producción con sentencias `pass` en bloques de excepción.
- **[P1] Optimización de Consultas:** Implementar `select_related` y `prefetch_related` en el 100% de los ViewSets para mantener la latencia < 300ms con 1M+ registros.

## 2. EVOLUCIÓN DE LA INTELIGENCIA ARTIFICIAL (N1-N7)
La jerarquía de agentes debe pasar de la "ejecución de plantillas" a la "toma de decisiones autónoma".

- **Activación de Sargentos (N5):** Reemplazar los stubs de sargentos por coordinadores reales que gestionen el estado de las microtareas de los Soldados (N6).
- **Hardening de Soldados:** Los soldados de dominios periféricos (Marketing, SST) deben integrarse con las APIs externas reales (SendGrid, WhatsApp Cloud) y no solo con mocks.
- **Forensic AI Audit:** Activar el visualizador de `MisionHistory` para que el Super Admin pueda auditar el razonamiento de los agentes en caso de anomalías financieras.

## 3. PARIDAD MULTIPLATAFORMA (THE GLOBAL EXPERIENCE)
La arquitectura unificada debe ser funcional, no solo estructural.

- **Evolución de Bridges:** Convertir los stubs de `panel-admin` y `tablero-prestador` en Mobile y Desktop en interfaces hidratadas con datos reales sincronizados vía `SyncEngine`.
- **Offline Total:** Garantizar que el 100% de las transacciones del POS en Desktop se sincronicen con el Ledger central sin pérdida de integridad SHA-256.
- **Impresión Térmica:** Implementar el driver universal de impresión en la versión Mobile para formalizar la "Factura de Bolsillo".

## 4. ESTÁNDARES DE CLASE MUNDIAL (PRODUCTION READY)
Para operar a escala gubernamental e internacional, el sistema debe cumplir:

- **Disponibilidad:** 99.95% mediante configuración Multi-AZ en AWS RDS y replicación de lectura.
- **Seguridad S-0.3:** Activar el `Kill Switch` global ante detecciones de inyección de intenciones en la capa de IA.
- **Compliance:** Auditoría automatizada de cumplimiento GDPR/CCPA en el módulo de `privacy_vault`.
- **Observabilidad:** Integración total con Prometheus/Grafana para alertas predictivas de agotamiento de recursos.

---

## CRONOGRAMA DE EJECUCIÓN (ROADMAP)

| Fase | Título | Plazo | Meta |
| :--- | :--- | :--- | :--- |
| **I** | **Estabilización de Núcleo** | 30 días | 0 Deuda Técnica P0. |
| **II** | **Alineación de Interfaces** | 45 días | 100% Paridad Funcional. |
| **III** | **Blindaje y Cognición** | 60 días | IA Autónoma y Seguridad Zero-Trust. |
| **IV** | **Certificación Global** | 90 días | Auditoría Externa y Salida a Producción. |

---
**Firmado por Jules.**
*Lead Architect & Senior Engineer.*
**Fecha:** Marzo 2026.
