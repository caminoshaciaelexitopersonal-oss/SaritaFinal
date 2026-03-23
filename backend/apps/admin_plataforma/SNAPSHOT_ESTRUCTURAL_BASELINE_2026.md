# SNAPSHOT ESTRUCTURAL BASELINE (PUNTO CERO) — 2026

## 1. MÉTRICAS BASELINE (ESTADO INICIAL)
Captura del estado del sistema antes de iniciar la consolidación estructural (Fase 1).

| Métrica | Valor | Observaciones |
| :--- | :---: | :--- |
| **Total de Modelos** | 176 | Incluye duplicados entre Admin y Mi Negocio. |
| **Total de Migraciones** | 51 | Solo de los módulos afectados. |
| **Imports Cruzados (Admin -> Mi Negocio)** | 9 | Acoplamiento directo de servicios. |
| **Imports Cruzados (Sarita -> Mi Negocio)** | 48 | Acoplamiento crítico de orquestación IA. |
| **Imports Cruzados (Mi Negocio -> Admin)** | 4 | Infiltración de lógica de holding en tenants. |
| **Total de Endpoints (Views)** | 305 | Alta fragmentación de lógica de presentación. |

---

## 2. ÁRBOL ESTRUCTURAL (SNAPSHOT)
```text
backend/apps/
├── admin_plataforma/
│   ├── facturacion/
│   ├── gestion_archivistica/
│   ├── gestion_comercial/ (Mirror de Mi Negocio)
│   ├── gestion_contable/ (ERP Holding)
│   ├── gestion_financiera/
│   ├── gestion_operativa/ (Mirror de Mi Negocio)
│   ├── services/ (Capa de Integración)
│   └── models.py (Gobernanza)
├── sarita_agents/
│   ├── agents/ (Jerarquía IA)
│   ├── finanzas/
│   ├── marketing/
│   └── orchestrator.py
└── prestadores/mi_negocio/
    ├── gestion_comercial/
    ├── gestion_contable/
    ├── gestion_financiera/
    └── gestion_operativa/
```

---

## 3. IDENTIFICACIÓN DE SERVICIOS DUPLICADOS (CANDIDATOS A CORE)
1.  **Facturación Service:** Duplicado en `admin_plataforma` y `mi_negocio`.
2.  **Operativa Turística:** Clones masivos de lógica en `gestion_operativa`.
3.  **Motores de AI/Contenido:** Duplicados en `gestion_comercial`.

---
**Generado por:** Jules
**Fecha:** Snapshot Punto Cero - 2026
