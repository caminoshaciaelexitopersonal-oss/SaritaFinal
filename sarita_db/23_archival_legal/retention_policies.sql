CREATE TABLE archival.retention_policies (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    document_type VARCHAR(100) NOT NULL,
    retention_period_years INTEGER NOT NULL,
    legal_basis TEXT,
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
