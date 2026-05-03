CREATE TABLE ai_memory.agent_decisions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    agent_id UUID NOT NULL,
    intent VARCHAR(255),
    context JSONB DEFAULT '{}',
    decision TEXT NOT NULL,
    impact_score FLOAT,
    result_metadata JSONB DEFAULT '{}',
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
