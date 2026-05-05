-- ai_core/agent_memory.sql
-- CONSOLIDACIÓN LÓGICA DE MEMORIA SCTA

CREATE TABLE IF NOT EXISTS ai_core.agent_memory_global (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    entity_type TEXT NOT NULL, -- GOVERNMENT, PROVIDER_HOTEL, PROVIDER_RESTAURANT, GUIDE, TOURIST
    entity_id UUID NOT NULL,
    agent_id UUID NOT NULL,
    context_id UUID NOT NULL,
    trace_id UUID NOT NULL,

    memory_content JSONB NOT NULL,
    relevance_score NUMERIC DEFAULT 0.5,

    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_amg_entity ON ai_core.agent_memory_global(entity_type, entity_id);
CREATE INDEX idx_amg_tenant ON ai_core.agent_memory_global(tenant_id);
CREATE INDEX idx_amg_context ON ai_core.agent_memory_global(context_id);
