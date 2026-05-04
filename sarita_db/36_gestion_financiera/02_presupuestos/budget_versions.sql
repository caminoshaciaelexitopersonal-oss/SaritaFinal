CREATE TABLE core.budget_versions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    budget_id UUID NOT NULL,
    version_number INT NOT NULL,
    change_log TEXT,

    approved_by UUID, -- FK a users
    snapshot_json JSONB NOT NULL,

    created_at TIMESTAMP DEFAULT now()
);
