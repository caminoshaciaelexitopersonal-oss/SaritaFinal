CREATE TABLE archival.lifecycle_transitions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    from_state_id UUID,
    to_state_id UUID NOT NULL,

    allowed_role TEXT,

    created_at TIMESTAMP DEFAULT now()
);
