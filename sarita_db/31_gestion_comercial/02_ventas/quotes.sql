CREATE TABLE core.quotes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    customer_id UUID NOT NULL, -- FK en 20_global
    status TEXT DEFAULT 'borrador', -- borrador, enviada, aceptada, rechazada
    valid_until DATE,
    total DECIMAL(18,2) DEFAULT 0.00,

    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now()
);
