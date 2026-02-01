# CATÁLOGO DE INTENCIONES VERBALES (SADI) — SISTEMA SARITA

Este catálogo define los comandos semánticos que el orquestador SADI reconoce y delega a la jerarquía SARITA.

---

## 🏛️ 1. Comandos de Gobernanza (SuperAdmin)

| Comando | Intención | Acción en Kernel |
| :--- | :--- | :--- |
| "Aprobar propuesta estratégica [ID]" | `STRATEGY_APPROVE` | Cambia estado a Aprobado y Ejecuta. |
| "Explícame la optimización de finanzas" | `OPTIMIZATION_EXPLAIN` | Consulta hallazgo de IA y lo narra. |
| "Bloquea operaciones en nodo Puerto Gaitán" | `SOVEREIGN_BLOCK` | Intervención manual inmediata. |
| "Muéstrame el log de voz del ecosistema" | `open.voice_audit` | Navegación a panel de auditoría. |

---

## 📈 2. Comandos Comerciales (Prestador)

| Comando | Intención | Acción en Agente |
| :--- | :--- | :--- |
| "Crear campaña para hotel de temporada" | `marketing.create_campaign` | Coronel Marketing inicia diseño. |
| "Enviar correos a leads calificados" | `marketing.send_mass` | Capitán Embudo dispara despacho. |
| "Ver estado del embudo" | `open.funnels` | Navegación a Arquitecto de Embudos. |
| "Regístrame una venta de $500" | `comercial.register_sale` | Genera factura y asiento contable. |

---

## 💰 3. Comandos Contables y Financieros

| Comando | Intención | Acción en Agente |
| :--- | :--- | :--- |
| "Ver balance general" | `open.accounting` | Muestra reporte consolidado. |
| "Cerrar el mes contable de marzo" | `accounting.close_period` | **Requiere Confirmación Verbal**. |
| "Ver flujo de caja proyectado" | `open.cashflow` | Visualiza ROI y LTV/CAC ratio. |
| "Registrar gasto de nómina" | `accounting.add_expense` | Capitán Contable inserta asiento. |

---

## 🛠️ 4. Comandos Operativos

| Comando | Intención | Acción en Agente |
| :--- | :--- | :--- |
| "Registrar incidencia de riesgo en cocina" | `sst.report_incident` | Crea alerta en módulo SST. |
| "Asignar guía a la ruta del Amanecer" | `operativo.assign_resource` | Actualiza agenda operativa. |
| "Ver agenda de reservas de hoy" | `open.reservations` | Abre calendario operativo. |

---

## 🔐 Flujos de Confirmación Requerida
Cualquier comando que implique:
1. Movimiento de fondos > $1,000.
2. Cierre definitivo de periodos.
3. Borrado de registros legales.
4. Envíos masivos a > 100 destinatarios.

**Respuesta obligatoria:** "Confirmo" o "Proceder".
