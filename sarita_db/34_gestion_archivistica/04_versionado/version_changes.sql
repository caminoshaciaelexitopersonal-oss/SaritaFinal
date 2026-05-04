CREATE TABLE archival.version_changes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    version_id UUID NOT NULL,
    change_summary TEXT,

    diff_payload JSONB,

    created_at TIMESTAMP DEFAULT now()
);
