-- 41_ai_core/03_execution/agent_executions.sql
CREATE TABLE ai.agent_executions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    agent_id UUID NOT NULL REFERENCES ai.agents_master(id),
    context_id UUID NOT NULL REFERENCES ai.agent_context_universal(id),
    execution_type TEXT NOT NULL, -- REASONING, ACTION, ANALYSIS, CHAT
    input_data JSONB,
    output_data JSONB,
    execution_status TEXT NOT NULL DEFAULT 'PENDING', -- PENDING, COMPLETED, FAILED
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_ae_agent ON ai.agent_executions(agent_id);
CREATE INDEX idx_ae_context ON ai.agent_executions(context_id);
CREATE INDEX idx_ae_trace ON ai.agent_executions(trace_id);
CREATE INDEX idx_ae_tenant ON ai.agent_executions(tenant_id);
