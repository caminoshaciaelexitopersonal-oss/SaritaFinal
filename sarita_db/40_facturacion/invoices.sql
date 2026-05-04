-- Facturación Electrónica
CREATE TABLE core.invoices (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    operation_id UUID NOT NULL, -- FK en 20_global

    numero TEXT UNIQUE NOT NULL,
    estado TEXT DEFAULT 'borrador',

    total DECIMAL(18,2) DEFAULT 0.00,
    cufe TEXT, -- Código Único de Factura Electrónica
    qr TEXT,

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
