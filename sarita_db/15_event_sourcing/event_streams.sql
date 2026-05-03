CREATE TABLE events.event_streams (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    aggregate_id UUID UNIQUE NOT NULL,
    aggregate_type VARCHAR(100) NOT NULL,
    current_version INTEGER DEFAULT 0,
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
