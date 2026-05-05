CREATE TABLE core.ai_lead_generation (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    session_id UUID NOT NULL,
    lead_id UUID NOT NULL,

    discovery_intent TEXT,
    captured_data JSONB,

    created_at TIMESTAMP DEFAULT now()
);
