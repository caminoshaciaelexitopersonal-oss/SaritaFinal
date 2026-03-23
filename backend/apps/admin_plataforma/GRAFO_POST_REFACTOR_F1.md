# GRAFO DE DEPENDENCIAS POST-REFACTOR (FASE 1) — 2026

## 1. ESTADO DE CIRCULARIDAD
Confirmado mediante `validate_architecture.py`: **0 Violaciones**.

## 2. ARQUITECTURA DIRIGIDA POR EVENTOS (POST-F1)
La comunicación entre los macro-dominios ahora ocurre exclusivamente a través de abstracciones e infraestructura compartida.

```text
[sarita_agents]
      │
      │ (Dynamic Dispatch / import_string)
      ▼
[application_services]
      │
      │ (Commands & Events)
      ▼
[admin_plataforma] ◄────(Events)────► [mi_negocio]
      │                                     │
      └───────────────► [core_erp] ◄────────┘
```

## 3. AISLAMIENTO DE IMPLEMENTACIÓN
*   **IA (sarita_agents):** Totalmente desacoplada de los modelos ORM de inquilinos. Solo utiliza rutas de cadena para resolución dinámica.
*   **ERP (QuintupleERPService):** No importa modelos de `mi_negocio`. Emite eventos que son procesados por suscriptores específicos en cada dominio.
*   **Tenants (mi_negocio):** No conocen la existencia del Super Admin. Publican solicitudes de impacto que la Holding captura voluntariamente.

## 4. JERARQUÍA DE CAPAS (UNIDIRECCIONAL)
1.  **Capa Orquestación:** `sarita_agents`
2.  **Capa Servicios de Aplicación:** `application_services`
3.  **Capa Dominio:** `admin_plataforma` / `mi_negocio`
4.  **Capa Núcleo:** `core_erp`

---
**Validación Final:** Cero ciclos detectados entre módulos de alto nivel.
**Próximo Paso:** Restauración gradual de las 5 dimensiones del ERP.
