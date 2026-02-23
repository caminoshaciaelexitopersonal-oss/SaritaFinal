# PLAN DE ESTABILIZACIÓN ESTRUCTURAL DEL SUPER ADMIN (SARITA) - 2026

(Pre-Implementación Opción A)

## I. OBJETIVO ESTRATÉGICO
Eliminar la deriva de esquema, la fragmentación financiera y la duplicación estructural para llevar el Super Admin a un estado de **Arquitectura Coherente, Consolidada y Auditable**.

## II. PRINCIPIOS RECTORES
- **Congelación Funcional:** No se agregan nuevas funcionalidades durante la estabilización.
- **Normalización:** Solo se corrige, normaliza y consolida.
- **Simplificación:** Todo cambio debe reducir la complejidad estructural.
- **Auditabilidad:** Todo módulo debe poder auditarse independientemente.

## III. BLOQUES DE ACCIÓN

### BLOQUE 1: CONTROL DE DERIVA DE ESQUEMA
- **Schema Freeze:** Declaración de ventana de congelación de esquema.
- **Normalización UUID:** Migración de IDs enteros a UUID v4.
- **Technical English:** Renombramiento de campos y modelos de Español a Inglés Técnico.
- **Prefijos de Dominio:** Implementación de nombres estandarizados para evitar colisiones.

### BLOQUE 2: CONSOLIDACIÓN FINANCIERA CENTRAL (LEDGER)
- **Financial Ledger Único:** Implementación del modelo `FinancialLedgerEntry` como única fuente de verdad financiera.
- **Cálculo Derivado:** Métricas como MRR, ARR y Comisiones se calculan exclusivamente desde el Ledger.
- **Política "No Finance Outside Ledger":** Todo evento con impacto monetario debe registrarse en el Ledger.

### BLOQUE 3: SUPERVISIÓN OPERATIVA CONSOLIDADA
- **Operational Snapshot Engine:** Motor para consolidar métricas de salud del sistema y de los inquilinos.
- **Dashboard Institucional:** Vista única del Holding con KPIs financieros, operativos y de riesgo.

### BLOQUE 4: REDUCCIÓN DE ACOPLAMIENTO
- **Domain Service Layer:** Implementación de capas de servicio para evitar el acceso directo a modelos.
- **Arquitectura Dirigida por Eventos (EDA):** Conversión de llamadas directas entre apps en eventos del `EventBus`.

### BLOQUE 5: INTEGRIDAD Y NO DUPLICACIÓN
- **Centralización de Entidades Base:** Unificación de modelos de `Tenant`, `Subscription` y `Transaction`.
- **Fuentes de Verdad:** Definición clara de la responsabilidad única de cada modelo.

## IV. ROADMAP DE IMPLEMENTACIÓN

### 🔵 FASE 1: SINCRO ESTRUCTURAL (2–3 semanas)
- [ ] Auditoría total de esquema y mapa de dependencias.
- [ ] Formalización del Freeze técnico.
- [ ] Diseño del plan de migración de datos.

### 🔵 FASE 2: CORE FINANCIERO (3–4 semanas)
- [ ] Implementación del Ledger Central.
- [ ] Migración de flujos financieros al EventBus.
- [ ] Eliminación de cálculos financieros implícitos en modelos dispersos.

### 🔵 FASE 3: VISIBILIDAD INSTITUCIONAL (2–3 semanas)
- [ ] Implementación del Snapshot Engine.
- [ ] Desarrollo del Dashboard consolidado del Holding.
- [ ] Activación de métricas estratégicas en tiempo real.

## V. CRITERIOS DE ÉXITO (GATE DE CALIDAD)
- [ ] 100% de eventos financieros registrados en el Ledger.
- [ ] Cero (0) IDs enteros en modelos nuevos o refactorizados.
- [ ] Eliminación de modelos duplicados entre dominios.
- [ ] Dashboard institucional operativo y verificado.
- [ ] Reducción del acoplamiento circular detectado.

---
**Plan ratificado por Jules - Senior Software Engineer.**
