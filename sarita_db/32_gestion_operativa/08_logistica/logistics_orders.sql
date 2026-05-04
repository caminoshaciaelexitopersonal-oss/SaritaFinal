-- Logística
CREATE TABLE core.logistics_orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    operation_id UUID NOT NULL,
    logistics_type TEXT NOT NULL, -- envio, retiro, abastecimiento

    origin_address TEXT,
    destination_address TEXT,

    status TEXT DEFAULT 'pendiente',

    created_at TIMESTAMP DEFAULT now()
);
