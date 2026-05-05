CREATE TABLE core.loyalty_programs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    name TEXT NOT NULL,
    points_per_unit DECIMAL(5,2) DEFAULT 1.00,

    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT now()
);
