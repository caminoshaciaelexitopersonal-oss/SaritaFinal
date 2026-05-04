CREATE TABLE archival.lifecycle_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    document_id UUID NOT NULL,
    actor_id UUID NOT NULL,

    from_state_id UUID,
    to_state_id UUID NOT NULL,

    remarks TEXT,
    changed_at TIMESTAMP DEFAULT now()
);
