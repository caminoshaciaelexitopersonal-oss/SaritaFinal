-- 41_ai_core/01_context/context_universal.sql
CREATE TABLE ai.agent_context_universal (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    domain TEXT NOT NULL,
    entity_type TEXT NOT NULL,
    entity_id UUID NOT NULL,
    role TEXT,
    metadata JSONB DEFAULT '{}',
    trace_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_acu_tenant ON ai.agent_context_universal(tenant_id);
CREATE INDEX idx_acu_trace ON ai.agent_context_universal(trace_id);
CREATE INDEX idx_acu_entity ON ai.agent_context_universal(entity_type, entity_id);
