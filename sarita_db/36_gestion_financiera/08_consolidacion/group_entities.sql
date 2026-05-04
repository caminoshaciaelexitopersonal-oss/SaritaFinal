CREATE TABLE core.group_entities (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    group_id UUID NOT NULL,
    entity_tenant_id UUID NOT NULL, -- La empresa asociada

    participation_percentage DECIMAL(5,2) DEFAULT 100.00,

    joined_at DATE DEFAULT CURRENT_DATE
);
