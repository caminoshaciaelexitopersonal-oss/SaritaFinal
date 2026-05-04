-- Líneas de Factura
CREATE TABLE core.invoice_lines (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    invoice_id UUID NOT NULL, -- FK en 20_global

    producto_id UUID NOT NULL, -- FK en 20_global
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(18,2) NOT NULL,
    subtotal DECIMAL(18,2) NOT NULL,

    created_at TIMESTAMP DEFAULT now()
);
