CREATE TABLE ai_memory.agent_events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    source_table VARCHAR(100) NOT NULL,
    record_id UUID NOT NULL,
    event_payload JSONB NOT NULL,
    ai_status VARCHAR(20) DEFAULT 'UNPROCESSED',
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
