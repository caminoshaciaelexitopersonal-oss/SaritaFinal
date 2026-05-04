CREATE TABLE archival.disposal_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    document_id UUID NOT NULL,
    action_taken TEXT NOT NULL,
    witness_id UUID, -- Usuario que autoriza

    executed_at TIMESTAMP DEFAULT now()
);
