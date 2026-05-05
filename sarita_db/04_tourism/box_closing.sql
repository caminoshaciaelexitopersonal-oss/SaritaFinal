CREATE TABLE tourism.box_closing (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    operational_unit_id UUID NOT NULL,
    actor_id UUID NOT NULL,

    total_expected DECIMAL(18,2),
    total_real DECIMAL(18,2),
    difference DECIMAL(18,2),

    closed_at TIMESTAMP DEFAULT now()
);
