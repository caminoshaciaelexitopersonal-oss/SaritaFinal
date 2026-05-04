CREATE TABLE archival.retention_rules (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    policy_id UUID NOT NULL,
    document_type_id UUID NOT NULL,

    disposal_action TEXT NOT NULL, -- delete, archive, anonymize

    created_at TIMESTAMP DEFAULT now()
);
