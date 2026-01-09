# Estrategia de Integración del Sistema de Gestión Archivística (SGA)

Este documento detalla la estrategia de archivado para cada tipo de documento clave identificado en los módulos de negocio del ERP "Sarita".

---

## 1. Documento: Factura de Venta (`FacturaVenta`)

-   **Módulo de Origen:** `gestion_comercial`
-   **Punto de Disparo:** `FacturacionService.facturar_operacion_confirmada()`
-   **Descripción:** Documento fiscal y legal que representa una venta completada y aceptada por la DIAN. Su integridad es de máxima criticidad.

### Estrategia de Archivado:

-   **¿Qué datos se archivarán?**
    -   **Formato Primario:** `PDF`. Se deberá generar una representación visual estandarizada de la factura, incluyendo el CUFE y otros detalles fiscales.
    -   **Metadatos:** El `JSON` con los datos del modelo `FacturaVenta` se almacenará como metadato para búsquedas y análisis.

-   **¿Cuándo se archivará?**
    -   **Mecanismo:** En **tiempo real**. La llamada al servicio de archivado se realizará inmediatamente después de que la factura se guarde con el estado final de la DIAN.

-   **¿Qué nivel de seguridad necesita?**
    -   **Nivel:** **Máximo - Notarización Blockchain**.
    -   **Proceso:** El hash SHA-256 del archivo PDF se calculará y se anclará en la blockchain a través del proceso de notarización del SGA (árboles de Merkle).

-   **¿Cómo se clasifica en el SGA?**
    -   **ProcessType Code:** `CONT` (Contabilidad)
    -   **Process Code:** `FACT` (Facturación)
    -   **DocumentType Code:** `FV` (Factura de Venta)

---

## 2. Documento: Asiento Contable (`JournalEntry`)

-   **Módulo de Origen:** `gestion_contable`
-   **Punto de Disparo:** `FacturaVentaAccountingService.registrar_factura_venta()`
-   **Descripción:** Registro fundamental que refleja el impacto de una transacción en el libro mayor. Es la "verdad contable" y su inmutabilidad es crítica para la confianza financiera.

### Estrategia de Archivado:

-   **¿Qué datos se archivarán?**
    -   **Formato Primario:** `JSON`. Se serializará el objeto `JournalEntry` junto con sus `Transaction` hijas a un formato JSON canónico. Este formato es ideal para auditorías automatizadas.

-   **¿Cuándo se archivará?**
    -   **Mecanismo:** En **tiempo real**. Inmediatamente después de que el `JournalEntry` pase la validación del método `clean()`.

-   **¿Qué nivel de seguridad necesita?**
    -   **Nivel:** **Máximo - Notarización Blockchain**.
    -   **Proceso:** El hash SHA-256 del string JSON canónico será enviado para notarización en la blockchain.

-   **¿Cómo se clasifica en el SGA?**
    -   **ProcessType Code:** `CONT` (Contabilidad)
    -   **Process Code:** `CONT-GEN` (Contabilidad General)
    -   **DocumentType Code:** `AC` (Asiento Contable)

---

## 3. Documento: Orden de Pago (`OrdenPago`)

-   **Módulo de Origen:** `gestion_financiera`
-   **Punto de Disparo:** `PagoService.crear_orden_pago_empleado()`
-   **Descripción:** Documento que evidencia una salida de dinero de la empresa (egreso). Crucial para el control de tesorería y auditorías.

### Estrategia de Archivado:

-   **¿Qué datos se archivarán?**
    -   **Formato Primario:** `PDF`. Se generará un comprobante de egreso o recibo de pago en formato PDF.

-   **¿Cuándo se archivará?**
    -   **Mecanismo:** En **tiempo real**, en el momento en que la orden de pago se crea con el estado `PAGADA`.

-   **¿Qué nivel de seguridad necesita?**
    -   **Nivel:** **Alto - Notarización Blockchain**.
    -   **Proceso:** El hash del PDF será anclado en la blockchain.

-   **¿Cómo se clasifica en el SGA?**
    -   **ProcessType Code:** `FIN` (Finanzas)
    -   **Process Code:** `PAGOS` (Pagos y Egresos)
    -   **DocumentType Code:** `OP` (Orden de Pago)

---

## 4. Documento: Registro de Reserva (`Reserva`)

-   **Módulo de Origen:** `gestion_operativa`
-   **Punto de Disparo:** `ReservaViewSet.perform_create()`
-   **Descripción:** Registro operativo que confirma un acuerdo de servicio con un cliente. Su integridad es importante para la gestión, pero de menor criticidad fiscal.

### Estrategia de Archivado:

-   **¿Qué datos se archivarán?**
    -   **Formato Primario:** `JSON`. Se serializarán los datos del modelo `Reserva` a JSON, capturando el estado de la reserva en el momento de su creación.

-   **¿Cuándo se archivará?**
    -   **Mecanismo:** En **tiempo real**, inmediatamente después de que la reserva se guarde en la base de datos.

-   **¿Qué nivel de seguridad necesita?**
    -   **Nivel:** **Medio - Hash simple (SHA-256)**.
    -   **Proceso:** El hash del JSON se calculará y se almacenará en el campo `file_hash_sha256` del `DocumentVersion`. No se enviará para notarización en blockchain, dejando los campos `merkle_root` y `blockchain_transaction` nulos. Esto permite una verificación de integridad interna sin incurrir en costos de transacción de blockchain.

-   **¿Cómo se clasifica en el SGA?**
    -   **ProcessType Code:** `OPER` (Operaciones)
    -   **Process Code:** `RESERV` (Gestión de Reservas)
    -   **DocumentType Code:** `RES-REG` (Registro de Reserva)
