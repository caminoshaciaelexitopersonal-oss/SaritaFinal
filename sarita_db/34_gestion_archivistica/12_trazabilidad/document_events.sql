CREATE TABLE archival.document_events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    document_id UUID NOT NULL,
    event_type TEXT NOT NULL, -- uploaded, shared, signed, classified

    payload JSONB,
    created_at TIMESTAMP DEFAULT now()
);
