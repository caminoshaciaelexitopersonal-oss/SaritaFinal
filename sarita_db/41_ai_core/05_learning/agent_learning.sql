-- 41_ai_core/05_learning/agent_learning.sql
CREATE TABLE ai.agent_learning (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    context_id UUID REFERENCES ai.agent_context_universal(id),
    agent_id UUID REFERENCES ai.agents_master(id),
    pattern TEXT,
    learning_data JSONB,
    impact_score NUMERIC,
    tenant_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_al_agent ON ai.agent_learning(agent_id);
CREATE INDEX idx_al_tenant ON ai.agent_learning(tenant_id);

-- Regla: No aprendizaje sin memoria
CREATE OR REPLACE FUNCTION ai.fn_trg_learning_memory_check()
RETURNS TRIGGER AS $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM ai.agent_memory_global
        WHERE agent_id = NEW.agent_id
        AND context_id = NEW.context_id
    ) THEN
        RAISE EXCEPTION 'SARITA SCTA ERROR: No se puede registrar aprendizaje sin memoria previa asociada';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_learning_memory_check_validation
BEFORE INSERT ON ai.agent_learning
FOR EACH ROW EXECUTE FUNCTION ai.fn_trg_learning_memory_check();
