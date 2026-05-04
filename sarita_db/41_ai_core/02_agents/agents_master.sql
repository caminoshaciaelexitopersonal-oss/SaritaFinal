-- 41_ai_core/02_agents/agents_master.sql
CREATE TABLE ai.agents_master (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    agent_name TEXT NOT NULL,
    hierarchy_level INT NOT NULL CHECK (hierarchy_level >= 1),
    specialization TEXT,
    domain_scope TEXT[],
    status TEXT NOT NULL DEFAULT 'ACTIVE',
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_am_status ON ai.agents_master(status);
