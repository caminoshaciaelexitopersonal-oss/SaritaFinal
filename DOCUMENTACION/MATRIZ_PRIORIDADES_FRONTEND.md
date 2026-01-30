# MATRIZ DE PRIORIDADES FRONTEND - FASE F1

## 🎯 Estrategia de Reconstrucción
La prioridad se define cruzando el **Impacto en el Negocio** (Conversión/Gobernanza) con la **Factibilidad Técnica** (Bloqueantes actuales).

---

## 📊 Matriz de Prioridades

| Módulo / Pantalla | Prioridad | Impacto | Complejidad | Motivo |
| :--- | :--- | :--- | :--- | :--- |
| **Estabilización de Dependencias** | 🚀 **P0** | Crítico | Media | Bloqueo actual de compilación (react-dnd). |
| **Embudo de Ventas (Checkout)** | 🚀 **P0** | Crítico | Alta | Imposibilidad de afiliar nuevos usuarios. |
| **Dashboard Comercial (ERP)** | 💎 **P1** | Alta | Alta | Núcleo de la promesa de venta de Sarita. |
| **Gobernanza Soberana (Admin)** | 💎 **P1** | Alta | Media | Control y auditoría del sistema por el SuperAdmin. |
| **Gestión Operativa Especializada** | ⚡ **P2** | Media | Alta | Diferenciación competitiva (Hoteles, Restaurantes). |
| **Portal Turístico (Vía 3)** | ✅ **P3** | Media | Baja | Actualmente el módulo más estable y funcional. |
| **SADI Interface (Voz)** | 🧠 **P4** | Alta | Muy Alta | Innovación tecnológica (requiere base estable previa). |

---

## 🛠️ Hoja de Ruta Sugerida para Fase F2

1. **Sprint 0 (Hotfix):** Inyectar dependencias faltantes y limpiar imports en `web-ventas-frontend`.
2. **Sprint 1 (Conversión):** Asegurar que un turista pueda navegar el funnel, elegir un plan y llegar al registro exitoso.
3. **Sprint 2 (Control Maestro):** Consolidar el Panel de Inteligencia Decisora para que el SuperAdmin pueda actuar sobre el sistema.
4. **Sprint 3 (ERP Deep Dive):** Reparar el Arquitecto de Embudos y unificar la lógica contable-financiera visual.

## 🏁 Cierre de Priorización
El éxito de Sarita depende de su capacidad de **vender** (Vía 3/Funnel) y **controlar** (Vía 1/Admin). El ERP (Vía 2) es la herramienta de retención, pero sin los dos primeros pilares operativos, el ecosistema carece de combustible.
