CREATE TABLE core.ai_intents_registry (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    name TEXT NOT NULL,
    description TEXT,
    confidence_threshold DECIMAL(3,2) DEFAULT 0.70,

    created_at TIMESTAMP DEFAULT now()
);
