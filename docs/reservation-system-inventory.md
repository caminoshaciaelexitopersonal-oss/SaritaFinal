# INVENTARIO: SISTEMA DE GESTIÓN DE RESERVAS (WEB SOURCE)
**Lead Implementer:** Jules (Senior AI Software Engineer)
**Date:** March 2026

Este documento define las capacidades del sistema de reservas que deben sincronizarse en todo el ecosistema.

## 1. Modelo Conceptual (Reserva)
- **Atributos:** ID, PrestadorID, ClienteID, Servicio, Fecha Inicio, Fecha Fin, Estado, Precio, Notas.
- **Estados Operativos:**
  - `PENDIENTE`: Recién creada, pendiente de pago o validación.
  - `CONFIRMADA`: Pago validado o cupo asegurado.
  - `EN_CURSO`: El turista está consumiendo el servicio.
  - `FINALIZADA`: Servicio completado exitosamente.
  - `CANCELADA`: Anulada por el usuario o sistema.

## 2. Flujo de Integración (POS + ERP)
- Las reservas se transforman en **Ventas POS** al momento de la facturación.
- Afectan la **Ocupación** regional en tiempo real.
- Generan asientos contables en el **ERP** (Libro Mayor) al confirmarse el pago.

## 3. Interfaces Web Referencia
- **Calendario:** Vista mensual/semanal de disponibilidad.
- **Formulario:** Creación manual de reservas con validación de disponibilidad.
- **Lista:** Tabla con filtros por estado y fecha.

## 4. Estrategia de Nivelación (8D)
- **Mobile:** Foco en la confirmación rápida y check-in/out en campo.
- **Desktop:** Gestión avanzada de agenda y vinculación directa con el POS offline.

---
**Gap Detectado:** Desktop tiene el POS pero las reservas no están integradas en la vista de ERP local.
