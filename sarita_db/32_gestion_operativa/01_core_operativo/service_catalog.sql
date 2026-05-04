CREATE TABLE core.service_catalog_extended (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    provider_id UUID NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    base_price DECIMAL(18,2),

    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT now()
);
