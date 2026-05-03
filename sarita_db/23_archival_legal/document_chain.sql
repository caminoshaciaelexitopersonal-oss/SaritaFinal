CREATE TABLE archival.document_chain (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    document_id UUID NOT NULL,
    previous_hash TEXT,
    current_hash TEXT NOT NULL,
    action VARCHAR(50) NOT NULL,
    actor_id UUID NOT NULL,
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
