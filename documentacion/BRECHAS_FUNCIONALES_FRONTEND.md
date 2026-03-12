# BRECHAS FUNCIONALES FRONTEND - FASE F1

## 🔍 Resumen de Funcionalidad
- 🟢 **Funcional Real:** Conexión directa con API, persistencia en BD confirmada.
- 🟠 **Simulado:** Interfaz activa pero con datos hardcoded o lógica de respuesta local (frontend).
- 🔴 **No Funcional:** Elementos visuales sin lógica asociada o bloqueados por errores técnicos.

---

## 🏛️ Vía 1 — Admin Plataforma

| Funcionalidad | Clasificación | Observación |
| :--- | :--- | :--- |
| Auditoría IA | 🟢 Funcional | Llama a `/run_analysis/` en el backend. |
| Aprobación de Propuestas | 🟢 Funcional | Persiste cambio de estado vía API. |
| Intervención Manual | 🔴 No Funcional | Botón visual sin disparador de acción en código. |
| Gestión de Planes | 🟢 Funcional | CRUD completo vía `GestionPlataformaService`. |
| Optimización SEO | 🟠 Simulado | Card informativa con estados estáticos. |

---

## 💼 Vía 2 — Prestador (ERP)

| Funcionalidad | Clasificación | Observación |
| :--- | :--- | :--- |
| Registro de Facturas | 🟢 Funcional | Integrado con el módulo contable del backend. |
| Arquitecto de Embudos | 🔴 No Funcional | Bloqueado por error de compilación (`react-dnd`). |
| Pipeline de Ventas | 🟢 Funcional | Kanban operativo con persistencia de etapas. |
| Carga de Documentos | 🟢 Funcional | Upload operativo a `gestion_archivistica`. |
| Ratios Financieros | 🟠 Simulado | Cálculos basados en datos de ejemplo en el componente. |
| Marketing Multicanal | 🟠 Simulado | Envía campaña a la BD (`scheduled`), pero sin salida real. |

---

## 🚀 Embudo de Ventas (web-ventas-frontend)

| Funcionalidad | Clasificación | Observación |
| :--- | :--- | :--- |
| Chat con SARITA | 🟠 Simulado | Envía texto a API, pero la respuesta se elige en el FE. |
| Reconocimiento de Voz | 🟠 Simulado | El botón cambia estado visual pero no procesa stream de audio. |
| Checkout / Carrito | 🔴 No Funcional | Bloqueado por errores de importación de componentes UI. |

---

## 📋 Diagnóstico de Brechas Críticas
1. **Divergencia en Marketing:** La UI de comunicaciones promete envío multicanal, pero el backend solo registra la intención sin ejecutar el despacho real (Email/SMS).
2. **Dependencia de Mocks en Analítica:** Los dashboards de rentabilidad y salud sistémica en el SuperAdmin utilizan estructuras de datos hardcoded que no reflejan el estado real de los prestadores en tiempo real.
3. **Bloqueo de Conversión:** El error en el Checkout del funnel impide la afiliación de nuevos usuarios, rompiendo el ciclo vital de la plataforma.
