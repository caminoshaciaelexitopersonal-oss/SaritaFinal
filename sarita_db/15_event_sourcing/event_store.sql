CREATE TABLE events.event_store (
    event_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    aggregate_id UUID NOT NULL,
    aggregate_type VARCHAR(100) NOT NULL,
    event_type VARCHAR(100) NOT NULL,
    payload JSONB NOT NULL,
    version INTEGER NOT NULL,
    metadata JSONB DEFAULT '{}',
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
) PARTITION BY RANGE (created_at);

-- Comentario: Prohibido UPDATE/DELETE en esta tabla vía RLS o Triggers
