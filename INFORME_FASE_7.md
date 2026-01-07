# INFORME TÉCNICO – FASE 7: Integración Contable Formal

## 1. Introducción

Este informe detalla la consolidación de la interoperabilidad entre los módulos `gestion_comercial`, `gestion_contable` (incluyendo `nomina`) y `gestion_financiera`, cumpliendo con los objetivos de la Fase 7. Se ha establecido a `gestion_contable` como la única fuente de la verdad para todas las escrituras contables.

## 2. Flujos de Negocio y su Impacto Contable

### 2.1. Flujo Venta -> Contabilidad

*   **Evento Disparador:** Un usuario confirma una `OperacionComercial` (estado pasa a `FACTURADA`).
*   **Servicio Invocado:** `FacturacionService.facturar_operacion_confirmada`
*   **Ruta:** `backend/apps/prestadores/mi_negocio/gestion_comercial/services.py`
*   **Orquestación:**
    1.  El servicio crea una `FacturaVenta`.
    2.  Invoca a `FacturaVentaAccountingService.registrar_factura_venta`.
*   **Servicio Contable Activo:** `FacturaVentaAccountingService`
*   **Ruta:** `backend/apps/prestadores/mi_negocio/gestion_contable/services/facturacion.py`
*   **Resultado Contable:** Se genera un `JournalEntry` balanceado:
    *   **Débito:** Cuentas por Cobrar (Activo).
    *   **Crédito:** Ingresos Operacionales (Ingreso).
    *   **Crédito:** IVA Generado (Pasivo).

### 2.2. Flujo Nómina -> Contabilidad

*   **Evento Disparador:** Un usuario ejecuta la acción `liquidar` sobre una `Planilla`.
*   **Servicio Invocado:** `ContabilidadNominaService.contabilizar_liquidacion`
*   **Ruta:** `backend/apps/prestadores/mi_negocio/gestion_contable/services/nomina.py`
*   **Orquestación:**
    1.  La acción `liquidar_planilla` en `PlanillaViewSet` calcula los valores de la liquidación.
    2.  Invoca al `ContabilidadNominaService`.
*   **Resultado Contable:** Se genera un `JournalEntry` que reconoce los gastos y pasivos:
    *   **Débito:** Gastos de Personal (Prima, Cesantías, etc.).
    *   **Crédito:** Provisiones / Cuentas por Pagar (Pasivo).

### 2.3. Flujo Pago -> Contabilidad

*   **Evento Disparador:** Un usuario ejecuta la acción `pagar` sobre una `Planilla` contabilizada.
*   **Servicio Invocado:** `ContabilidadPagoService.contabilizar_pago`
*   **Ruta:** `backend/apps/prestadores/mi_negocio/gestion_contable/services/pagos.py`
*   **Orquestación:**
    1.  La acción `pagar_planilla` invoca a `PagoService` (en `gestion_financiera`) para crear la `OrdenPago`.
    2.  A continuación, invoca a `ContabilidadPagoService`.
*   **Resultado Contable:** Se genera un `JournalEntry` que cancela el pasivo:
    *   **Débito:** Provisiones / Cuentas por Pagar (Pasivo).
    *   **Crédito:** Bancos (Activo).

## 3. Listado de Servicios Contables Activos

*   **`FacturaVentaAccountingService`**
    *   **Ruta:** `.../gestion_contable/services/facturacion.py`
    *   **Disparador:** Confirmación de `OperacionComercial`.
*   **`ContabilidadNominaService`**
    *   **Ruta:** `.../gestion_contable/services/nomina.py`
    *   **Disparador:** Liquidación de `Planilla`.
*   **`ContabilidadPagoService`**
    *   **Ruta:** `.../gestion_contable/services/pagos.py`
    *   **Disparador:** Creación de `OrdenPago` (desde el pago de nómina o facturas de compra).

## 4. Confirmación Explícita

Se confirma explícitamente que, tras la refactorización de la Fase 7, **no existen escrituras contables (creación de `JournalEntry` o `Transaction`) fuera del módulo `gestion_contable`**. Todos los flujos de negocio que requieren un impacto contable lo hacen a través de la invocación de los servicios especializados dentro de `gestion_contable/services/`.
