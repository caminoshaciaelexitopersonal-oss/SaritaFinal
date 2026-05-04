-- 41_ai_core/03_execution/agent_actions.sql
CREATE TABLE ai.agent_actions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    execution_id UUID NOT NULL REFERENCES ai.agent_executions(id),
    action_type TEXT, -- DATABASE_INSERT, API_CALL, EMAIL_SEND
    action_payload JSONB,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_aa_execution ON ai.agent_actions(execution_id);
