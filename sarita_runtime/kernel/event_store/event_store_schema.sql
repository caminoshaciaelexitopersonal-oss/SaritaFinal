-- 45.1 — Implementar Sovereign Event Store
-- Append-only immutable log for all ecosystem events

CREATE TABLE IF NOT EXISTS infrastructure.event_store_global (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_type TEXT NOT NULL,
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    correlation_id UUID,
    causation_id UUID,
    payload JSONB NOT NULL,
    version INTEGER DEFAULT 1,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);

CREATE TABLE IF NOT EXISTS infrastructure.event_replay_checkpoints (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    consumer_id TEXT NOT NULL,
    topic_partition TEXT NOT NULL,
    last_offset BIGINT NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    context_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);

CREATE TABLE IF NOT EXISTS infrastructure.event_snapshots (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    entity_id UUID NOT NULL,
    entity_type TEXT NOT NULL, -- e.g., 'WALLET', 'AGENT_STATE'
    snapshot_data JSONB NOT NULL,
    event_version INTEGER NOT NULL,
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    context_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
