-- Retención y Disposición
CREATE TABLE archival.retention_policies_extended (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    name TEXT NOT NULL,
    years_retention INT NOT NULL,
    legal_base TEXT,

    created_at TIMESTAMP DEFAULT now()
);
