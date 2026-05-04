-- 41_ai_core/06_decisions/agent_decisions.sql
CREATE TABLE ai.agent_decisions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    agent_id UUID NOT NULL REFERENCES ai.agents_master(id),
    context_id UUID NOT NULL REFERENCES ai.agent_context_universal(id),
    decision_type TEXT, -- APPROVE_PAYMENT, CANCEL_BOOKING, ESCALATE_INCIDENT
    decision_payload JSONB,
    approved BOOLEAN DEFAULT FALSE,
    executed BOOLEAN DEFAULT FALSE,
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_ad_agent ON ai.agent_decisions(agent_id);
CREATE INDEX idx_ad_context ON ai.agent_decisions(context_id);
CREATE INDEX idx_ad_trace ON ai.agent_decisions(trace_id);
CREATE INDEX idx_ad_tenant ON ai.agent_decisions(tenant_id);
